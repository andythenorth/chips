from station import FacilityTypeTown


def main():
    facility_type = FacilityTypeTown(
        id="parcels_office",
        numeric_id=1000,
    )

    spriteset_1 = facility_type.add_spriteset(
        sprites_ne_sw=[(10, 10, 64, 65, -31, -34)],
        # sprites_nw_se are automatically interpolated in the general case
    )

    facility_type.add_spritelayout(
        id="parcels_office_spritelayout_1",
        rear_building_sprites=[],
        front_building_sprites=[spriteset_1],
        fences=["nw", "ne", "se", "sw"],
    )

    facility_type.add_rail_station(
        type="non_track_tile",
        layout=[
            (
                0,
                0,
                "parcels_office_spritelayout_1",
            ),
        ],
    )

    return facility_type
