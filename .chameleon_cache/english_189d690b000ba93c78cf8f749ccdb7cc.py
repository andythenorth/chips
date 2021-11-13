# -*- coding: utf-8 -*-
__filename = '/Users/andy2/Documents/OTTD_graphics/CHIPS/chips/src/templates/english.pylng'

__tokens = {0: ('STR_GRF_NAME                                                    :FIRS Industry Replacement Set ${git_info.get_version()}\nSTR_GRF_DOCS_URL                                                :${utils.get_docs_url()}', 1, 0), 97: ('git_info.get_version()', 1, 97), 188: ('utils.get_docs_url()', 2, 67)}

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

            # <Interpolation value=<Substitution 'STR_GRF_NAME                                                    :FIRS Industry Replacement Set ${git_info.get_version()}\nSTR_GRF_DOCS_URL                                                :${utils.get_docs_url()}\n' (1:0)> braces_required=True translation=False default='"?"' default_marker='"?"' at 1019e6ec0> -> __content_4311961584
            __token = 0
            __token = 97
            __content_4311961584 = _lookup_attr(getitem('git_info'), 'get_version')()
            __content_4311961584 = __quote(__content_4311961584, '\x00', '&#0;', None, None)
            __token = 188
            __content_4311961584_186 = _lookup_attr(getitem('utils'), 'get_docs_url')()
            __content_4311961584_186 = __quote(__content_4311961584_186, '\x00', '&#0;', None, None)
            __content_4311961584 = ('%s%s%s%s%s' % ('STR_GRF_NAME                                                    :FIRS Industry Replacement Set ', (__content_4311961584 if (__content_4311961584 is not None) else ''), '\nSTR_GRF_DOCS_URL                                                :', (__content_4311961584_186 if (__content_4311961584_186 is not None) else ''), '\n', ))
            if (__content_4311961584 is None):
                pass
            else:
                if (__content_4311961584 is None):
                    __content_4311961584 = None
                else:
                    __tt = type(__content_4311961584)
                    if ((__tt is int) or (__tt is float) or (__tt is int)):
                        __content_4311961584 = str(__content_4311961584)
                    else:
                        if (__tt is bytes):
                            __content_4311961584 = decode(__content_4311961584)
                        else:
                            if (__tt is not str):
                                try:
                                    __content_4311961584 = __content_4311961584.__html__
                                except get('AttributeError', AttributeError):
                                    __converted = convert(__content_4311961584)
                                    __content_4311961584 = (str(__content_4311961584) if (__content_4311961584 is __converted) else __converted)
                                else:
                                    __content_4311961584 = __content_4311961584()
            if (__content_4311961584 is not None):
                __append(__content_4311961584)
            __append('\nSTR_EMPTY                                                       :\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }