from PIL import Image
import os.path
import codecs  # used for writing files - more unicode friendly than standard open() module
import global_constants
from polar_fox import git_info


def get_makefile_args(sys):
    # get args passed by makefile
    if len(sys.argv) > 1:
        makefile_args = {
            "no_mp": sys.argv[1],
        }
    else:
        # provide any necessary defaults here
        makefile_args = {}
    return makefile_args


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


def parse_base_lang():
    # pick out strings for docs, both from lang file, and extra strings that can't be in the lang file
    base_lang_file = codecs.open(
        os.path.join("src", "lang", "english.lng"), "r", "utf8"
    )
    strings = split_nml_string_lines(base_lang_file.readlines())

    extra_strings_file = codecs.open(
        os.path.join("src", "docs_templates", "extra_strings.lng"), "r", "utf8"
    )
    extra_strings = split_nml_string_lines(extra_strings_file.readlines())
    for i in extra_strings:
        strings[i] = extra_strings[i]

    return strings


def unwrap_nml_string_declaration(nml_string=None):
    # some properties are declared in python as 'string(STR_HAM_EGGS)'
    # this is done because it saves hassle with nml (distinguishes from default OTTD strings)
    # doesn't work for direct lookups of string identifier in lang file though, so remove the string() packaging

    if nml_string is not None and "string(" in nml_string:
        unwrapped_string = nml_string.split("string(")[1][
            :-1
        ]  # split and then slice off the closing bracket
        return unwrapped_string
    else:
        return nml_string


def echo_message(message, message_type=None):
    # use to raise messages from templates to standard out (can't print directly from template render)
    # magically wraps these messages in ANSI colour to make them visible - they are only intended for noticeable messages, not general output
    if message_type == "info":
        color = "\033[36m"  # cyan
    else:
        color = "\033[33m"  # yellow
    print(color + message + "\033[0m")
