from facility import FacilityTypeTown


def main():
    facility_type = FacilityTypeTown(
        id="test",
        numeric_id=1,
    )
    """
    consist = DumpCarAggregateConsist(
        roster_id="pony",
        base_numeric_id=14730,
        gen=1,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_gapped_16px")
    """

    return facility_type
