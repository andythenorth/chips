# JFDI module to help do some doc formatting

import global_constants
import utils

class DocHelper(object):
    # Some constants

    def __init__(self, lang_strings):
        self.lang_strings = lang_strings

    def get_active_nav(self, doc_name, nav_link):
        return ("", "active")[doc_name == nav_link]
