import global_constants
from sprite import CargoSprite

# cargo label -> filename mapping
# keep alphabetised by cargo label
# this might need further structure in future if we want cargo sprite randomisation or animation
# !! CABBAGE we might want to map multiple labels to a single cargo spritesheet; that might need extra work to prevent duplicate spritesets
# !! also should this be handled via Polar Fox?  I haven't seen any case for that so far.
cargo_label_mapping = {
    "CLAY": "clay_cargo",
    "COAL": "coal_cargo",
    "TYRE": "tyres_cargo",
    "VEHI": "vehicles_cargo",
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
    def get_spriteset_id(self, cargo_label):
        return "spriteset_cargo_" + cargo_label

    @property
    def spriteset_ids(self):
        result = []
        for cargo_label in cargo_label_mapping.keys():
            result.append(self.get_spriteset_id(cargo_label))
        return result

    @property
    def sprites(self):
        # returns a simple list of sprites
        result = []
        for cargo_label, filename in cargo_label_mapping.items():
            graphics_file_path = "src/graphics/" + filename + ".png"
            for spriteset_label, x_y_loc in cargo_spriteset_format.items():
                offset_adjustment = self.get_offset_adjustment(spriteset_label)
                sprite = CargoSprite(
                    id=spriteset_label,
                    x_loc=x_y_loc[0],
                    y_loc=x_y_loc[1],
                    x_offset_adjustment=offset_adjustment[0],
                    y_offset_adjustment=offset_adjustment[1],
                    graphics_file_path=graphics_file_path,
                    spriteset_id=self.get_spriteset_id(cargo_label),
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

