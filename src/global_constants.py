grfid = "CHPR"

metadata = {
    "dev_thread_url": "https://www.tt-forums.net/viewtopic.php?t=53348",
    "repo_url": "https://github.com/andythenorth/chips",
    "docs_url": "https://grf.farm/chips",
}

chameleon_cache_dir = ".chameleon_cache"

# specify location for intermediate files generated during build (nml, graphics, lang etc)
generated_files_dir = "generated"

# this is for nml or grfcodec, don't need to use python path module here
graphics_path = "generated/graphics/"

# OpenTTD's max date
max_game_date = 5000000

graphics_temp_storage = dict(
    var_ground_sprite=0,  # ID of ground sprite
    var_fencesprite_ne=1,  # fence sprite to use on the NE border
    var_fencesprite_nw=2,  # fence sprite to use on the NW border
    var_fencesprite_se=3,  # fence sprite to use on the SE border
    var_fencesprite_sw=4,  # fence sprite to use on the SW border
    var_fence_offset_ne=5,  # y-offset for fence sprite to use on the NE border
    var_fence_offset_nw=6,  # y-offset for fence sprite to use on the NW border
    var_fence_offset_se=7,  # y-offset for fence sprite to use on the SE border
    var_fence_offset_sw=8,  # y-offset for fence sprite to use on the SW border
    var_use_fence_ne=9,  # draw fence in the NE
    var_use_fence_nw=10,  # draw fence in the NW
    var_use_fence_se=11,  # draw fence in the SE
    var_use_fence_sw=12,  # draw fence in the SW
    var_terrain_is_snow=13,  # must be set to 1 (true) or 0 (false)
    var_random_bits=14,  # some random bits to use as required
    # unused=15,  # hide tree sprite for default (temperate, arctic below snowline)
    # unused=16,  # hide tree sprite for snow
    # unused=17,  # hide tree sprite for snow
    var_hide_building=18,  # hide a building in spritelayout, must be set to 1 (true) or 0 (false)
    var_hide_building_snow=19,  # hide a snow building in spritelayout, must be set to 1 (true) or 0 (false)
)  # max register number must be 235; registers 236-255 are reserved for building sprite hide/show values

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
