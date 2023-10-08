# numeric IDs are significant for purchase list order of stations
# we could control the order by auto-assignment of IDs, but this breaks savegames when facility types (or station tiles) are added or removed
# so the best-efforts solution is a manual list, with widely spaced assignments, so that new types can be inserted in the gaps later
# this is faff, but will work, as experience with other grfs has proven (although splitting purchase order from ID is better)
# occasionally a savegame-breaking reset of IDs might be needed
# RANGE SPACING: 1000 by default, then insert any new facility types on 100 spacing
# each facility type isn't expected to consume more than 100 IDs (there might already be a validation check for this?)
facility_type_numeric_ids = dict(
    cargo_visible_freight=0,
    cargo_visible_town=1000,
    concourse_1=2000,
    booking_office_small=3000,
    booking_office=4000,
    parcels_office=5000,
    hotel=6000,
    dispatchers_office=7000,
    warehouse_town=8000,
    boiler_house_office=9000,
    harbour_crane=10000,
    huts=11000,
    tipple=12000,
    flood_loader_silo=13000,
    mine_buildings=14000,
    foundry_buildings=15000,
    cement_silo=16000,
    steel_handling=17000,
)

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
    var_sprite_rear_rail_platform_ne_sw=0,  # ground-type-specific sprite for track tiles
    var_sprite_rear_rail_platform_nw_se=1,  # ground-type-specific sprite for track tiles
    var_sprite_front_rail_platform_ne_sw=2,  # ground-type-specific sprite for track tiles
    var_sprite_front_rail_platform_nw_se=3,  # ground-type-specific sprite for track tiles
    var_sprite_whole_tile=4,  # ground-type-specific sprite for non_track tiles
    var_hide_buffer_stop_ne_and_nw=5,  # hide a buffer stop on a ne or ne edge (as appropriate to station orientation)
    var_hide_buffer_stop_se_and_sw=6,  # hide a buffer stop on a se or sw edge (as appropriate to station orientation)
    var_hide_cargo=7,  # hide cargo sprites
    var_sprite_rear_road_platform_ne_sw=8,  # ground-type-specific sprite for drive-through road tiles
    var_sprite_rear_road_platform_nw_se=9,  # ground-type-specific sprite for drive-through road tiles
    var_sprite_front_road_platform_ne_sw=10,  # ground-type-specific sprite for drive-through road tiles
    var_sprite_front_road_platform_nw_se=11,  # ground-type-specific sprite for drive-through road tiles
    var_palette_building_recolour=12,  # palette for building recolouring
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
            "palette": "PALETTE_USE_DEFAULT",
        },
    ],
    "freight": [
        {
            "class_id": "FRAS",
            "default_ground_type": "asphalt",
            "palette": "PALETTE_USE_DEFAULT",
        },
        {
            "class_id": "FRGR",
            "default_ground_type": "gravel",
            "palette": "PALETTE_USE_DEFAULT",
        },
        {
            "class_id": "FRDI",
            "default_ground_type": "dirt",
            "palette": "PALETTE_USE_DEFAULT",
        },
    ],
    "industry": [
        # based on the supported colours in FIRS, this could be unified via polar fox but eh, might get version drift anyway
        {
            "class_id": "INB0",
            "default_ground_type": "gravel",
            "palette": "PALETTE_CC_DARK_BLUE",
        },
        {
            "class_id": "INB1",
            "default_ground_type": "gravel",
            "palette": "PALETTE_CC_PALE_GREEN",
        },
        {
            "class_id": "INB2",
            "default_ground_type": "gravel",
            "palette": "PALETTE_CC_PINK",
        },
        {
            "class_id": "INB3",
            "default_ground_type": "gravel",
            "palette": "PALETTE_CC_YELLOW",
        },
        {
            "class_id": "INB4",
            "default_ground_type": "gravel",
            "palette": "PALETTE_CC_LIGHT_BLUE",
        },
        {
            "class_id": "INB5",
            "default_ground_type": "gravel",
            "palette": "PALETTE_CC_MAUVE",
        },
        {
            "class_id": "INB6",
            "default_ground_type": "gravel",
            "palette": "PALETTE_CC_PURPLE",
        },
        {
            "class_id": "INB7",
            "default_ground_type": "gravel",
            "palette": "PALETTE_CC_BROWN",
        },
        {
            "class_id": "INB8",
            "default_ground_type": "gravel",
            "palette": "PALETTE_CC_GREY",
        },
        {
            "class_id": "INB_",
            "default_ground_type": "gravel",
            "palette": "PALETTE_USE_DEFAULT",
        },
    ],
}

# extents (bounding boxes should match default stations, for simplicity of sprite sorting etc
# https://github.com/OpenTTD/OpenTTD/blob/master/src/table/station_land.h#L61
# zextents set suitable to each use case, not needed here
rail_station_bounding_boxes = {
    "whole_tile_ne_sw": {"x_offset": 0, "y_offset": 0, "x_extent": 16, "y_extent": 16},
    "rear_platform_ne_sw": {
        "x_offset": 0,
        "y_offset": 0,
        "x_extent": 16,
        "y_extent": 5,
    },
    "front_platform_ne_sw": {
        "x_offset": 0,
        "y_offset": 11,
        "x_extent": 16,
        "y_extent": 5,
    },
    "whole_tile_nw_se": {"x_offset": 0, "y_offset": 0, "x_extent": 16, "y_extent": 16},
    "rear_platform_nw_se": {
        "x_offset": 0,
        "y_offset": 0,
        "x_extent": 5,
        "y_extent": 16,
    },
    "front_platform_nw_se": {
        "x_offset": 11,
        "y_offset": 0,
        "x_extent": 5,
        "y_extent": 16,
    },
}


road_stop_bounding_boxes = {
    "whole_tile_ne_sw": {"x_offset": 0, "y_offset": 0, "x_extent": 16, "y_extent": 16},
    "rear_platform_ne_sw": {
        "x_offset": 0,
        "y_offset": 0,
        "x_extent": 16,
        "y_extent": 3,
    },
    "middle_divider_ne_sw": {
        "x_offset": 0,
        "y_offset": 8,
        "x_extent": 16,
        "y_extent": 0,
    },
    "front_platform_ne_sw": {
        "x_offset": 0,
        "y_offset": 13,
        "x_extent": 16,
        "y_extent": 3,
    },
    "whole_tile_nw_se": {"x_offset": 0, "y_offset": 0, "x_extent": 16, "y_extent": 16},
    "rear_platform_nw_se": {
        "x_offset": 0,
        "y_offset": 0,
        "x_extent": 3,
        "y_extent": 16,
    },
    "middle_divider_nw_se": {
        "x_offset": 8,
        "y_offset": 0,
        "x_extent": 0,
        "y_extent": 16,
    },
    "front_platform_nw_se": {
        "x_offset": 13,
        "y_offset": 0,
        "x_extent": 3,
        "y_extent": 16,
    },
}


# shared global constants via Polar Fox library - import at end to make the this project's constants easier to work with
# done this way so we don't have to pass Polar Fox to templates, we can just pass global_constants
# assignments are clunky - they exist to stop pyflakes tripping on 'unused' imports
import polar_fox.constants

cargo_labels = polar_fox.constants.cargo_labels
chameleon_cache_dir = polar_fox.constants.chameleon_cache_dir
generated_files_dir = polar_fox.constants.generated_files_dir
