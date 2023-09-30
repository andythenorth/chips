from station import FacilityTypeTown


def main():
    facility_type = FacilityTypeTown(
        id="warehouses_1",
        numeric_id=1800,
    )

    facility_type.add_sprite(
        id="sprite_1",
        x_y_loc=(10, 10),
        dimensions=(64, 65),
        offsets=(-31, -34),
    )

    facility_type.add_spritelayout(
        id="warehouses_1_spritelayout_1",
        ground_overlay_sprites=[],
        rear_structure_sprites=[],
        main_structure_sprites=["sprite_1"],
    )

    facility_type.add_rail_station(
        type="non_track_tile",
        layout=[
            (
                0,
                0,
                "warehouses_1_spritelayout_1",
            ),
        ],
    )

    return facility_type
