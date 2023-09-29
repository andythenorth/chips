import os
from copy import copy

currentdir = os.curdir

import chips
import global_constants
import utils
from spriteset import SpritesetLegacy, Spriteset, SpriteBuilding


class FacilityType(object):
    """
    Root of all stations.
    A 'facility' optionally provides rail stations, road stops, objects, etc.
    """

    def __init__(self, **kwargs):
        self.id = kwargs["id"]
        self.numeric_id = kwargs["numeric_id"]
        self.spritesets = []
        self.spritelayouts = []
        self.rail_stations = []
        self.road_stops = []
        self.objects = []
        self.provides_snow = kwargs.get("provides_snow", False)
        self.spriteset_id = "spriteset_" + self.id
        for orientation_suffix in ["_ne_sw", "_nw_se"]:
            chips.sprite_manager.add_spriteset(
                spriteset_id=self.spriteset_id + orientation_suffix
            )

    def get_station_numeric_id_offset(self, station):
        result = None
        found_count = 0
        for station_feature_list in [self.rail_stations, self.road_stops, self.objects]:
            if station in station_feature_list:
                result = station_feature_list.index(station)
                found_count += 1
                # we don't break here just in case there are duplicates later - we want to catch them as that would be a bug

        if found_count == 0:
            # Station is not in any feature list? Should *never* be triggered - this code path should only be running if the station is in one of the feature lists
            raise BaseException(
                "station " + str(station) + " not found for facility_type " + self.id
            )
        elif found_count > 1:
            # Should *never* be triggered - we don't have any mechanism for adding a station instance more than once
            raise BaseException(
                "station "
                + str(station)
                + " found more than once for facility_type "
                + self.id
            )
        else:
            return result

    @property
    def station_classes(self):
        return global_constants.station_classes_by_metaclass[self.metaclass]

    def add_sprite(self, **kwargs):
        # auto extend for both needed orientations
        for orientation_suffix, x_loc_modifier in {"_ne_sw": 0, "_nw_se": 70}.items():
            sprite_id = kwargs["id"]
            sprite = SpriteBuilding(
                id=sprite_id,
                x_loc=kwargs["x_y_loc"][0] + x_loc_modifier,
                y_loc=kwargs["x_y_loc"][1],
                width=kwargs["dimensions"][0],
                height=kwargs["dimensions"][1],
                x_offset=kwargs["offsets"][0],
                y_offset=kwargs["offsets"][1],
                graphics_file_path=self.get_graphics_file_path(),
                spriteset_id=self.spriteset_id + orientation_suffix,
            )
            chips.sprite_manager.add_sprite(sprite)

    def add_spritelayout(self, *args, **kwargs):
        new_spritelayout = SpriteLayout(self, *args, **kwargs)
        self.spritelayouts.append(new_spritelayout)
        # returning the new spritelayout isn't essential, but permits the caller giving it a reference for use elsewhere
        return new_spritelayout

    def add_rail_station(self, type, **kwargs):
        match type:
            case "track_tile":
                new_station_type = RailStationTrackTile
            case "non_track_tile":
                new_station_type = RailStationNonTrackTile
        for station_class in self.station_classes:
            self.rail_stations.append(
                new_station_type(
                    station_class=station_class,
                    facility_type=self,
                    **kwargs,
                )
            )

    def add_road_stop(self, type, **kwargs):
        match type:
            case "bay_tile":
                new_station_type = RoadStopBay
            case "drive_through_tile":
                new_station_type = RoadStopDriveThrough
        for station_class in self.station_classes:
            self.road_stops.append(
                new_station_type(
                    station_class=station_class,
                    facility_type=self,
                    **kwargs,
                )
            )

    def add_grf_object(self, type, **kwargs):
        layout = StationLayout(kwargs["layout"])
        for station_class in self.station_classes:
            self.objects.append(
                GRFObject(
                    station_class=station_class,
                    facility_type=self,
                    **kwargs,
                )
            )

    def unpack_sprite_or_spriteset(
        self,
        sprite_or_spriteset,
        orientation,
        snow_overlay=False,
    ):
        # note the annoying edge case where 'empty' should not have a snow overlay
        if (
            snow_overlay == True
            and getattr(sprite_or_spriteset, "type", None) != "empty"
        ):
            suffix = "_snow"
        else:
            suffix = ""
        if isinstance(sprite_or_spriteset, SpritesetLegacy):
            # tiny optimisation, don't use an animation sprite selector if there is no animation
            # !!!! CABBAGE - animation won't work correctly currently, and would need extended to handle the orientations correctly (ne-sw = even, nw-se = odd)
            if sprite_or_spriteset.animation_rate > 0:
                if sprite_or_spriteset.custom_sprite_selector:
                    sprite_selector = (
                        str(sprite_or_spriteset.animation_rate)
                        + "*"
                        + sprite_or_spriteset.custom_sprite_selector
                    )
                else:
                    sprite_selector = (
                        str(sprite_or_spriteset.animation_rate) + "* (animation_frame)"
                    )
            else:
                match orientation:
                    case "ne_sw":
                        sprite_selector = str(0)
                    case "nw_se":
                        sprite_selector = str(1)
            if sprite_or_spriteset.type != "":
                # ground tile assumes sprite_or_spriteset.type will always map to a ground_tile type
                # have to accomodate number of frames needed (num_sprites_to_autofill) for animated spritelayouts
                # !! if this is failing, look if the required number of frames is provided in ground_tiles.pynml
                """
                # !!! CABBAGE - this is copy-paste from FIRS, might not be be needed as there are no animations yet?
                if (
                    sprite_or_spriteset.num_sprites_to_autofill
                    not in global_constants.animated_ground_tile_frame_counts
                ):
                    raise BaseException(
                        self.id
                        + " needs global_constants.animated_ground_tile_frame_counts extended to add a frame count of "
                        + str(sprite_or_spriteset.num_sprites_to_autofill)
                    )
                """
                return (
                    "spriteset_ground_tile_"
                    + sprite_or_spriteset.type
                    + "_"
                    + str(sprite_or_spriteset.num_sprites_to_autofill)
                )
            else:
                # default result is a spriteset name and optional frame number
                return sprite_or_spriteset.id + suffix + "(" + sprite_selector + ")"
        if isinstance(sprite_or_spriteset, Sprite):
            return getattr(sprite_or_spriteset, "sprite_number" + suffix)

    def get_spritelayout_by_id(self, spritelayout_id):
        for spritelayout in self.spritelayouts:
            if spritelayout.id == spritelayout_id:
                return spritelayout
        # should not be reached
        return None

    @property
    def rail_spritelayouts(self):
        # only return spritelayouts actually used for this feature type, there may be other spritelayouts for other feature types not needed here
        result = {
            "track": [],
            "non_track": [],
        }
        for rail_station in self.rail_stations:
            for spritelayout_id in rail_station.layout.spritelayout_ids:
                # check we don't repeat spritelayout ids, won't be valid
                if spritelayout_id not in result[rail_station.track_non_track]:
                    result[rail_station.track_non_track].append(spritelayout_id)
        for track_non_track, spritelayout_ids in result.items():
            result[track_non_track] = [
                self.get_spritelayout_by_id(spritelayout_id)
                for spritelayout_id in spritelayout_ids
            ]
        return result

    def get_graphics_file_path(self, terrain=None):
        if terrain == "snow" and self.provides_snow:
            terrain_suffix = "_snow"
        else:
            terrain_suffix = ""
        # don't use os.path.join here, this returns a string for use by nml
        return "src/graphics/" + self.id + terrain_suffix + ".png"

    def render_nml(self, templates):
        station_feature_template_mapping = [
            (self.rail_stations, "rail_stations.pynml"),
            #            (self.road_stops, "road_stops.pynml"),
            #            (self.rail_stations, "objects.pynml"),
        ]
        result = ""
        for stations, template_name in station_feature_template_mapping:
            template = templates[template_name]
            templated_nml = utils.unescape_chameleon_output(
                template(
                    facility_type=self,
                    stations=stations,
                    # get_perm_num=self.get_perm_num, # !!
                    global_constants=global_constants,
                    graphics_temp_storage=global_constants.graphics_temp_storage,  # convenience measure # !!
                    # registered_industries=registered_industries, # !!
                    utils=utils,
                    sprite_manager=chips.sprite_manager,
                )
            )
            result += templated_nml
        return result


