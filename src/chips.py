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


class FacilityTypeManager(list):
    """
    It's convenient to have a structure for working with facility types.
    This is a class to manage that, intended for use as a singleton, which can be passed to templates etc.
    Extends default python list, as it's a convenient behaviour (the instantiated class instance behaves like a list object).
    """

    def add_facility_type(self, facility_type_module):
        facility_type = facility_type_module.main()
        self.append(facility_type)


from stations import booking_office
from stations import booking_office_small
from stations import dispatchers_office
from stations import flood_loader_silo
from stations import hotel
from stations import mine_building_large
from stations import mine_building_small
from stations import parcels_office
from stations import test
from stations import tipple

# declared outside of main, got bored trying to figure out how to otherwise put it in the module scope
facility_type_manager = FacilityTypeManager()


def main():
    facility_type_manager.add_facility_type(booking_office)
    facility_type_manager.add_facility_type(booking_office_small)
    facility_type_manager.add_facility_type(dispatchers_office)
    facility_type_manager.add_facility_type(flood_loader_silo)
    facility_type_manager.add_facility_type(hotel)
    facility_type_manager.add_facility_type(mine_building_large)
    facility_type_manager.add_facility_type(mine_building_small)
    facility_type_manager.add_facility_type(parcels_office)
    facility_type_manager.add_facility_type(test)
    facility_type_manager.add_facility_type(tipple)

