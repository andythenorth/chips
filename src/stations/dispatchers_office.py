from station import FacilityTypeTown


def main():
    facility_type = FacilityTypeTown(
        id="dispatchers_office",
        numeric_id=900,
    )

    facility_type.add_sprite(
        id="sprite_1",
        x_y_loc=(10, 10),
        dimensions=(64, 65),
        offsets=(-31, -34),
        auto_extend_orientation=True,
    )

    facility_type.add_spritelayout(
        id="dispatchers_office_spritelayout_1",
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
                "dispatchers_office_spritelayout_1",
            ),
        ],
    )

    return facility_type
