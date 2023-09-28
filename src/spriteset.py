class Spriteset(object):
    # !! pasted from FIRS - needs ported
    """Simple class to hold spritesets"""

    # !! arguably this should be two different classes, one for building/feature spritesets, and one for ground spritesets
    def __init__(
        self,
        id,
        sprites_ne_sw=[],
        type="",
        xoffset=0,
        yoffset=0,
        zoffset=0,
        xextent=16,
        yextent=16,
        # CABBAGE !! do we need animated tiles?
        animation_rate=0,
        custom_sprite_selector=None,
        always_draw=0,
        num_sprites_to_autofill=1,
    ):
        self.id = id
        self.sprites_ne_sw = sprites_ne_sw  # a list of sprites 6-tuples in format (x, y, w, h, xoffs, yoffs)
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

    @property
    def sprites_both_orientations(self):
        # we want to interleave sprites so ne_sw are even numbered, and nw_se are odd numbered
        # this is cascaded up to spritelayouts, then picked up by OpenTTD automatically when picking which spritelayout to use for the orientation
        result = []
        for sprite_ne_sw in self.sprites_ne_sw:
            sprite_nw_se = [
                sprite_ne_sw[0]
                + sprite_ne_sw[2]
                + 6,  # !! CABBAGE this assumes 6px spacing on 64 wide sprites, is this always the case??
                sprite_ne_sw[1],
                sprite_ne_sw[2],
                sprite_ne_sw[3],
                sprite_ne_sw[4],
                sprite_ne_sw[5],
            ]
            result.append(
                {
                    "ne_sw": sprite_ne_sw,
                    "nw_se": sprite_nw_se,
                }
            )
        return result


class SpriteLayout(object):
    """Simple class to hold spritelayouts"""

    def __init__(
        self,
        id,
        rear_building_sprites,
        front_building_sprites,
        fences=[],
        terrain_aware_ground=False,
    ):
        self.id = id
        self.rear_building_sprites = rear_building_sprites
        self.front_building_sprites = front_building_sprites
        # Valid fence values: 'ne', 'se', 'sw', 'nw'.  Order is arbitrary.
        self.fences = fences


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