class FacilityTypeIndustry(FacilityType):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.metaclass = "industry"


class FacilityTypeTown(FacilityType):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.metaclass = "town"


class Station(object):
    """
    Base class for all stations, instances of which are composed as needed by FacilityType.
    Note that in CHIPS, rail station, road stop, and objects are all 'stations'...
    ...unlike the grf specs, where a station is always a rail station (even if it doesn't provide track).
    """

    def __init__(self, **kwargs):
        self.station_class = kwargs["station_class"]
        self.facility_type = kwargs["facility_type"]
        self.layout = StationLayout(kwargs["layout"])

    @property
    def id(self):
        # id suffix maker
        # !! seems safe enough here to derive id suffixes at compile time (unlike industries or vehicles which need to refer to each other)
        # !! however if we want to cross-refer station tiles, then we'll need to derive these IDs earlier
        return (
            self.facility_type.id
            + "_"
            + str(self.facility_type.get_station_numeric_id_offset(self))
        )

    @property
    def numeric_id(self):
        # numeric id maker
        # !! seems safe enough here to derive numeric ids at compile time (unlike industries or vehicles which need to refer to each other)
        # !! however if we want to cross-refer station tiles, then we'll need to derive these IDs earlier
        return (
            self.facility_type.numeric_id
            + self.facility_type.get_station_numeric_id_offset(self)
        )

    @property
    def classname_string_id(self):
        return "STR_NAME_STATION_CLASS_" + self.station_class["class_id"]

    @property
    def name_string_id(self):
        return "STR_NAME_STATION_" + self.facility_type.id.upper()

    @property
    def spritelayouts_as_nml_array(self):
        result = []
        # extend per orientation, with ne-sw as even numbered, and nw-se as odd numbered, which OpenTTD will then pick up appropriate to each orientation
        for orientation_suffix in ["_ne_sw", "_nw_se"]:
            for spritelayout_id in self.layout.spritelayout_ids:
                result.append(
                    spritelayout_id + "_" + self.track_non_track + orientation_suffix
                )
        return "[" + ",".join(result) + "]"

    @property
    def ground_type(self):
        return self.station_class["default_ground_type"]


