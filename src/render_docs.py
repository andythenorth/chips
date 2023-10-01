import codecs  # used for writing files - more unicode friendly than standard open() module

import shutil
import sys
import os

currentdir = os.curdir
from time import time
import markdown

import chips
import utils
import global_constants
from polar_fox import git_info
from doc_helper import DocHelper

metadata = {}
metadata.update(global_constants.metadata)

# get args passed by makefile
command_line_args = utils.get_command_line_args()

docs_src = os.path.join(currentdir, "src", "docs_templates")


def render_docs(
    doc_list,
    file_type,
    docs_output_path,
    chips,
    doc_helper,
    use_markdown=False,
    source_is_repo_root=False,
):
    if source_is_repo_root:
        doc_path = os.path.join(currentdir)
    else:
        doc_path = docs_src
    # imports inside functions are generally avoided
    # but PageTemplateLoader is expensive to import and causes unnecessary overhead for Pool mapping when processing docs graphics
    from chameleon import PageTemplateLoader

    docs_templates = PageTemplateLoader(doc_path, format="text")

    for doc_name in doc_list:
        # .pt is the conventional extension for chameleon page templates
        template = docs_templates[doc_name + ".pt"]
        doc = template(
            global_constants=global_constants,
            command_line_args=command_line_args,
            git_info=git_info,
            metadata=metadata,
            utils=utils,
            doc_helper=doc_helper,
            doc_name=doc_name,
        )
        if use_markdown:
            # the doc might be in markdown format, if so we need to render markdown to html, and wrap the result in some boilerplate html
            markdown_wrapper = PageTemplateLoader(docs_src, format="text")[
                "markdown_wrapper.pt"
            ]
            doc = markdown_wrapper(
                content=markdown.markdown(doc),
                global_constants=global_constants,
                command_line_args=command_line_args,
                git_info=git_info,
                metadata=metadata,
                utils=utils,
                doc_helper=doc_helper,
                doc_name=doc_name,
            )
        # save the results of templating
        doc_file = codecs.open(
            os.path.join(docs_output_path, doc_name + "." + file_type),
            "w",
            "utf8",
        )
        doc_file.write(doc)
        doc_file.close()


def main():
    print("[RENDER DOCS]", " ".join(sys.argv))
    start = time()
    # don't init chips on import of this module, do it explicitly inside main()
    chips.main()

    doc_helper = DocHelper(lang_strings=utils.get_lang_data("english")["lang_strings"])

    # default to no mp, makes debugging easier (mp fails to pickle errors correctly)

    # setting up a cache for compiled chameleon templates can significantly speed up template rendering
    chameleon_cache_path = os.path.join(
        currentdir, global_constants.chameleon_cache_dir
    )
    # exist_ok=True is used for case with parallel make (`make -j 2` or similar), don't fail with error if dir already exists
    os.makedirs(chameleon_cache_path, exist_ok=True)
    os.environ["CHAMELEON_CACHE"] = chameleon_cache_path

    docs_output_path = os.path.join(currentdir, "docs")
    html_docs_output_path = os.path.join(docs_output_path, "html")
    if os.path.exists(docs_output_path):
        shutil.rmtree(docs_output_path)
    os.makedirs(docs_output_path)
    os.makedirs(html_docs_output_path)

    shutil.copy(os.path.join(docs_src, "index.html"), docs_output_path)

    static_dir_src = os.path.join(docs_src, "static")
    static_dir_dst = os.path.join(html_docs_output_path, "static")
    shutil.copytree(static_dir_src, static_dir_dst)

    # render standard docs from a list
    html_docs = [
        "code_reference",
        "get_started",
    ]
    txt_docs = ["readme"]
    license_docs = ["license"]
    markdown_docs = ["changelog"]

    render_docs_start = time()
    render_docs(html_docs, "html", html_docs_output_path, chips, doc_helper)
    render_docs(txt_docs, "txt", docs_output_path, chips, doc_helper)
    render_docs(
        license_docs,
        "txt",
        docs_output_path,
        chips,
        doc_helper,
        source_is_repo_root=True,
    )
    # just render the markdown docs twice to get txt and html versions, simples no?
    render_docs(markdown_docs, "txt", docs_output_path, chips, doc_helper)
    render_docs(
        markdown_docs,
        "html",
        html_docs_output_path,
        doc_helper,
        use_markdown=True,
    )
    print("render_docs", time() - render_docs_start)

    """
    # render vehicle details
    # this is slow and _might_ go faster in an MP pool, but eh overhead...
    render_vehicle_details_start = time()
    for consist in roster.engine_consists:
        consist.assert_description_foamer_facts()
        render_docs_vehicle_details(
            consist,
            "vehicle_details_engine",
            html_docs_output_path,
            consists,
            doc_helper,
        )
    print("render_docs_vehicle_details", time() - render_vehicle_details_start)

    """
    print(
        "[RENDER DOCS]",
        "- complete",
        format((time() - start), ".2f") + "s",
    )


if __name__ == "__main__":
    main()
