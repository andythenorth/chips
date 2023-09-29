from station import FacilityTypeIndustry


def main():
    facility_type = FacilityTypeIndustry(
        id="mine_building_large",
        numeric_id=500,
    )

    facility_type.add_sprite(
        id="sprite_1",
        x_y_loc=(10, 10),
        dimensions=(64, 65),
        offsets=(-31, -34),
    )

    facility_type.add_spritelayout(
        id="mine_building_large_spritelayout_1",
        ground_overlay_sprites=[],
        rear_building_sprites=[],
        front_building_sprites=["sprite_1"],
    )

    facility_type.add_rail_station(
        type="non_track_tile",
        layout=[
            (
                0,
                0,
                "mine_building_large_spritelayout_1",
            ),
        ],
    )

    return facility_type
