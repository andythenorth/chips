from sprite import BufferStopSprite

# labels and x y offsets
buffer_stop_sprites = {
    "ne": (10, 10),
    "sw": (10, 50),
    "nw": (10, 90),
    "se": (10, 130),
}


def get_sprites():
    # returns a simple list of sprites
    result = []
    for id, x_y in buffer_stop_sprites.items():
        sprite = BufferStopSprite(
            id=id, x_loc=x_y[0], y_loc=x_y[1], spriteset_id="spriteset_buffer_stop"
        )
        result.append(sprite)
    return result


def main():
    # nothing, just here for consistency of module interfaces
    pass
