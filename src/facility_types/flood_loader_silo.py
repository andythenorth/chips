from facility import FacilityTypeIndustry


def main():
    facility_type = FacilityTypeIndustry(
        id="flood_loader_silo",
        numeric_id=2,
    )

    spriteset_ground = facility_type.add_spriteset(
        type="dirty_concrete",
    )
    spriteset_ground_overlay = facility_type.add_spriteset(type="empty")
    spriteset_1 = facility_type.add_spriteset(
        sprites=[(10, 10, 64, 80, -31, -49)],
    )

    facility_type.add_spritelayout(
        id="flood_loader_silo_spritelayout_1",
        ground_sprite=spriteset_ground,
        ground_overlay=spriteset_ground_overlay,
        building_sprites=[spriteset_1],
        fences=["nw", "ne", "se", "sw"],
    )

    facility_type.add_spritelayout(
        id="flood_loader_silo_spritelayout_2",
        ground_sprite=spriteset_ground,
        ground_overlay=spriteset_ground_overlay,
        building_sprites=[spriteset_1],
        fences=["nw", "ne", "se", "sw"],
    )

    return facility_type
