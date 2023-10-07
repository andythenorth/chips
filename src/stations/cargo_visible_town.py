from station import FacilityTypeVisibleCargo

# !!! UNFINISHED - duplicated rom cargo_industry

def main(numeric_id):
    facility_type = FacilityTypeVisibleCargo(
        id="cargo_visible_town",
        numeric_id=numeric_id,
        # FacilityTypeVisibleCargo can take arbitrary metaclass
        metaclass="town",
    )

    facility_type.add_spritelayout(
        id="cargo_visible_town_spritelayout_1",
        ground_overlay_sprites=[],
        rear_structure_sprites=[],
        main_structure_sprites=[],
    )

    facility_type.add_rail_station(
        type="track_tile",
        layout=[
            (
                0,
                0,
                "cargo_visible_town_spritelayout_1",
            ),
        ],
    )
    facility_type.add_rail_station(
        type="non_track_tile",
        layout=[
            (
                0,
                0,
                "cargo_visible_town_spritelayout_1",
            ),
        ],
    )
    facility_type.add_station_object(
        layout=[
            (
                0,
                0,
                "cargo_visible_town_spritelayout_1",
            ),
        ],
    )

    return facility_type
