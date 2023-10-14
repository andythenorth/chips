from sprite import GroundSprite

# labels and x y offsets
ground_sprites = {
    "dirt_whole_tile": (10, 10),
    "dirt_rear_rail_platform_ne_sw": (10, 50),
    "dirt_front_rail_platform_ne_sw": (10, 90),
    "dirt_rear_rail_platform_nw_se": (10, 130),
    "dirt_front_rail_platform_nw_se": (10, 170),
    "dirt_rear_road_platform_ne_sw": (10, 210),
    "dirt_front_road_platform_ne_sw": (10, 250),
    "dirt_rear_road_platform_nw_se": (10, 290),
    "dirt_front_road_platform_nw_se": (10, 330),
    "asphalt_whole_tile": (80, 10),
    "asphalt_rear_rail_platform_ne_sw": (80, 50),
    "asphalt_front_rail_platform_ne_sw": (80, 90),
    "asphalt_rear_rail_platform_nw_se": (80, 130),
    "asphalt_front_rail_platform_nw_se": (80, 170),
    "asphalt_rear_road_platform_ne_sw": (80, 210),
    "asphalt_front_road_platform_ne_sw": (80, 250),
    "asphalt_rear_road_platform_nw_se": (80, 290),
    "asphalt_front_road_platform_nw_se": (80, 330),
    "gravel_whole_tile": (150, 10),
    "gravel_rear_rail_platform_ne_sw": (150, 50),
    "gravel_front_rail_platform_ne_sw": (150, 90),
    "gravel_rear_rail_platform_nw_se": (150, 130),
    "gravel_front_rail_platform_nw_se": (150, 170),
    "gravel_rear_road_platform_ne_sw": (150, 210),
    "gravel_front_road_platform_ne_sw": (150, 250),
    "gravel_rear_road_platform_nw_se": (150, 290),
    "gravel_front_road_platform_nw_se": (150, 330),
    "pavement_whole_tile": (290, 10),
    "pavement_rear_rail_platform_ne_sw": (290, 50),
    "pavement_front_rail_platform_ne_sw": (290, 90),
    "pavement_rear_rail_platform_nw_se": (290, 130),
    "pavement_front_rail_platform_nw_se": (290, 170),
    "pavement_rear_road_platform_ne_sw": (290, 210),
    "pavement_front_road_platform_ne_sw": (290, 250),
    "pavement_rear_road_platform_nw_se": (290, 290),
    "pavement_front_road_platform_nw_se": (290, 330),
}

def get_sprites():
    # returns a simple list sprites
    result = []
    for id, x_y in ground_sprites.items():
        sprite = GroundSprite(
            id=id, x_loc=x_y[0], y_loc=x_y[1], spriteset_id="spriteset_ground"
        )
        result.append(sprite)
    return result


def main():
    # nothing, just here for consistency of module interfaces
    pass
