from station import FacilityTypeFreight


def main():
    facility_type = FacilityTypeFreight(
        id="mine_buildings",
    )

    facility_type.add_sprite(
        id="building_large",
        x_y_loc=(10, 10),
        dimensions=(64, 65),
        offsets=(-31, -34),
    )
    facility_type.add_sprite(
        id="building_small",
        x_y_loc=(150, 10),
        dimensions=(64, 65),
        offsets=(-31, -34),
    )

    facility_type.add_spritelayout(
        id="mine_buildings_spritelayout_building_small",
        ground_overlay_sprites=[],
        rear_structure_sprites=[],
        main_structure_sprites=["building_small"],
    )
    facility_type.add_spritelayout(
        id="mine_buildings_spritelayout_building_large",
        ground_overlay_sprites=[],
        rear_structure_sprites=[],
        main_structure_sprites=["building_large"],
    )

    facility_type.add_rail_station(
        type="non_track_tile",
        layout=[
            (
                0,
                0,
                "mine_buildings_spritelayout_building_small",
            ),
        ],
    )
    facility_type.add_rail_station(
        type="non_track_tile",
        layout=[
            (
                0,
                0,
                "mine_buildings_spritelayout_building_large",
            ),
        ],
    )
    facility_type.add_station_object(
        layout=[
            (
                0,
                0,
                "mine_buildings_spritelayout_building_small",
            ),
        ],
    )
    facility_type.add_station_object(
        layout=[
            (
                0,
                0,
                "mine_buildings_spritelayout_building_large",
            ),
        ],
    )

    return facility_type
