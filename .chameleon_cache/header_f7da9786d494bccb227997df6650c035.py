# -*- coding: utf-8 -*-
__filename = '/Users/andy2/Documents/OTTD_graphics/CHIPS/chips/src/templates/header.pynml'

__tokens = {0: ('// define the newgrf\ngrf {\n\tgrfid: "${global_constants.grfid}";\n\tname: string(STR_GRF_NAME);\n\tdesc: string(STR_GRF_DESCRIPTION);\n\turl: string(STR_GRF_DOCS_URL);\n\tversion: ${git_info.get_revision()};\n\tmin_compatible_version: 378; // previous nfo max version, probably needs bumped\n}', 1, 0), 38: ('global_constants.grfid', 3, 11), 173: ('git_info.get_revision()', 7, 12)}

from sys import exc_info as _exc_info
from chameleon.utils import lookup_attr as _lookup_attr

import re
import functools
from itertools import chain as __chain
from sys import intern
__default = intern('__default__')
__marker = object()
g_re_amp = re.compile('&(?!([A-Za-z]+|#[0-9]+);)')
g_re_needs_escape = re.compile('[&<>\\"\\\']').search
__re_whitespace = functools.partial(re.compile('\\s+').sub, ' ')

def initialize(__loader, macros, nothing, template):

    def render(__stream, econtext, rcontext, __i18n_domain=None, __i18n_context=None):
        __append = __stream.append
        __re_amp = g_re_amp
        __token = None
        __re_needs_escape = g_re_needs_escape

        def __convert(target):
            if (target is None):
                return
            __tt = type(target)
            if ((__tt is int) or (__tt is float) or (__tt is int)):
                target = str(target)
            else:
                if (__tt is bytes):
                    target = decode(target)
                else:
                    if (__tt is not str):
                        try:
                            target = target.__html__
                        except AttributeError:
                            __converted = convert(target)
                            target = (str(target) if (target is __converted) else __converted)
                        else:
                            target = target()
            return target

        def __quote(target, quote, quote_entity, default, default_marker):
            if (target is None):
                return
            if (target is default_marker):
                return default
            __tt = type(target)
            if ((__tt is int) or (__tt is float) or (__tt is int)):
                target = str(target)
            else:
                if (__tt is bytes):
                    target = decode(target)
                else:
                    if (__tt is not str):
                        try:
                            target = target.__html__
                        except:
                            __converted = convert(target)
                            target = (str(target) if (target is __converted) else __converted)
                        else:
                            return target()
                if (target is not None):
                    try:
                        escape = (__re_needs_escape(target) is not None)
                    except TypeError:
                        pass
                    else:
                        if escape:
                            if ('&' in target):
                                target = target.replace('&', '&amp;')
                            if ('<' in target):
                                target = target.replace('<', '&lt;')
                            if ('>' in target):
                                target = target.replace('>', '&gt;')
                            if ((quote is not None) and (quote in target)):
                                target = target.replace(quote, quote_entity)
            return target
        translate = econtext['__translate']
        decode = econtext['__decode']
        convert = econtext['__convert']
        on_error_handler = econtext['__on_error_handler']
        try:
            getitem = econtext.__getitem__
            get = econtext.get

            # <Interpolation value=<Substitution '// define the newgrf\ngrf {\n\tgrfid: "${global_constants.grfid}";\n\tname: string(STR_GRF_NAME);\n\tdesc: string(STR_GRF_DESCRIPTION);\n\turl: string(STR_GRF_DOCS_URL);\n\tversion: ${git_info.get_revision()};\n\tmin_compatible_version: 378; // previous nfo max version, probably needs bumped\n}\n' (1:0)> braces_required=True translation=False default='"?"' default_marker='"?"' at 103a21fc0> -> __content_4345809904
            __token = 0
            __token = 38
            __content_4345809904 = _lookup_attr(getitem('global_constants'), 'grfid')
            __content_4345809904 = __quote(__content_4345809904, '\x00', '&#0;', None, None)
            __token = 173
            __content_4345809904_171 = _lookup_attr(getitem('git_info'), 'get_revision')()
            __content_4345809904_171 = __quote(__content_4345809904_171, '\x00', '&#0;', None, None)
            __content_4345809904 = ('%s%s%s%s%s' % ('// define the newgrf\ngrf {\n\tgrfid: "', (__content_4345809904 if (__content_4345809904 is not None) else ''), '";\n\tname: string(STR_GRF_NAME);\n\tdesc: string(STR_GRF_DESCRIPTION);\n\turl: string(STR_GRF_DOCS_URL);\n\tversion: ', (__content_4345809904_171 if (__content_4345809904_171 is not None) else ''), ';\n\tmin_compatible_version: 378; // previous nfo max version, probably needs bumped\n}\n', ))
            if (__content_4345809904 is None):
                pass
            else:
                if (__content_4345809904 is None):
                    __content_4345809904 = None
                else:
                    __tt = type(__content_4345809904)
                    if ((__tt is int) or (__tt is float) or (__tt is int)):
                        __content_4345809904 = str(__content_4345809904)
                    else:
                        if (__tt is bytes):
                            __content_4345809904 = decode(__content_4345809904)
                        else:
                            if (__tt is not str):
                                try:
                                    __content_4345809904 = __content_4345809904.__html__
                                except get('AttributeError', AttributeError):
                                    __converted = convert(__content_4345809904)
                                    __content_4345809904 = (str(__content_4345809904) if (__content_4345809904 is __converted) else __converted)
                                else:
                                    __content_4345809904 = __content_4345809904()
            if (__content_4345809904 is not None):
                __append(__content_4345809904)
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }