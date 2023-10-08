from station import FacilityTypeFreight


def main():
    facility_type = FacilityTypeFreight(
        id="cement_silo",
    )

    facility_type.add_sprite(
        id="cement_silo_upper_rail",
        x_y_loc=(10, 10),
        dimensions=(64, 145),
        offsets=(-31, -114),
    )
    facility_type.add_sprite(
        id="sprite_silo_base_rail_front",
        x_y_loc=(10, 170),
        dimensions=(64, 65),
        offsets=(-31, -34),
    )
    facility_type.add_sprite(
        id="sprite_silo_base_rail_rear",
        x_y_loc=(10, 250),
        dimensions=(64, 65),
        offsets=(-31, -34),
    )
    facility_type.add_sprite(
        id="sprite_silo_pre_composed",
        x_y_loc=(150, 10),
        dimensions=(64, 145),
        offsets=(-31, -114),
    )
    facility_type.add_sprite(
        id="cement_silo_upper_road",
        x_y_loc=(290, 10),
        dimensions=(64, 145),
        offsets=(-31, -114),
    )
    facility_type.add_sprite(
        id="sprite_silo_base_road_front",
        x_y_loc=(290, 170),
        dimensions=(64, 65),
        offsets=(-31, -34),
    )
    facility_type.add_sprite(
        id="sprite_silo_base_road_middle",
        x_y_loc=(290, 330),
        dimensions=(64, 65),
        offsets=(-31, -34),
    )
    facility_type.add_sprite(
        id="sprite_silo_base_road_rear",
        x_y_loc=(290, 250),
        dimensions=(64, 65),
        offsets=(-31, -34),
    )

    facility_type.add_spritelayout(
        id="cement_silo_spritelayout_1",
        ground_overlay_sprites=[],
        rear_structure_sprites=["sprite_silo_base_rail_rear"],
        main_structure_sprites=["sprite_silo_base_rail_front", "cement_silo_upper_rail"],
    )
    facility_type.add_spritelayout(
        id="cement_silo_spritelayout_2",
        ground_overlay_sprites=[],
        rear_structure_sprites=[],
        main_structure_sprites=["sprite_silo_pre_composed"],
    )
    facility_type.add_spritelayout(
        id="cement_silo_spritelayout_3",
        ground_overlay_sprites=[],
        rear_structure_sprites=["sprite_silo_base_road_rear"],
        middle_structure_sprites=["sprite_silo_base_road_middle"],
        main_structure_sprites=["sprite_silo_base_road_front", "cement_silo_upper_road"],
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
                "cement_silo_spritelayout_2",
            ),
        ],
    )

    facility_type.add_road_stop(
        type="drive_through_tile",
        layout=[
            (
                0,
                0,
                "cement_silo_spritelayout_3",
            ),
        ],
    )
    facility_type.add_station_object(
        layout=[
            (
                0,
                0,
                "cement_silo_spritelayout_2",
            ),
        ],
    )

    return facility_type
