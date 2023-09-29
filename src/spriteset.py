import chips

class Spriteset(list):
    """
    Simple class to hold spritesets.
    Derives from dict for convenience, as we want to store a list of sprites in it.
    """

    def __init__(
        self,
        id,
    ):
        self.id = id

    def get_sprite_by_id(self, sprite_id, allow_not_found=False):
        for sprite in self:
            if sprite.id == sprite_id:
                return sprite
        # if not found we can either fail or return None
        if allow_not_found:
            return None
        else:
            raise BaseException("get_sprite_by_id: sprite " + sprite_id + " not found in spriteset " + self.id)

    def get_index_for_sprite_by_id(self, sprite_id):
        sprite = self.get_sprite_by_id(sprite_id)
        return self.index(sprite)


class SpritesetLegacy(object):
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


class Sprite(object):
    """Simple class to hold sprite metadata"""

    def __init__(
        self,
        **kwargs,
    ):
        self.id = kwargs["id"]
        self.spriteset_id = kwargs["spriteset_id"]
        self.x_loc = kwargs.get("x_loc", None)
        self.y_loc = kwargs.get("y_loc", None)
        self.width = kwargs.get("width", None)
        self.height = kwargs.get("height", None)
        self.x_offset = kwargs.get("x_offset", None)
        self.y_offset = kwargs.get("y_offset", None)
        self.graphics_file_path = kwargs.get("graphics_file_path", None)

    def get_nml_declaration_for_spritelayout(self, orientation):
        return self.spriteset_id + "(" + self.id + ")"


class SpriteBuilding(Sprite):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # nothing else as of Sept 2023?


class GroundTileSprite(Sprite):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.width = 64
        self.height = 31
        self.x_offset = -31
        self.y_offset = 0
        self.graphics_file_path = "src/graphics/ground_tiles.png"
