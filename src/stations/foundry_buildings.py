from station import FacilityTypeIndustry


def main(numeric_id):
    facility_type = FacilityTypeIndustry(
        id="foundry_buildings",
        numeric_id=numeric_id,
    )

    facility_type.add_sprite(
        id="ground_overlay_platforms",
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
        id="sprite_rear_legs_large",
        x_y_loc=(10, 170),
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
        id="sprite_rear_legs_small",
        x_y_loc=(150, 170),
        dimensions=(64, 65),
        offsets=(-31, -34),
    )

    facility_type.add_spritelayout(
        id="foundry_buildings_spritelayout_1_track",
        ground_overlay_sprites=["ground_overlay_platforms"],
        rear_structure_sprites=["sprite_rear_legs_large"],
        main_structure_sprites=["sprite_building_large"],
    )
    facility_type.add_spritelayout(
        id="foundry_buildings_spritelayout_1_non_track",
        ground_overlay_sprites=["ground_overlay_whole_tile"],
        rear_structure_sprites=["sprite_rear_legs_large"],
        main_structure_sprites=["sprite_building_large"],
    )
    facility_type.add_spritelayout(
        id="foundry_buildings_spritelayout_2_track",
        ground_overlay_sprites=["ground_overlay_platforms"],
        rear_structure_sprites=["sprite_rear_legs_small"],
        main_structure_sprites=["sprite_building_small"],
    )
    facility_type.add_spritelayout(
        id="foundry_buildings_spritelayout_2_non_track",
        ground_overlay_sprites=["ground_overlay_whole_tile"],
        rear_structure_sprites=["sprite_rear_legs_small"],
        main_structure_sprites=["sprite_building_small"],
    )

    facility_type.add_rail_station(
        type="track_tile",
        layout=[
            (
                0,
                0,
                "foundry_buildings_spritelayout_1_track",
            ),
        ],
    )
    facility_type.add_rail_station(
        type="non_track_tile",
        layout=[
            (
                0,
                0,
                "foundry_buildings_spritelayout_1_non_track",
            ),
        ],
    )
    facility_type.add_rail_station(
        type="track_tile",
        layout=[
            (
                0,
                0,
                "foundry_buildings_spritelayout_2_track",
            ),
        ],
    )
    facility_type.add_rail_station(
        type="non_track_tile",
        layout=[
            (
                0,
                0,
                "foundry_buildings_spritelayout_2_non_track",
            ),
        ],
    )
    facility_type.add_station_object(
        layout=[
            (
                0,
                0,
                "foundry_buildings_spritelayout_1_non_track",
            ),
        ],
    )
    facility_type.add_road_stop(
        type="drive_through_tile",
        layout=[
            (
                0,
                0,
                "foundry_buildings_spritelayout_1_non_track",
            ),
        ],
    )
    facility_type.add_road_stop(
        type="drive_through_tile",
        layout=[
            (
                0,
                0,
                "foundry_buildings_spritelayout_2_non_track",
            ),
        ],
    )
    facility_type.add_station_object(
        layout=[
            (
                0,
                0,
                "foundry_buildings_spritelayout_2_non_track",
            ),
        ],
    )

    return facility_type
