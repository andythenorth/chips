import os

currentdir = os.curdir

import global_constants
import utils


class FacilityType(object):
    """
    Core class, used as a container that optionally provides rail stations, road stops, objects, etc.
    Note that 'Station' in CHIPS has a different meaning to 'station' in the grf specs.
    In the grf specs, a station is always a rail station (even when it doesn't provide track).
    """

    def __init__(self, **kwargs):
        self.id = kwargs["id"]
        self.numeric_id = kwargs["numeric_id"]
        self.spritesets = []
        self.spritelayouts = []
        self.provides_snow = kwargs.get("provides_snow", False)
        # over-ride station_class in subclasses
        self.station_class = None

    def render_nml(self, templates):
        result = RailStation(facility_type=self).render_nml(templates)
        return result

    def add_spriteset(self, *args, **kwargs):
        id = self.id + "_spriteset_" + str(len(self.spritesets))
        new_spriteset = Spriteset(id=id, *args, **kwargs)
        self.spritesets.append(new_spriteset)
        # returning the new spriteset isn't essential, but permits the caller giving it a reference for use elsewhere
        return new_spriteset

    def add_spritelayout(self, *args, **kwargs):
        new_spritelayout = SpriteLayout(*args, **kwargs)
        self.spritelayouts.append(new_spritelayout)
        # returning the new spritelayout isn't essential, but permits the caller giving it a reference for use elsewhere
        return new_spritelayout

    def unpack_sprite_or_spriteset(
        self,
        sprite_or_spriteset,
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
        if isinstance(sprite_or_spriteset, Spriteset):
            # tiny optimisation, don't use an animation sprite selector if there is no animation
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
                sprite_selector = "0"
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


    def get_graphics_file_path(self, terrain=None, construction_state_num=None):
        if terrain == "snow" and self.provides_snow:
            terrain_suffix = "_snow"
        else:
            terrain_suffix = ""
        # don't use os.path.join here, this returns a string for use by nml
        return '"src/graphics/' + self.id + terrain_suffix + '.png"'


class FacilityTypeIndustry(FacilityType):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.station_class = "CHIN"


class FacilityTypeTown(FacilityType):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.station_class = "CHTO"


class RailStation(object):
    def __init__(self, **kwargs):
        self.facility_type = kwargs["facility_type"]

    def render_nml(self, templates):
        template = templates["rail_station.pynml"]
        templated_nml = utils.unescape_chameleon_output(
            template(
                station=self,
                # get_perm_num=self.get_perm_num, # !!
                global_constants=global_constants,
                facility_type=self.facility_type,
                graphics_temp_storage=global_constants.graphics_temp_storage,  # convenience measure # !!
                # registered_industries=registered_industries, # !!
                utils=utils,
            )
        )
        return templated_nml


class RoadStop(object):
    def __init__(self, **kwargs):
        pass
        # not implemented

    def render_nml(self):
        pass
        # not implemented


class GRFObject(object):
    """Stubby class to hold objects - GRFObject to avoid conflating with built-in python classname"""

    def __init__(self, **kwargs):
        pass
        # not implemented

    def render_nml(self):
        pass
        # not implemented


class Spriteset(object):
    # !! pasted from FIRS - needs ported
    """Simple class to hold spritesets"""

    # !! arguably this should be two different classes, one for building/feature spritesets, and one for ground spritesets
    def __init__(
        self,
        id,
        sprites=[],
        type="",
        xoffset=0,
        yoffset=0,
        zoffset=0,
        xextent=16,
        yextent=16,
        animation_rate=0,
        custom_sprite_selector=None,
        always_draw=0,
        num_sprites_to_autofill=1,
    ):
        self.id = id
        self.sprites = (
            sprites  # a list of sprites 6-tuples in format (x, y, w, h, xoffs, yoffs)
        )
        self.type = type  # set to ground or other special types, or omit for default (building, greeble, foundations etc - graphics from png named same as industry)
        self.animation_rate = animation_rate  # (must be int)
        self.custom_sprite_selector = custom_sprite_selector
        self.num_sprites_to_autofill = num_sprites_to_autofill  # create n sprites per sprite passed (optional convenience method for use where spriteset sizes must match; set value to same as size of largest spriteset)
        # optional parameters for offsets and extents for the *spritelayout* to use with this sprite (read nml spritelayout docs to see use)
        # (more convenient to store on the sprite, even though consumed by spritelayout, as they tend to be constant in most cases where the sprite is used)
        self.xoffset = xoffset
        self.yoffset = yoffset
        self.zoffset = zoffset
        self.xextent = xextent  # set extents to x/y/z sizes of largest sprite in spriteset, or omit for default (16)
        self.yextent = yextent
        self.zextent = 32  # it's of limited use setting zextent, just make it 32 and be done with it
        self.always_draw = always_draw


class SpriteLayout(object):
    """Simple class to hold spritelayouts"""

    def __init__(
        self,
        id,
        ground_sprite,
        ground_overlay,
        building_sprites,
        fences=[],
        perma_fences=[],
        terrain_aware_ground=False,
    ):
        self.id = id
        self.ground_sprite = ground_sprite
        self.ground_overlay = ground_overlay
        self.building_sprites = building_sprites
        # Valid fence values: 'ne', 'se', 'sw', 'nw'.  Order is arbitrary.
        self.fences = fences
        # !!!! optionally prevent fences hiding when a station is adjacent.  Same string values as fences.
        self.perma_fences = perma_fences
        self.terrain_aware_ground = terrain_aware_ground  # we don't draw terrain (and climate) aware ground unless explicitly required by the spritelayout, it makes nml compiles slower
