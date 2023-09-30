grfid = "CHPR"

metadata = {
    "dev_thread_url": "https://www.tt-forums.net/viewtopic.php?t=53348",
    "repo_url": "https://github.com/andythenorth/chips",
    "docs_url": "https://grf.farm/chips",
}

# this is for nml or grfcodec, don't need to use python path module here
graphics_path = "generated/graphics/"

# OpenTTD's max date
max_game_date = 5000000

graphics_temp_storage = dict(
    var_sprite_rear_platform_ne_sw=0, # ground-type-specific sprite for track tiles
    var_sprite_rear_platform_nw_se=1, # ground-type-specific sprite for track tiles
    var_sprite_front_platform_ne_sw=2, # ground-type-specific sprite for track tiles
    var_sprite_front_platform_nw_se=3, # ground-type-specific sprite for track tiles
    var_sprite_whole_tile=4, # ground-type-specific sprite for non_track tiles
    # unused=5,  #
    # unused=6,  #
    # unused=7,  #
    # unused=8,  #
    # unused=9,  #
    # unused=10,  #
    # unused=11,  #
    # unused=12,  #
    var_terrain_is_snow=13,  # must be set to 1 (true) or 0 (false)
    var_random_bits=14,  # some random bits to use as required
    # unused=15,  #
    # unused=16,  #
    # unused=17,  #
    # unused=18,  #
    var_hide_building_snow=19,  # hide a snow building in spritelayout, must be set to 1 (true) or 0 (false)
)

station_classes_by_metaclass = {
    # default town stations go into the DFLT class, alongside the base game stations, and we also change the name string for that class
    "town": [
        {
            "class_id": "DFLT",
            "default_ground_type": "pavement",
        },
    ],
    "industry": [
        {
            "class_id": "INAS",
            "default_ground_type": "asphalt",
        },
        {
            "class_id": "INGR",
            "default_ground_type": "gravel",
        },
        {
            "class_id": "INCO",
            "default_ground_type": "cobble",
        },
        {
            "class_id": "INDI",
            "default_ground_type": "dirt",
        },
    ],
}

# labels and x offsets
ground_tiles_cabbage = {
    "dirt": 10,
    "asphalt": 80,
    "gravel": 150,
    "cobble": 220,
    "pavement": 290,
}

ground_tiles = {
    "dirt_whole_tile": (10, 10),
    "dirt_rear_platform_ne_sw": (10, 50),
    "dirt_front_platform_ne_sw": (10, 90),
    "dirt_rear_platform_nw_se": (10, 130),
    "dirt_front_platform_nw_se": (10, 170),
    "asphalt_whole_tile": (80, 10),
    "asphalt_rear_platform_ne_sw": (80, 50),
    "asphalt_front_platform_ne_sw": (80, 90),
    "asphalt_rear_platform_nw_se": (80, 130),
    "asphalt_front_platform_nw_se": (80, 170),
    "gravel_whole_tile": (150, 10),
    "gravel_rear_platform_ne_sw": (150, 50),
    "gravel_front_platform_ne_sw": (150, 90),
    "gravel_rear_platform_nw_se": (150, 130),
    "gravel_front_platform_nw_se": (150, 170),
    "cobble_whole_tile": (220, 10),
    "cobble_rear_platform_ne_sw": (220, 50),
    "cobble_front_platform_ne_sw": (220, 90),
    "cobble_rear_platform_nw_se": (220, 130),
    "cobble_front_platform_nw_se": (220, 170),
    "pavement_whole_tile": (290, 10),
    "pavement_rear_platform_ne_sw": (290, 50),
    "pavement_front_platform_ne_sw": (290, 90),
    "pavement_rear_platform_nw_se": (290, 130),
    "pavement_front_platform_nw_se": (290, 170),
}

# shared global constants via Polar Fox library - import at end to make the this project's constants easier to work with
# done this way so we don't have to pass Polar Fox to templates, we can just pass global_constants
# assignments are clunky - they exist to stop pyflakes tripping on 'unused' imports
import polar_fox.constants

cargo_labels = polar_fox.constants.cargo_labels
chameleon_cache_dir = polar_fox.constants.chameleon_cache_dir
generated_files_dir = polar_fox.constants.generated_files_dir
