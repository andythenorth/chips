from station import FacilityTypeIndustry


def main(numeric_id):
    facility_type = FacilityTypeIndustry(
        id="huts",
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
        id="huts_spritelayout_small_wooden",
        ground_overlay_sprites=[],
        rear_structure_sprites=[],
        main_structure_sprites=["hut_small_wooden"],
    )
    facility_type.add_spritelayout(
        id="huts_spritelayout_huts_grey",
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
                "huts_spritelayout_small_wooden",
            ),
        ],
    )
    facility_type.add_rail_station(
        type="non_track_tile",
        layout=[
            (
                0,
                0,
                "huts_spritelayout_huts_grey",
            ),
        ],
    )
    facility_type.add_station_object(
        layout=[
            (
                0,
                0,
                "huts_spritelayout_small_wooden",
            ),
        ],
    )
    facility_type.add_station_object(
        layout=[
            (
                0,
                0,
                "huts_spritelayout_huts_grey",
            ),
        ],
    )

    return facility_type
