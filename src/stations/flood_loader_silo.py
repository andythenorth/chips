from station import FacilityTypeIndustry


def main(numeric_id):
    facility_type = FacilityTypeIndustry(
        id="flood_loader_silo",
        numeric_id=numeric_id,
    )

    facility_type.add_sprite(
        id="sprite_silo",
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

    facility_type.add_spritelayout(
        id="flood_loader_silo_spritelayout_1",
        ground_overlay_sprites=[],
        rear_structure_sprites=["sprite_rear_legs"],
        main_structure_sprites=["sprite_silo"],
    )

    facility_type.add_rail_station(
        type="track_tile",
        hide_pylon_tiles=True,
        hide_wire_tiles=True,
        layout=[
            (
                0,
                0,
                "flood_loader_silo_spritelayout_1",
            ),
        ],
    )
    facility_type.add_rail_station(
        type="non_track_tile",
        layout=[
            (
                0,
                0,
                "flood_loader_silo_spritelayout_1",
            ),
        ],
    )

    return facility_type
