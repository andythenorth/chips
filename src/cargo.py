import global_constants
from sprite import CargoSprite

# cargo label -> cargo_filename mapping
# keep alphabetised by cargo label
# this might need further structure in future if we want cargo sprite randomisation or animation
# !! CABBAGE we might want to map multiple labels to a single cargo spritesheet; that might need extra work to prevent duplicate spritesets
# !! also should this be handled via Polar Fox?  I haven't seen any case for that so far.
cargo_label_mapping = {
    "NULL": "empty_cargo", # for empty cargo sprites; assumes no-one defines a real cargo with label NULL, but eh, probably fine?
    "CLAY": "clay_cargo",
    "COAL": "coal_cargo",
    "IRON": "metal_mixed_cargo",
    "METL": "metal_mixed_cargo",
    "NICK": "metal_mixed_cargo",
    "SCMT": "scrap_metal_cargo",
    "STEL": "metal_mixed_cargo",
    "TYRE": "tyres_cargo",
    "VEHI": "vehicles_cargo",
    "WDPR": "lumber_cargo",
    "WOOD": "wood_cargo",
    "ZINC": "metal_mixed_cargo",
}

# spriteset_label, (x_loc, y_loc)
cargo_spriteset_format = {
    "whole_tile_ne_sw": (10, 10),
    "rear_platform_ne_sw": (10, 90),
    "front_platform_ne_sw": (10, 170),
    "whole_tile_nw_se": (150, 10),
    "rear_platform_nw_se": (150, 90),
    "front_platform_nw_se": (150, 170),
}

class CargoManager:
    def get_spriteset_id(self, cargo_filename):
        return "spriteset_cargo_" + cargo_filename

    def get_spriteset_id_by_cargo_label(self, cargo_label):
        return self.get_spriteset_id(cargo_label_mapping[cargo_label])

    @property
    def spriteset_ids(self):
        result = []
        for cargo_filename in set(cargo_label_mapping.values()):
            result.append(self.get_spriteset_id(cargo_filename))
        print(result)
        return result

    @property
    def sprites(self):
        # returns a simple list of sprites
        result = []
        for cargo_filename in set(cargo_label_mapping.values()):
            graphics_file_path = "src/graphics/" + cargo_filename + ".png"
            for spriteset_label, x_y_loc in cargo_spriteset_format.items():
                offset_adjustment = self.get_offset_adjustment(spriteset_label)
                sprite = CargoSprite(
                    id=spriteset_label,
                    x_loc=x_y_loc[0],
                    y_loc=x_y_loc[1],
                    x_offset_adjustment=offset_adjustment[0],
                    y_offset_adjustment=offset_adjustment[1],
                    graphics_file_path=graphics_file_path,
                    spriteset_id=self.get_spriteset_id(cargo_filename),
                )
                result.append(sprite)

        return result

    @property
    def cargo_labels(self):
        return cargo_label_mapping.keys()

    def get_offset_adjustment(self, spriteset_label):
        # automatic offset adjustment from frosch, returns a 2-tuple (x, y) of adjustments for sprites when bounding boxes aren't located at 0, 0
        # !! CABBAGE - possibly should be moved to sprite.py - isn't specific to cargo, may be needed with other sprites also
        bb_x_offset = global_constants.rail_station_bounding_boxes[spriteset_label]["x_offset"]
        bb_y_offset = global_constants.rail_station_bounding_boxes[spriteset_label]["y_offset"]
        return (2 * (bb_y_offset - bb_x_offset), bb_x_offset + bb_y_offset)

