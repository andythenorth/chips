from station import FacilityTypeIndustry


def main():
    facility_type = FacilityTypeIndustry(
        id="tipple",
        numeric_id=300,
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
        rear_building_sprites=["sprite_2"],
        front_building_sprites=["sprite_1"],
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

    return facility_type
