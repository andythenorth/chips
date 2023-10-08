from station import FacilityTypeTown


def main():
    facility_type = FacilityTypeTown(
        id="warehouse_town",
    )

    facility_type.add_sprite(
        id="sprite_1",
        x_y_loc=(10, 10),
        dimensions=(64, 65),
        offsets=(-31, -34),
    )

    facility_type.add_spritelayout(
        id="warehouse_town_spritelayout_1",
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
                "warehouse_town_spritelayout_1",
            ),
        ],
    )
    facility_type.add_station_object(
        layout=[
            (
                0,
                0,
                "warehouse_town_spritelayout_1",
            ),
        ],
    )

    return facility_type
