import global_constants

class Station(object):
    """
        Core class, used as a container that optionally provides rail stations, road stops, objects, etc.
        Note that 'Station' in CHIPS has a different meaning to 'station' in the grf specs.
        In the grf specs, a station is always a rail station (even when it doesn't provide track).
    """

    def __init__(self, **kwargs):
        self.id = kwargs["id"]
        self.numeric_id = kwargs["numeric_id"]


class RailStation(object):

    def __init__(self, **kwargs):
        pass
        # not implemented


class RoadStop(object):

    def __init__(self, **kwargs):
        pass
        # not implemented


class GRFObject(object):
    """Stubby class to hold objects - GRFObject to avoid conflating with built-in python classname"""

    def __init__(self, **kwargs):
        pass
        # not implemented
