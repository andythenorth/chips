from station import FacilityTypeIndustry


def main():
    facility_type = FacilityTypeIndustry(
        id="foundry_buildings",
    )

    facility_type.add_sprite(
        id="ground_overlay_platforms_rail",
        x_y_loc=(10, 290),
        dimensions=(64, 31),
        offsets=(-31, 0),
    )
    facility_type.add_sprite(
        id="ground_overlay_whole_tile",
        x_y_loc=(10, 250),
        dimensions=(64, 31),
        offsets=(-31, 0),
    )
    facility_type.add_sprite(
        id="sprite_building_large",
        x_y_loc=(10, 10),
        dimensions=(64, 145),
        offsets=(-31, -114),
    )
    facility_type.add_sprite(
        id="sprite_building_large_rear_legs_rail",
        x_y_loc=(10, 170),
        dimensions=(64, 65),
        offsets=(-31, -34),
    )
    facility_type.add_sprite(
        id="sprite_building_large_rear_legs_road",
        x_y_loc=(10, 490),
        dimensions=(64, 65),
        offsets=(-31, -34),
    )
    facility_type.add_sprite(
        id="sprite_building_small",
        x_y_loc=(150, 10),
        dimensions=(64, 145),
        offsets=(-31, -114),
    )
    facility_type.add_sprite(
        id="sprite_building_small_rear_legs",
        x_y_loc=(150, 170),
        dimensions=(64, 65),
        offsets=(-31, -34),
    )
    facility_type.add_sprite(
        id="sprite_enclosed_shed_1_rail",
        x_y_loc=(290, 10),
        dimensions=(64, 145),
        offsets=(-31, -114),
    )
    facility_type.add_sprite(
        id="sprite_enclosed_shed_1_rear_wall_rail",
        x_y_loc=(290, 170),
        dimensions=(64, 65),
        offsets=(-31, -34),
    )
    facility_type.add_sprite(
        id="sprite_enclosed_shed_1_road",
        x_y_loc=(290, 330),
        dimensions=(64, 145),
        offsets=(-31, -114),
    )
    facility_type.add_sprite(
        id="sprite_enclosed_shed_1_rear_wall_road",
        x_y_loc=(290, 490),
        dimensions=(64, 65),
        offsets=(-31, -34),
    )
    """
    facility_type.add_sprite(
        id="sprite_enclosed_shed_1_midle_road",
        x_y_loc=(290, 570),
        dimensions=(64, 65),
        offsets=(-31, -34),
    )
    """

    facility_type.add_spritelayout(
        id="foundry_buildings_spritelayout_1_rail",
        ground_overlay_sprites=["ground_overlay_platforms_rail"],
        rear_structure_sprites=["sprite_building_large_rear_legs_rail"],
        main_structure_sprites=["sprite_building_large"],
    )
    facility_type.add_spritelayout(
        id="foundry_buildings_spritelayout_1_whole_tile",
        ground_overlay_sprites=["ground_overlay_whole_tile"],
        rear_structure_sprites=["sprite_building_large_rear_legs_rail"],
        main_structure_sprites=["sprite_building_large"],
    )
    facility_type.add_spritelayout(
        id="foundry_buildings_spritelayout_1_road",
        ground_overlay_sprites=[],
        rear_structure_sprites=["sprite_building_large_rear_legs_road"],
        main_structure_sprites=["sprite_building_large"],
    )
    facility_type.add_spritelayout(
        id="foundry_buildings_spritelayout_2_rail",
        ground_overlay_sprites=["ground_overlay_platforms_rail"],
        rear_structure_sprites=["sprite_building_small_rear_legs"],
        main_structure_sprites=["sprite_building_small"],
    )
    facility_type.add_spritelayout(
        id="foundry_buildings_spritelayout_2_whole_tile",
        ground_overlay_sprites=["ground_overlay_whole_tile"],
        rear_structure_sprites=["sprite_building_small_rear_legs"],
        main_structure_sprites=["sprite_building_small"],
    )
    facility_type.add_spritelayout(
        id="foundry_buildings_spritelayout_3_rail",
        ground_overlay_sprites=["ground_overlay_platforms_rail"],
        rear_structure_sprites=["sprite_enclosed_shed_1_rear_wall_rail"],
        main_structure_sprites=["sprite_enclosed_shed_1_rail"],
    )
    facility_type.add_spritelayout(
        id="foundry_buildings_spritelayout_3_road",
        ground_overlay_sprites=["ground_overlay_platforms_rail"],
        rear_structure_sprites=["sprite_enclosed_shed_1_rear_wall_road"],
        middle_structure_sprites=[],
        main_structure_sprites=["sprite_enclosed_shed_1_road"],
    )
    facility_type.add_spritelayout(
        id="foundry_buildings_spritelayout_3_whole_tile",
        ground_overlay_sprites=["ground_overlay_whole_tile"],
        rear_structure_sprites=["sprite_enclosed_shed_1_rear_wall_rail"],
        main_structure_sprites=["sprite_enclosed_shed_1_rail"],
    )

    facility_type.add_rail_station(
        type="track_tile",
        layout=[
            (
                0,
                0,
                "foundry_buildings_spritelayout_1_rail",
            ),
        ],
    )
    facility_type.add_rail_station(
        type="non_track_tile",
        layout=[
            (
                0,
                0,
                "foundry_buildings_spritelayout_1_whole_tile",
            ),
        ],
    )
    facility_type.add_rail_station(
        type="track_tile",
        layout=[
            (
                0,
                0,
                "foundry_buildings_spritelayout_2_rail",
            ),
        ],
    )
    facility_type.add_rail_station(
        type="non_track_tile",
        layout=[
            (
                0,
                0,
                "foundry_buildings_spritelayout_2_whole_tile",
            ),
        ],
    )
    facility_type.add_rail_station(
        type="track_tile",
        layout=[
            (
                0,
                0,
                "foundry_buildings_spritelayout_3_rail",
            ),
        ],
    )
    facility_type.add_rail_station(
        type="non_track_tile",
        layout=[
            (
                0,
                0,
                "foundry_buildings_spritelayout_3_whole_tile",
            ),
        ],
    )
    facility_type.add_road_stop(
        type="drive_through_tile",
        layout=[
            (
                0,
                0,
                "foundry_buildings_spritelayout_1_road",
            ),
        ],
    )
    facility_type.add_road_stop(
        type="drive_through_tile",
        layout=[
            (
                0,
                0,
                "foundry_buildings_spritelayout_2_whole_tile",
            ),
        ],
    )
    facility_type.add_road_stop(
        type="drive_through_tile",
        layout=[
            (
                0,
                0,
                "foundry_buildings_spritelayout_3_road",
            ),
        ],
    )
    facility_type.add_station_object(
        layout=[
            (
                0,
                0,
                "foundry_buildings_spritelayout_1_whole_tile",
            ),
        ],
    )
    facility_type.add_station_object(
        layout=[
            (
                0,
                0,
                "foundry_buildings_spritelayout_2_whole_tile",
            ),
        ],
    )
    facility_type.add_station_object(
        layout=[
            (
                0,
                0,
                "foundry_buildings_spritelayout_3_whole_tile",
            ),
        ],
    )

    return facility_type
