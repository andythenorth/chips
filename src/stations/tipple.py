from station import FacilityTypeIndustry


def main(numeric_id):
    facility_type = FacilityTypeIndustry(
        id="tipple",
        numeric_id=numeric_id,
    )

    facility_type.add_sprite(
        id="sprite_1",
        x_y_loc=(10, 10),
        dimensions=(64, 65),
        offsets=(-31, -34),
    )
    facility_type.add_sprite(
        id="sprite_2",
        x_y_loc=(10, 90),
        dimensions=(64, 65),
        offsets=(-31, -34),
    )

    facility_type.add_spritelayout(
        id="tipple_spritelayout_1",
        ground_overlay_sprites=[],
        rear_structure_sprites=["sprite_2"],
        main_structure_sprites=["sprite_1"],
    )

    facility_type.add_rail_station(
        type="track_tile",
        hide_pylon_tiles=True,
        hide_wire_tiles=True,
        layout=[
            (
                0,
                0,
                "tipple_spritelayout_1",
            ),
        ],
    )
    facility_type.add_rail_station(
        type="non_track_tile",
        layout=[
            (
                0,
                0,
                "tipple_spritelayout_1",
            ),
        ],
    )
    facility_type.add_road_stop(
        type="drive_through_tile",
        layout=[
            (
                0,
                0,
                "tipple_spritelayout_1",
            ),
        ],
    )
    facility_type.add_station_object(
        layout=[
            (
                0,
                0,
                "tipple_spritelayout_1",
            ),
        ],
    )

    return facility_type
