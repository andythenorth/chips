# 'tiles' is a bit of a throwaway term, these aren't station tiles, they're configurations of spritesets

from spriteset import CargoSprite

# cargo label -> filename mapping
# keep alphabetised by cargo label
# this might need further structure in future if we want cargo sprite randomisation or animation
cargo_label_mapping = {
    "CLAY": "clay_cargo",
    "COAL": "coal_cargo",
}


#class CargoManager():

def get_spriteset_ids():
    result = []
    for cargo_label in cargo_label_mapping.keys():
        result.append("spriteset_cargo_" + cargo_label)
    return result


def get_sprites():
    # returns a simple list sprites
    result = []
    for cargo_label, filename in cargo_label_mapping.items():
        graphics_file_path = "src/graphics/" + filename + ".png"
        sprite = CargoSprite(
            id=cargo_label,
            graphics_file_path=graphics_file_path,
            spriteset_id="spriteset_cargo_" + cargo_label,
        )
        result.append(sprite)

    return result


def main():
    # nothing, just here for consistency of module interfaces
    pass
