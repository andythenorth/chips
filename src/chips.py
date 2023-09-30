import os

currentdir = os.curdir

import global_constants
import utils

from spriteset import Spriteset, GroundSprite

generated_files_path = os.path.join(currentdir, global_constants.generated_files_dir)
if not os.path.exists(generated_files_path):
    os.mkdir(generated_files_path)

import cargo
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


class SpriteManager(dict):
    """
    CHIPS zips sprites into a limited number of global spritesets.
    This is because station spritelayouts have a limit of 6 spritesets due to size of var 0x10.
    This is a class to manage sprites and spritesets, intended for use as a singleton, which can be passed to templates etc.
    Extends default python dict, as it's a convenient behaviour (the instantiated class instance behaves like a dict object).
    """

    def add_spriteset(self, spriteset_id):
        self[spriteset_id] = Spriteset(id=spriteset_id)

    def add_spritesets_from_id_list(self, spriteset_ids):
        # convience function, can add a list of spritesets by id, wraps add_spriteset
        for spriteset_id in spriteset_ids:
            self.add_spriteset(spriteset_id)

    def add_sprite(self, sprite):
        if (
            self[sprite.spriteset_id].get_sprite_by_id(sprite.id, allow_not_found=True)
            is not None
        ):
            raise BaseException(
                "sprite with id "
                + sprite.id
                + " already exists in spriteset "
                + spriteset_id
            )
        self[sprite.spriteset_id].append(sprite)

    def add_sprites_from_list(self, sprites):
        # convience function, can add a list of sprites, wraps add_sprite
        for sprite in sprites:
            self.add_sprite(sprite)


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
sprite_manager = SpriteManager()
facility_type_manager = FacilityTypeManager()


def main():
    sprite_manager.add_spritesets_from_id_list(cargo.get_spriteset_ids())
    sprite_manager.add_sprites_from_list(cargo.get_sprites())

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
