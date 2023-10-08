from station import FacilityTypeIndustry


def main():
    facility_type = FacilityTypeIndustry(
        id="harbour_crane",
    )

    facility_type.add_sprite(
        id="sprite_1",
        x_y_loc=(10, 10),
        dimensions=(64, 145),
        offsets=(-31, -114),
    )
    facility_type.add_sprite(
        id="sprite_2",
        x_y_loc=(10, 170),
        dimensions=(64, 65),
        offsets=(-31, -34),
    )
    facility_type.add_sprite(
        id="sprite_3",
        x_y_loc=(150, 10),
        dimensions=(64, 145),
        offsets=(-31, -114),
    )
    facility_type.add_sprite(
        id="sprite_4",
        x_y_loc=(150, 170),
        dimensions=(64, 65),
        offsets=(-31, -34),
    )
    facility_type.add_sprite(
        id="sprite_rails_for_track_tile",
        x_y_loc=(10, 250),
        dimensions=(64, 39),
        offsets=(-31, -8),
    )
    facility_type.add_sprite(
        id="sprite_rails_for_non_track_tile",
        x_y_loc=(10, 250),
        dimensions=(64, 39),
        offsets=(-31, -8),
    )

    facility_type.add_spritelayout(
        id="harbour_crane_spritelayout_1_track",
        ground_overlay_sprites=["sprite_rails_for_track_tile"],
        rear_structure_sprites=["sprite_2"],
        main_structure_sprites=["sprite_1"],
    )
    facility_type.add_spritelayout(
        id="harbour_crane_spritelayout_2_track",
        ground_overlay_sprites=["sprite_rails_for_track_tile"],
        rear_structure_sprites=["sprite_4"],
        main_structure_sprites=["sprite_3"],
    )
    facility_type.add_spritelayout(
        id="harbour_crane_spritelayout_1_non_track",
        ground_overlay_sprites=["sprite_rails_for_non_track_tile"],
        rear_structure_sprites=["sprite_2"],
        main_structure_sprites=["sprite_1"],
    )
    facility_type.add_spritelayout(
        id="harbour_crane_spritelayout_2_non_track",
        ground_overlay_sprites=["sprite_rails_for_non_track_tile"],
        rear_structure_sprites=["sprite_4"],
        main_structure_sprites=["sprite_3"],
    )
    facility_type.add_spritelayout(
        id="harbour_crane_spritelayout_crane_rails_track",
        ground_overlay_sprites=["sprite_rails_for_track_tile"],
        rear_structure_sprites=[],
        main_structure_sprites=[],
    )
    facility_type.add_spritelayout(
        id="harbour_crane_spritelayout_crane_rails_non_track",
        ground_overlay_sprites=["sprite_rails_for_non_track_tile"],
        rear_structure_sprites=[],
        main_structure_sprites=[],
    )

    facility_type.add_rail_station(
        type="non_track_tile",
        layout=[
            (
                0,
                0,
                "harbour_crane_spritelayout_1_non_track",
            ),
        ],
    )
    facility_type.add_rail_station(
        type="non_track_tile",
        layout=[
            (
                0,
                0,
                "harbour_crane_spritelayout_2_non_track",
            ),
        ],
    )
    facility_type.add_rail_station(
        type="non_track_tile",
        layout=[
            (
                0,
                0,
                "harbour_crane_spritelayout_crane_rails_non_track",
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
                "harbour_crane_spritelayout_1_track",
            ),
            (
                1,
                0,
                "harbour_crane_spritelayout_crane_rails_track",
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
                "harbour_crane_spritelayout_2_track",
            ),
            (
                0,
                1,
                "harbour_crane_spritelayout_crane_rails_track",
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
                "harbour_crane_spritelayout_crane_rails_track",
            ),
        ],
    )

    facility_type.add_station_object(
        layout=[
            (
                0,
                0,
                "harbour_crane_spritelayout_1_track",
            ),
        ],
    )
    facility_type.add_station_object(
        layout=[
            (
                0,
                0,
                "harbour_crane_spritelayout_2_track",
            ),
        ],
    )
    facility_type.add_station_object(
        layout=[
            (
                0,
                0,
                "harbour_crane_spritelayout_crane_rails_track",
            ),
        ],
    )

    return facility_type
