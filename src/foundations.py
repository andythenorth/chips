from sprite import FoundationSprite

# labels and x y offsets
foundation_water_and_coast_sprites = {
    "no_foundation": (10, 10),
    "sw_face_flat": (80, 10),
    "se_face_flat": (150, 10),
    "sw_face_corner_raised_w": (220, 10),
    "se_face_corner_raised_e": (290, 10),
    "sw_face_corner_raised_s": (360, 10),
    "se_face_corner_raised_s": (430, 10),
}

# see also https://newgrf-specs.tt-wiki.net/wiki/NML:List_of_tile_slopes
slope_mapping = {
    "SLOPE_FLAT": {
        "foundations": ["sw_face_flat", "se_face_flat"],
        "water_checks": [(0, 0)],
        "base_set_sprite": 4078, # SPR_EMPTY in OpenTTD sprites.h empty (transparent blue) sprite
    },
    "SLOPE_W": {
        "foundations": ["sw_face_corner_raised_w", "se_face_flat"],
        "water_checks": [(0, 1), (-1, 0)],
        "base_set_sprite": 5450,
    },
    "SLOPE_S": {
        "foundations": ["sw_face_corner_raised_s", "se_face_corner_raised_s"],
        "water_checks": [(0, -1), (-1, 0)],
        "base_set_sprite": 5465,
    },
    "SLOPE_E": {
        "foundations": ["sw_face_flat", "se_face_corner_raised_e"],
        "water_checks": [(0, -1), (1, 0)],
        "base_set_sprite": 5431,
    },
    "SLOPE_N": {
        "foundations": ["sw_face_flat", "se_face_flat"],
        "water_checks": [(0, 1), (1, 0)],
        "base_set_sprite": 5471,
    },
    "SLOPE_NW": {
        "foundations": ["sw_face_corner_raised_w", "se_face_flat"],
        "water_checks": [(0, 1), (1, 1), (-1, 1)],
        "base_set_sprite": 5450,
    },
    "SLOPE_SW": {
        "foundations": ["no_foundation", "se_face_corner_raised_s"],
        "water_checks": [(-1, 0), (-1, 1), (-1, -1)],
        "base_set_sprite": 5466,
    },
    "SLOPE_SE": {
        "foundations": ["sw_face_corner_raised_s", "no_foundation"],
        "water_checks": [(0, -1), (1, -1), (-1, -1)],
        "base_set_sprite": 5469,
    },
    "SLOPE_NE": {
        "foundations": ["sw_face_flat", "se_face_corner_raised_e"],
        "water_checks": [(1, 0), (1, 1), (1, -1)],
        "base_set_sprite": 5431,
    },
    "SLOPE_EW": {
        "foundations": ["sw_face_corner_raised_w", "se_face_corner_raised_e"],
        "water_checks": [(0,1), (1, 0), (1, 1)],
        "base_set_sprite": 5468,
    },
    "SLOPE_NS": {
        "foundations": ["sw_face_corner_raised_s", "se_face_corner_raised_s"],
        "water_checks": [(-1, 1), (1, -1)],
        "base_set_sprite": 5465,
    },
    "SLOPE_NWS": {
        "foundations": ["no_foundation", "se_face_corner_raised_s"],
        "water_checks": [(-1, 0), (-1, 1)],
        "base_set_sprite": 5466,
    },
    "SLOPE_WSE": {
        "foundations": ["no_foundation", "no_foundation"],
        "water_checks": [],
        "base_set_sprite": 4078, # SPR_EMPTY in OpenTTD sprites.h empty (transparent blue) sprite
    },
    "SLOPE_SEN": {
        "foundations": ["sw_face_corner_raised_s", "no_foundation"],
        "water_checks": [(1, 0), (1, -1)],
        "base_set_sprite": 5469,
    },
    "SLOPE_ENW": {
        "foundations": ["sw_face_corner_raised_w", "se_face_corner_raised_e"],
        "water_checks": [(0, 1), (1, 0), (1, 1)],
        "base_set_sprite": 5468,
    },
}


def custom_foundation_mapping_for_nml_slope_check():
    result = []
    for slope_name, slope_data in slope_mapping.items():
        result.append(
            {
                "slope_name": slope_name,
                "sw_face": list(foundation_water_and_coast_sprites.keys()).index(
                    slope_data["foundations"][0]
                ),
                "se_face": list(foundation_water_and_coast_sprites.keys()).index(
                    slope_data["foundations"][1]
                ),
            }
        )
    return result


def base_set_foundation_mapping_for_nml_slope_check():
    result = []
    for slope_name, slope_data in slope_mapping.items():
        result.append(
            {
                "slope_name": slope_name,
                "base_set_sprite": slope_data["base_set_sprite"],
            }
        )
    return result



def tile_offset_mapping_for_nml_water_check():
    result = []
    for slope_name, slope_data in slope_mapping.items():
        result.append(
            {
                "slope_name": slope_name,
                "offsets": slope_data["water_checks"],
            }
        )
    return result


def get_water_and_coast_sprites():
    # returns a simple list of sprites
    result = []
    for id, x_y in foundation_water_and_coast_sprites.items():
        sprite = FoundationSprite(
            id=id,
            x_loc=x_y[0],
            y_loc=x_y[1],
            spriteset_id="spriteset_foundations_water_and_coast",
        )
        result.append(sprite)
    return result


def main():
    # nothing, just here for consistency of module interfaces
    pass
