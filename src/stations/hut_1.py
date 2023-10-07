from station import FacilityTypeIndustry


def main(numeric_id):
    facility_type = FacilityTypeIndustry(
        id="hut_1",
        numeric_id=numeric_id,
    )

    facility_type.add_sprite(
        id="hut_small_wooden",
        x_y_loc=(10, 10),
        dimensions=(64, 65),
        offsets=(-31, -34),
    )
    facility_type.add_sprite(
        id="huts_grey",
        x_y_loc=(150, 10),
        dimensions=(64, 65),
        offsets=(-31, -34),
    )

    facility_type.add_spritelayout(
        id="hut_1_spritelayout_1",
        ground_overlay_sprites=[],
        rear_structure_sprites=[],
        main_structure_sprites=["hut_small_wooden"],
    )
    facility_type.add_spritelayout(
        id="hut_1_spritelayout_2",
        ground_overlay_sprites=[],
        rear_structure_sprites=[],
        main_structure_sprites=["huts_grey"],
    )

    facility_type.add_rail_station(
        type="non_track_tile",
        layout=[
            (
                0,
                0,
                "hut_1_spritelayout_1",
            ),
        ],
    )
    facility_type.add_rail_station(
        type="non_track_tile",
        layout=[
            (
                0,
                0,
                "hut_1_spritelayout_2",
            ),
        ],
    )
    facility_type.add_station_object(
        layout=[
            (
                0,
                0,
                "hut_1_spritelayout_1",
            ),
        ],
    )
    facility_type.add_station_object(
        layout=[
            (
                0,
                0,
                "hut_1_spritelayout_2",
            ),
        ],
    )

    return facility_type
