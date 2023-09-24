from station import FacilityTypeTown


def main():
    facility_type = FacilityTypeTown(
        id="test",
        numeric_id=100,
    )

    facility_type.add_rail_station(type="track_tile", layout=[])
    # facility_type.add_road_stop(type="foo")
    # facility_type.add_grf_object(type="foo")

    return facility_type
