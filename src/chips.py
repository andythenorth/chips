import os

currentdir = os.curdir

import global_constants
import ground_tiles
import utils

from spriteset import Spriteset, GroundTileSprite

# setting up a cache for compiled chameleon templates can significantly speed up template rendering
chameleon_cache_path = os.path.join(currentdir, global_constants.chameleon_cache_dir)
if not os.path.exists(chameleon_cache_path):
    os.mkdir(chameleon_cache_path)
os.environ["CHAMELEON_CACHE"] = chameleon_cache_path

generated_files_path = os.path.join(currentdir, global_constants.generated_files_dir)
if not os.path.exists(generated_files_path):
    os.mkdir(generated_files_path)


class SpriteManager(dict):
    """
    CHIPS zips sprites into a limited number of global spritesets.
    This is because station spritelayouts have a limit of 6 spritesets due to size of var 0x10.
    This is a class to manage sprites and spritesets, intended for use as a singleton, which can be passed to templates etc.
    Extends default python dict, as it's a convenient behaviour (the instantiated class instance behaves like a dict object).
    """

    def add_spriteset(self, spriteset_id):
        self[spriteset_id] = Spriteset(id=spriteset_id)

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


from stations import booking_office
from stations import booking_office_small
from stations import dispatchers_office
from stations import flood_loader_silo
from stations import harbour_crane
from stations import hotel
from stations import hut_1
from stations import hut_2
from stations import mine_building_large
from stations import mine_building_small
from stations import parcels_office

# from stations import test
from stations import tipple

# declared outside of main, got bored trying to figure out how to otherwise put these in the module scope
sprite_manager = SpriteManager()
facility_type_manager = FacilityTypeManager()


def main():
    sprite_manager.add_spriteset("spriteset_ground_tiles")
    sprite_manager.add_sprites_from_list(ground_tiles.get_sprites())

    facility_type_manager.add_facility_type(booking_office)
    facility_type_manager.add_facility_type(booking_office_small)
    facility_type_manager.add_facility_type(dispatchers_office)
    facility_type_manager.add_facility_type(flood_loader_silo)
    facility_type_manager.add_facility_type(harbour_crane)
    facility_type_manager.add_facility_type(hotel)
    facility_type_manager.add_facility_type(hut_1)
    facility_type_manager.add_facility_type(hut_2)
    facility_type_manager.add_facility_type(mine_building_large)
    facility_type_manager.add_facility_type(mine_building_small)
    facility_type_manager.add_facility_type(parcels_office)
    # facility_type_manager.add_facility_type(test)
    facility_type_manager.add_facility_type(tipple)
