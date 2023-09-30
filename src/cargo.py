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
            sprite = CargoSprite(
                id=cargo_label,
                graphics_file_path=graphics_file_path,
                spriteset_id=self.get_spriteset_id(cargo_label),
            )
            result.append(sprite)

        return result

    @property
    def cargo_labels(self):
        return cargo_label_mapping.keys()
