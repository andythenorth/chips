from station import FacilityTypeIndustry


def main(numeric_id):
    facility_type = FacilityTypeIndustry(
        id="cement_silo",
        numeric_id=numeric_id,
    )

    facility_type.add_sprite(
        id="sprite_silo",
        x_y_loc=(10, 10),
        dimensions=(64, 145),
        offsets=(-31, -114),
    )
    facility_type.add_sprite(
        id="sprite_silo_base_front",
        x_y_loc=(10, 170),
        dimensions=(64, 65),
        offsets=(-31, -34),
    )
    facility_type.add_sprite(
        id="sprite_silo_base_rear",
        x_y_loc=(10, 250),
        dimensions=(64, 65),
        offsets=(-31, -34),
    )

    facility_type.add_spritelayout(
        id="cement_silo_spritelayout_1",
        ground_overlay_sprites=[],
        rear_structure_sprites=["sprite_silo_base_rear"],
        main_structure_sprites=["sprite_silo_base_front", "sprite_silo"],
    )

    facility_type.add_rail_station(
        type="track_tile",
        hide_pylon_tiles=True,
        hide_wire_tiles=True,
        layout=[
            (
                0,
                0,
                "cement_silo_spritelayout_1",
            ),
        ],
    )
    facility_type.add_rail_station(
        type="non_track_tile",
        layout=[
            (
                0,
                0,
                "cement_silo_spritelayout_1",
            ),
        ],
    )

    return facility_type
