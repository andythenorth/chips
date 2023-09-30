from spriteset import GroundTileSprite

# labels and x offsets
ground_tiles = {
    "dirt_whole_tile": (10, 10),
    "dirt_rear_platform_ne_sw": (10, 50),
    "dirt_front_platform_ne_sw": (10, 90),
    "dirt_rear_platform_nw_se": (10, 130),
    "dirt_front_platform_nw_se": (10, 170),
    "asphalt_whole_tile": (80, 10),
    "asphalt_rear_platform_ne_sw": (80, 50),
    "asphalt_front_platform_ne_sw": (80, 90),
    "asphalt_rear_platform_nw_se": (80, 130),
    "asphalt_front_platform_nw_se": (80, 170),
    "gravel_whole_tile": (150, 10),
    "gravel_rear_platform_ne_sw": (150, 50),
    "gravel_front_platform_ne_sw": (150, 90),
    "gravel_rear_platform_nw_se": (150, 130),
    "gravel_front_platform_nw_se": (150, 170),
    "cobble_whole_tile": (220, 10),
    "cobble_rear_platform_ne_sw": (220, 50),
    "cobble_front_platform_ne_sw": (220, 90),
    "cobble_rear_platform_nw_se": (220, 130),
    "cobble_front_platform_nw_se": (220, 170),
    "pavement_whole_tile": (290, 10),
    "pavement_rear_platform_ne_sw": (290, 50),
    "pavement_front_platform_ne_sw": (290, 90),
    "pavement_rear_platform_nw_se": (290, 130),
    "pavement_front_platform_nw_se": (290, 170),
}


def get_sprites():
    # returns a simple list sprites
    result = []
    for id, x_y in ground_tiles.items():
        sprite = GroundTileSprite(
            id=id, x_loc=x_y[0], y_loc=x_y[1], spriteset_id="spriteset_ground_tiles"
        )
        result.append(sprite)
    return result


def main():
    # nothing, just here for consistency of module interfaces
    pass
