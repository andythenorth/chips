# Definition of station tile numeric IDs
tile_numeric_ids = dict(
    # add ids here in format below
    # plaza_tile_1=85,
)

class DwordGrfID(object):
    """
    grfids in game and bananas are presented as dwords, so it would be more convenient all round to use the dword
    however nml wants grfids as literals, so this class stores a dword, and converts it to an *nml* literal on demand
    """

    def __init__(self, grfid):
        self.grfid_as_dword = grfid  # keep the grfid around in case it's wanted for docs etc (as yet unknown)
        # split to bytes
        split = [
            self.grfid_as_dword[i : i + 2]
            for i in range(0, len(self.grfid_as_dword), 2)
        ]
        self.grfid = "\\" + "\\".join(
            split
        )  # note the leading '\' that nml requires (escaped as double \\ for python)


#grfid = DwordGrfID("43485054").grfid
grfid = "CHPT"

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

