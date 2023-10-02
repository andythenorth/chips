from station import FacilityTypeIndustry


def main(numeric_id):
    facility_type = FacilityTypeIndustry(
        id="mine_building_1",
        numeric_id=numeric_id,
    )

    facility_type.add_sprite(
        id="building_large",
        x_y_loc=(10, 10),
        dimensions=(64, 65),
        offsets=(-31, -34),
    )
    facility_type.add_sprite(
        id="building_small",
        x_y_loc=(150, 10),
        dimensions=(64, 65),
        offsets=(-31, -34),
    )

    facility_type.add_spritelayout(
        id="mine_building_1_spritelayout_1",
        ground_overlay_sprites=[],
        rear_structure_sprites=[],
        main_structure_sprites=["building_small"],
    )
    facility_type.add_spritelayout(
        id="mine_building_1_spritelayout_2",
        ground_overlay_sprites=[],
        rear_structure_sprites=[],
        main_structure_sprites=["building_large"],
    )

    facility_type.add_rail_station(
        type="non_track_tile",
        layout=[
            (
                0,
                0,
                "mine_building_1_spritelayout_1",
            ),
        ],
    )
    facility_type.add_rail_station(
        type="non_track_tile",
        layout=[
            (
                0,
                0,
                "mine_building_1_spritelayout_2",
            ),
        ],
    )

    return facility_type
