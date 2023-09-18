import os

currentdir = os.curdir

import global_constants
import utils

# setting up a cache for compiled chameleon templates can significantly speed up template rendering
chameleon_cache_path = os.path.join(currentdir, global_constants.chameleon_cache_dir)
if not os.path.exists(chameleon_cache_path):
    os.mkdir(chameleon_cache_path)
os.environ["CHAMELEON_CACHE"] = chameleon_cache_path

generated_files_path = os.path.join(currentdir, global_constants.generated_files_dir)
if not os.path.exists(generated_files_path):
    os.mkdir(generated_files_path)

"""
import tiles
registered_tiles = tiles.registered_tiles
"""


class StationManager(list):
    """
    It's convenient to have a structure for working with stations.
    This is a class to manage that, intended for use as a singleton, which can be passed to templates etc.
    Extends default python list, as it's a convenient behaviour (the instantiated class instance behaves like a list object).
    """

    def add_station(self, station_module):
        station = station_module.main()
        self.append(station)


from stations import test

# declared outside of main, got bored trying to figure out how to otherwise put it in the module scope
station_manager = StationManager()


def main():
    station_manager.add_station(test)
