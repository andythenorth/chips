from sprite import FoundationSprite

# labels and x y offsets
foundation_water_and_coast_sprites = {
    "nw_se": (10, 10),
    "ne_sw": (80, 10),
    "slope_nw_se": (150, 10),
    "slope_ne_sw": (220, 10),
    "slope_se_nw": (290, 10),
    "slope_sw_ne": (360, 10),
}

def get_water_and_coast_sprites():
    # returns a simple list of sprites
    result = []
    for id, x_y in foundation_water_and_coast_sprites.items():
        sprite = FoundationSprite(
            id=id, x_loc=x_y[0], y_loc=x_y[1], spriteset_id="spriteset_foundations_water_and_coast"
        )
        result.append(sprite)
    return result

def main():
    # nothing, just here for consistency of module interfaces
    pass
