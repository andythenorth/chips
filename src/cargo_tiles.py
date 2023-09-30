# 'tiles' is a bit of a throwaway term, these aren't station tiles, they're configurations of spritesets

from spriteset import CargoTileSprite

# cargo label -> filename mapping
# keep alphabetised by cargo label
# this might need further structure in future if we want cargo sprite randomisation or animation
cargo_label_mapping = {
    "CLAY": "clay_cargo",
    "COAL": "coal_cargo",
}

def get_sprites():
    # returns a simple list sprites
    result = []
    for cargo_label, filename in cargo_label_mapping.items():
        print(cargo_label, filename)
        """
        sprite = CargoTileSprite(
            id=id, x_loc=x_y[0], y_loc=x_y[1], spriteset_id="spriteset_cargo_tiles"
        )
        result.append(sprite)
        """
    return result


def main():
    # nothing, just here for consistency of module interfaces
    pass
