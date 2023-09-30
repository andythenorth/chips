import os

currentdir = os.curdir

import global_constants
import utils

generated_files_path = os.path.join(currentdir, global_constants.generated_files_dir)
if not os.path.exists(generated_files_path):
    os.mkdir(generated_files_path)

from cargo import CargoManager
from sprite import SpriteManager

import ground

from stations import booking_office
from stations import booking_office_small
from stations import cargo_visible_industry
from stations import dispatchers_office
from stations import flood_loader_silo
from stations import harbour_crane
from stations import hotel
from stations import hut_1
from stations import hut_2
from stations import mine_building_large
from stations import mine_building_small
from stations import parcels_office
from stations import tipple


class FacilityTypeManager(list):
    """
    It's convenient to have a structure for working with facility types.
    This is a class to manage that, intended for use as a singleton, which can be passed to templates etc.
    Extends default python list, as it's a convenient behaviour (the instantiated class instance behaves like a list object).
    """

    def add_facility_type(self, facility_type_module):
        facility_type = facility_type_module.main()
        self.append(facility_type)

# declared outside of main, got bored trying to figure out how to otherwise put these in the module scope
cargo_manager = CargoManager()
facility_type_manager = FacilityTypeManager()
sprite_manager = SpriteManager()

def main():
    sprite_manager.add_spritesets_from_id_list(cargo_manager.spriteset_ids)
    sprite_manager.add_sprites_from_list(cargo_manager.sprites)

    sprite_manager.add_spriteset("spriteset_ground")
    sprite_manager.add_sprites_from_list(ground.get_sprites())

    facility_type_manager.add_facility_type(booking_office)
    facility_type_manager.add_facility_type(booking_office_small)
    facility_type_manager.add_facility_type(cargo_visible_industry)
    facility_type_manager.add_facility_type(dispatchers_office)
    facility_type_manager.add_facility_type(flood_loader_silo)
    facility_type_manager.add_facility_type(harbour_crane)
    facility_type_manager.add_facility_type(hotel)
    facility_type_manager.add_facility_type(hut_1)
    facility_type_manager.add_facility_type(hut_2)
    facility_type_manager.add_facility_type(mine_building_large)
    facility_type_manager.add_facility_type(mine_building_small)
    facility_type_manager.add_facility_type(parcels_office)
    facility_type_manager.add_facility_type(tipple)
