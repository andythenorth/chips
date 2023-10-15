from sprite import FoundationSprite

# labels and x y offsets
foundation_water_and_coast_sprites = {
    "sw_face_flat": (10, 10),
    "se_face_flat": (80, 10),
    "sw_face_corner_raised_w": (150, 10),
    "se_face_corner_raised_e": (220, 10),
    "sw_face_corner_raised_s": (290, 10),
    "se_face_corner_raised_s": (360, 10),
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
