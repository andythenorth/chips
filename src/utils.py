import argparse

import os.path
import codecs  # used for writing files - more unicode friendly than standard open() module
import tomllib

currentdir = os.curdir

import global_constants
from polar_fox import git_info


def get_command_line_args():
    argparser = argparse.ArgumentParser()
    # nothing - see Iron Horse for how this is used
    return argparser.parse_args()


def get_docs_url():
    # not convinced this belongs in utils, but I can't find anywhere better to put it
    # could be in polar fox - method will be common to all grfs? - pass the project name as a var?
    # not convinced it's big enough to bother centralising TBH, too much close coupling has costs
    result = [global_constants.metadata["docs_url"]]
    if git_info.get_tag_exact_match() != "undefined":
        result.append(git_info.get_tag_exact_match())
    result.append("index.html")
    return "/".join(result)


def unescape_chameleon_output(escaped_nml):
    # first drop as much whitespace as we sensibly can
    # in tests, this doesn't make the compile any faster at all, but it reduced firs.nml (v3.0.4) from 326k lines to 226k lines,
    escaped_nml = "\n".join(
        [x for x in escaped_nml.split("\n") if x.strip(" \t\n\r") != ""]
    )
    # chameleon html-escapes some characters; that's sane and secure for chameleon's intended web use, but not wanted for nml
    # there is probably a standard module for unescaping html entities, but this will do for now
    escaped_nml = ">".join(escaped_nml.split("&gt;"))
    escaped_nml = "<".join(escaped_nml.split("&lt;"))
    escaped_nml = "&".join(escaped_nml.split("&amp;"))
    return escaped_nml


def split_nml_string_lines(text):
    # this is fragile, playing one line python is silly :)
    return dict(
        (line.split(":", 1)[0].strip(), line.split(":", 1)[1].strip())
        for line in text
        if ":" in line
    )


def get_lang_data(lang):
    global_pragma = {}
    lang_strings = {}
    with open(os.path.join(currentdir, "src", "lang", lang + ".toml"), "rb") as fp:
        lang_source = tomllib.load(fp)

    for node_name, node_value in lang_source.items():
        if node_name == "GLOBAL_PRAGMA":
            # explicit handling of global pragma items
            global_pragma["grflangid"] = node_value["grflangid"]
            global_pragma["plural"] = node_value["plural"]
            if node_value.get("gender", False):
                global_pragma["gender"] = node_value["gender"]
            if node_value.get("case", False):
                global_pragma["case"] = node_value["case"]
        else:
            lang_strings[node_name] = node_value["base"]

    return {"global_pragma": global_pragma, "lang_strings": lang_strings}


def echo_message(message, message_type=None):
    # use to raise messages from templates to standard out (can't print directly from template render)
    # magically wraps these messages in ANSI colour to make them visible - they are only intended for noticeable messages, not general output
    if message_type == "info":
        color = "\033[36m"  # cyan
    else:
        color = "\033[33m"  # yellow
    print(color + message + "\033[0m")
