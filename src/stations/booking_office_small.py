from station import FacilityTypeTown


def main():
    facility_type = FacilityTypeTown(
        id="booking_office_small",
        numeric_id=800,
    )

    facility_type.add_sprite(
        id="sprite_1",
        x_y_loc=(10, 10),
        dimensions=(64, 65),
        offsets=(-31, -34),
        auto_extend_orientation=True,
    )

    facility_type.add_spritelayout(
        id="booking_office_small_spritelayout_1",
        rear_building_sprites=[],
        front_building_sprites=["sprite_1"],
        fences=["nw", "ne", "se", "sw"],
    )

    facility_type.add_rail_station(
        type="non_track_tile",
        layout=[
            (
                0,
                0,
                "booking_office_small_spritelayout_1",
            ),
        ],
    )

    return facility_type
