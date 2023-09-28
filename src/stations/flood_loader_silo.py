from station import FacilityTypeIndustry


def main():
    facility_type = FacilityTypeIndustry(
        id="flood_loader_silo",
        numeric_id=200,
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
        rear_building_sprites=["sprite_rear_legs"],
        front_building_sprites=["sprite_silo"],
        fences=["nw", "ne", "se", "sw"],
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