class RailStationBase(Station):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # set catenary wire and pylon drawing appropriately in subclass, or allow over-riding per tile
        self._hide_pylon_tiles = None
        self._hide_wire_tiles = None
        # set non_traversable_tiles appropriately in subclass, no over-riding per tile
        self.non_traversable_tiles = None
        # set track_non_track appropriately in subclass, no over-riding per tile
        self.track_non_track = None

    @property
    def draw_pylon_tiles(self):
        # note that this inverts hide_pylon_tiles, as it makes the interface less likely to cause the wearing of clown shoes in public
        match self._hide_pylon_tiles:
            case False:
                return "STAT_ALL_TILES"
            case True:
                return 0

    @property
    def hide_wire_tiles(self):
        match self._hide_wire_tiles:
            case True:
                return "STAT_ALL_TILES"
            case False:
                return 0

    def get_custom_sprite_index_structs(self, ground_subtypes):
        # index into the global ground_tiles spriteset, with a label included for convenience of debugging
        result = []
        for ground_subtype in ground_subtypes:
            sprite_id = self.ground_type + "_" + ground_subtype
            # returns a 3 tuple of index in spriteset, storage to use in graphics chain, and label for convenience of debugging
            result.append(
                (
                    chips.sprite_manager[
                        "spriteset_ground_tiles"
                    ].get_index_for_sprite_by_id(sprite_id),
                    global_constants.graphics_temp_storage["var_sprite_" + ground_subtype],
                    sprite_id,
                )
            )
        return result


