from station import FacilityTypeIndustry


def main():
    facility_type = FacilityTypeIndustry(
        id="flood_loader_silo",
        numeric_id=200,
    )

    spriteset_ground = facility_type.add_spriteset(
        type="dirty_concrete",
    )
    spriteset_ground_overlay = facility_type.add_spriteset(type="empty")
    spriteset_1 = facility_type.add_spriteset(
        sprites_ne_sw=[(10, 10, 64, 145, -31, -114)],
        # sprites_nw_se are automatically interpolated in the general case
    )
    spriteset_2 = facility_type.add_spriteset(
        sprites_ne_sw=[(10, 170, 64, 65, -31, -34)],
        # sprites_nw_se are automatically interpolated in the general case
    )

    facility_type.add_spritelayout(
        id="flood_loader_silo_spritelayout_1",
        ground_sprite=spriteset_ground,
        ground_overlay=spriteset_ground_overlay,
        building_sprites=[spriteset_2, spriteset_1],
        fences=["nw", "ne", "se", "sw"],
    )

    facility_type.add_rail_station(
        type="track_tile",
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
