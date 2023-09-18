print("[RENDER NML] render_nml.py")

import codecs  # used for writing files - more unicode friendly than standard open() module

import sys
import os

currentdir = os.curdir
from time import time

import chips
import utils
import global_constants
from polar_fox import git_info

# get args passed by makefile
makefile_args = utils.get_makefile_args(sys)

# chameleon used in most template cases
from chameleon import PageTemplateLoader

# setup the places we look for templates
templates = PageTemplateLoader(os.path.join(currentdir, "src", "templates"))

# setting up a cache for compiled chameleon templates can significantly speed up template rendering
chameleon_cache_path = os.path.join(currentdir, global_constants.chameleon_cache_dir)
if not os.path.exists(chameleon_cache_path):
    os.mkdir(chameleon_cache_path)
os.environ["CHAMELEON_CACHE"] = chameleon_cache_path

generated_files_path = chips.generated_files_path


def render_header_item_nml(header_item):
    template = templates[header_item + ".pynml"]
    return utils.unescape_chameleon_output(
        template(
            global_constants=global_constants,
            utils=utils,
            graphics_path=global_constants.graphics_path,
            makefile_args=makefile_args,
            git_info=git_info,
        )
    )


def render_item_nml(item):
    result = utils.unescape_chameleon_output(item.render(templates))
    # write the nml per item to disk, it aids debugging
    item_nml = codecs.open(
        os.path.join(generated_files_path, "nml", item.id + ".nml"), "w", "utf8"
    )
    item_nml.write(result)
    item_nml.close()
    # also return the nml directly for writing to the concatenated nml, don't faff around opening the generated nml files from disk
    return result


def main():
    start = time()
    chips.main()

    generated_nml_path = os.path.join(generated_files_path, "nml")
    if not os.path.exists(generated_nml_path):
        # reminder to self: inside main() to avoid modifying filesystem simply by importing module
        os.mkdir(generated_nml_path)
    grf_nml = codecs.open(
        os.path.join(generated_files_path, "chips.nml"), "w", "utf8"
    )
    """
    spritelayer_cargos = iron_horse.registered_spritelayer_cargos
    consists = iron_horse.get_consists_in_buy_menu_order()
    """
    header_items = [
        "header",
        "cargotable",
        "spritesets",
        "dock",
        "rail_station",
        "road_stop",
    ]
    for header_item in header_items:
        grf_nml.write(render_header_item_nml(header_item))

    """
    # multiprocessing was tried here and removed as it was empirically slower in testing (due to overhead of starting extra pythons probably)
    for spritelayercargo in spritelayer_cargos:
        grf_nml.write(render_item_nml(spritelayercargo))
    for consist in consists:
        grf_nml.write(render_item_nml(consist))
    """
    grf_nml.close()

    print(format((time() - start), ".2f") + "s")


if __name__ == "__main__":
    main()