class RailStationTrackTile(RailStationBase):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.non_traversable_tiles = 0
        self.track_non_track = "track"
        # default to always drawing wire catenary and pylons - over-ride per station as needed
        self._hide_pylon_tiles = kwargs.get("hide_pylon_tiles", False)
        self._hide_wire_tiles = kwargs.get("hide_wire_tiles", False)

    @property
    def custom_sprite_index_structs(self):
        ground_subtypes = [
            "rear_platform_ne_sw",
            "rear_platform_nw_se",
            "front_platform_ne_sw",
            "front_platform_nw_se",
        ]
        return self.get_custom_sprite_index_structs(ground_subtypes)


class RailStationNonTrackTile(RailStationBase):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.non_traversable_tiles = "STAT_ALL_TILES"
        self.track_non_track = "non_track"
        # never draw wire catenary and pylons for non-track tiles - makes no sense(?)
        self._hide_pylon_tiles = True
        self._hide_wire_tiles = True

    @property
    def custom_sprite_index_structs(self):
        ground_subtypes = ["whole_tile"]
        return self.get_custom_sprite_index_structs(ground_subtypes)


class RoadStopBase(Station):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class RoadStopBay(RoadStopBase):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class RoadStopDriveThrough(RoadStopBase):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class GRFObject(Station):
    """Stubby class to hold objects - GRFObject to avoid conflating with built-in python classname"""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class StationLayout(list):
    """
    Base class to hold station layouts
    Extends default python list, as it's a convenient behaviour (the instantiated class instance behaves like a list object).
    """

    def __init__(
        self,
        layout,
    ):
        for layout_entry in layout:
            self.append(layout_entry)
        self.validate_xy()

    def validate_xy(self):
        # in-game station layouts must not have negative xy offsets
        for x, y, spritelayout_id in self:
            for offset_dir in [x, y]:
                if offset_dir < 0:
                    raise BaseException(
                        "Negative values are invalid for x or y offsets: "
                        + self.id
                        + " ("
                        + str(x)
                        + ", "
                        + str(y)
                        + ")"
                    )
        # xy offset pairs must be unique per layout
        xy_offsets = [(i[0], i[1]) for i in self]
        for x, y in xy_offsets:
            if xy_offsets.count((x, y)) > 1:
                raise BaseException(
                    "Repeated xy offset pair: " + self.id + " " + str((x, y))
                )

    @property
    def spritelayout_ids(self):
        # convenience function for when we only want spritelayouts
        result = []
        for x, y, spritelayout_id in self:
            result.append(spritelayout_id)
        return result


class SpriteLayout(object):
    """Simple class to hold spritelayouts"""

    def __init__(
        self,
        facility_type,
        id,
        ground_overlay_sprites,
        rear_building_sprites,
        front_building_sprites,
        terrain_aware_ground=False,
    ):
        self.id = id
        self.facility_type = facility_type
        self._ground_overlay_sprites = ground_overlay_sprites
        self._rear_building_sprites = rear_building_sprites
        self._front_building_sprites = front_building_sprites

    def get_sprites_by_orientation(self, sprite_id_list):
        # we have sprite_ids in local context, so use those to get the actual sprite objects
        # sprites are organised into spriteset per orientation (ne_sw, nw_se), so fetch from the correct spriteset
        result = {}
        for orientation in ["ne_sw", "nw_se"]:
            sprites = []
            spriteset_id = self.facility_type.spriteset_id + "_" + orientation
            for sprite_id in sprite_id_list:
                sprite = chips.sprite_manager[spriteset_id].get_sprite_by_id(sprite_id)
                sprites.append(sprite)
            result[orientation] = sprites
        return result

    @property
    def ground_overlay_sprites(self):
        return self.get_sprites_by_orientation(self._ground_overlay_sprites)

    @property
    def rear_building_sprites(self):
        return self.get_sprites_by_orientation(self._rear_building_sprites)

    @property
    def front_building_sprites(self):
        return self.get_sprites_by_orientation(self._front_building_sprites)
