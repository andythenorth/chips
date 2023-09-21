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

    def render_nml(self, templates):
        result = RailStation(facility_type=self).render_nml(templates)
        return result


class RailStation(object):
    def __init__(self, **kwargs):
        self.facility_type = kwargs["facility_type"]
        self.spritelayouts = []

    def render_nml(self, templates):
        template = templates["rail_station.pynml"]
        templated_nml = utils.unescape_chameleon_output(
            template(
                station=self,
                # get_perm_num=self.get_perm_num, # !!
                global_constants=global_constants,
                facility_type=self.facility_type,
                # graphics_temp_storage=global_constants.graphics_temp_storage,  # convenience measure # !!
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
        self.animation_rate = animation_rate  # (must be int) optional multiplier to tile's animation rate, set to 1 for same as tile, >1 for faster; leave default (0) to disable animation; < 1 isn't valid and nml won't compile it
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
        tile=None,
        add_to_object_num=None,
    ):
        self.id = id
        self.ground_sprite = ground_sprite
        self.ground_overlay = ground_overlay
        self.building_sprites = building_sprites
        self.smoke_sprites = smoke_sprites
        # Valid fence values: 'ne', 'se', 'sw', 'nw'.  Order is arbitrary.
        self.fences = fences
        # !!!! optionally prevent fences hiding when a station is adjacent.  Same string values as fences.
        self.perma_fences = perma_fences
        self.terrain_aware_ground = terrain_aware_ground  # we don't draw terrain (and climate) aware ground unless explicitly required by the spritelayout, it makes nml compiles slower
        self.tile = tile
        # optionally spritelayouts can cause objects to be defined
        self.add_to_object_num = add_to_object_num

    """
    # !! this is from FIRS - what's it for ?
    def resolve_tile(self, industry):
        for tile in industry.tiles:
            if tile.id == self.tile:
                return tile
    """
