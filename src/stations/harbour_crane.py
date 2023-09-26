from station import FacilityTypeIndustry


def main():
    facility_type = FacilityTypeIndustry(
        id="harbour_crane",
        numeric_id=1400,
    )

    spriteset_1 = facility_type.add_spriteset(
        sprites_ne_sw=[(10, 10, 64, 145, -31, -114)],
        # sprites_nw_se are automatically interpolated in the general case
    )
    spriteset_2 = facility_type.add_spriteset(
        sprites_ne_sw=[(10, 170, 64, 65, -31, -34)],
        # sprites_nw_se are automatically interpolated in the general case
    )
    spriteset_3 = facility_type.add_spriteset(
        sprites_ne_sw=[(150, 10, 64, 145, -31, -114)],
        # sprites_nw_se are automatically interpolated in the general case
    )
    spriteset_4 = facility_type.add_spriteset(
        sprites_ne_sw=[(150, 170, 64, 65, -31, -34)],
        # sprites_nw_se are automatically interpolated in the general case
    )
    spriteset_rails = facility_type.add_spriteset(
        sprites_ne_sw=[(10, 250, 64, 39, -31, -8)],
        # sprites_nw_se are automatically interpolated in the general case
    )

    facility_type.add_spritelayout(
        id="harbour_crane_spritelayout_1",
        rear_building_sprites=[spriteset_2],
        front_building_sprites=[spriteset_1],
        fences=["nw", "ne", "se", "sw"],
    )

    facility_type.add_spritelayout(
        id="harbour_crane_spritelayout_2",
        rear_building_sprites=[spriteset_4],
        front_building_sprites=[spriteset_3],
        fences=["nw", "ne", "se", "sw"],
    )
    facility_type.add_spritelayout(
        id="harbour_crane_spritelayout_crane_rails",
        rear_building_sprites=[spriteset_rails],
        front_building_sprites=[],
        fences=["nw", "ne", "se", "sw"],
    )

    facility_type.add_rail_station(
        type="non_track_tile",
        layout=[
            (
                0,
                0,
                "harbour_crane_spritelayout_1",
            ),
        ],
    )
    facility_type.add_rail_station(
        type="non_track_tile",
        layout=[
            (
                0,
                0,
                "harbour_crane_spritelayout_2",
            ),
        ],
    )
    facility_type.add_rail_station(
        type="non_track_tile",
        layout=[
            (
                0,
                0,
                "harbour_crane_spritelayout_crane_rails",
            ),
        ],
    )
    facility_type.add_rail_station(
        type="track_tile",
        hide_pylon_tiles=True,
        hide_wire_tiles=True,
        layout=[
            (
                0,
                0,
                "harbour_crane_spritelayout_1",
            ),
        ],
    )
    facility_type.add_rail_station(
        type="track_tile",
        hide_pylon_tiles=True,
        hide_wire_tiles=True,
        layout=[
            (
                0,
                0,
                "harbour_crane_spritelayout_2",
            ),
        ],
    )
    facility_type.add_rail_station(
        type="track_tile",
        hide_pylon_tiles=True,
        hide_wire_tiles=True,
        layout=[
            (
                0,
                0,
                "harbour_crane_spritelayout_crane_rails",
            ),
        ],
    )

    return facility_type
