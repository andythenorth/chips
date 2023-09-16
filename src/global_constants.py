# Definition of station tile numeric IDs
tile_numeric_ids = dict(
    # add ids here in format below
    # plaza_tile_1=85,
)

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

