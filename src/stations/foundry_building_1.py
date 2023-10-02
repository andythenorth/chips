from station import FacilityTypeIndustry


def main(numeric_id):
    facility_type = FacilityTypeIndustry(
        id="foundry_building_1",
        numeric_id=numeric_id,
    )

    facility_type.add_sprite(
        id="sprite_building",
        x_y_loc=(10, 10),
        dimensions=(64, 145),
        offsets=(-31, -114),
    )
    facility_type.add_sprite(
        id="sprite_rear_legs",
        x_y_loc=(10, 170),
        dimensions=(64, 65),
        offsets=(-31, -34),
    )
    facility_type.add_sprite(
        id="ground_overlay",
        x_y_loc=(10, 250),
        dimensions=(64, 31),
        offsets=(-31, 0),
    )

    facility_type.add_spritelayout(
        id="foundry_building_1_spritelayout_1",
        ground_overlay_sprites=["ground_overlay"],
        rear_structure_sprites=["sprite_rear_legs"],
        main_structure_sprites=["sprite_building"],
    )

    facility_type.add_rail_station(
        type="track_tile",
        layout=[
            (
                0,
                0,
                "foundry_building_1_spritelayout_1",
            ),
        ],
    )
    facility_type.add_rail_station(
        type="non_track_tile",
        layout=[
            (
                0,
                0,
                "foundry_building_1_spritelayout_1",
            ),
        ],
    )

    return facility_type
