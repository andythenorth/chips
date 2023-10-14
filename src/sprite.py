# handles sprites and related items such as spritesets


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
        self._always_draw = kwargs.get("always_draw", False)
        self.graphics_file_path = kwargs.get("graphics_file_path", None)

    @property
    def always_draw(self):
        # nml wants 0 or 1 for always_draw, not python False or True
        return [0, 1][self._always_draw]

    def get_nml_declaration_for_sprite_in_spritelayout(self, orientation, snow=False):
        # !! CABBAGE nothing happens with snow currently, it's unfinished support - but it would probably index into an alternative spriteset with _snow appended to graphics file path
        return self.spriteset_id + "(" + self.id + ")"


class BufferStopSprite(Sprite):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.width = 64
        self.height = 31
        self.x_offset = -31
        self.y_offset = 0
        self.graphics_file_path = "src/graphics/buffer_stop.png"


class BuildingSprite(Sprite):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # nothing else as of Sept 2023?


class CargoSprite(Sprite):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.x_loc = kwargs["x_loc"]
        self.y_loc = kwargs["y_loc"]
        self.width = 64
        self.height = 65
        self.x_offset = -31 - kwargs["x_offset_adjustment"]
        self.y_offset = -34 - kwargs["y_offset_adjustment"]
        """
        -1 THIS_CARGO_SPRITESHEET                  10 10 09 65 64 -31 -34
        -1 THIS_CARGO_SPRITESHEET                  80 10 09 65 64 -31 -34
        -1 THIS_CARGO_SPRITESHEET                 150 10 09 65 64 -31 -34
        -1 THIS_CARGO_SPRITESHEET                 220 10 09 65 64 -31 -34
        """


class FoundationSprite(Sprite):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.width = 64
        self.height = 31
        self.x_offset = -31
        self.y_offset = 0
        self.graphics_file_path = "src/graphics/foundations.png"


class GroundSprite(Sprite):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.width = 64
        self.height = 31
        self.x_offset = -31
        self.y_offset = 0
        self.graphics_file_path = "src/graphics/ground.png"


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
            raise BaseException(
                "get_sprite_by_id: sprite "
                + sprite_id
                + " not found in spriteset "
                + self.id
            )

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


class SpriteManager(dict):
    """
    CHIPS zips sprites into a limited number of global spritesets.
    This is because station spritelayouts have a limit of 6 spritesets due to size of var 0x10.
    This is a class to manage sprites and spritesets, intended for use as a singleton, which can be passed to templates etc.
    Extends default python dict, as it's a convenient behaviour (the instantiated class instance behaves like a dict object).
    """

    def add_spriteset(self, spriteset_id):
        self[spriteset_id] = Spriteset(id=spriteset_id)

    def add_spritesets_from_id_list(self, spriteset_ids):
        # convience function, can add a list of spritesets by id, wraps add_spriteset
        for spriteset_id in spriteset_ids:
            self.add_spriteset(spriteset_id)

    def add_sprite(self, sprite):
        if (
            self[sprite.spriteset_id].get_sprite_by_id(sprite.id, allow_not_found=True)
            is not None
        ):
            raise BaseException(
                "sprite with id "
                + sprite.id
                + " already exists in spriteset "
                + sprite.spriteset_id
            )
        self[sprite.spriteset_id].append(sprite)

    def add_sprites_from_list(self, sprites):
        # convience function, can add a list of sprites, wraps add_sprite
        for sprite in sprites:
            self.add_sprite(sprite)
