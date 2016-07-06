# Avoid name clash with raritan.rpc.sys
from __future__ import absolute_import
import sys

class Utils(object):

    @staticmethod
    def indent(string, indent):
        return "\n".join([(" " * indent) + l for l in string.splitlines()])

    @staticmethod
    def rprint(object):
        if sys.version_info.major < 3:
            if isinstance(object, basestring):
                return str(object)
        else:
            if isinstance(object, str):
                return str(object)
        try:
            return '[\n' + ",\n".join(Utils.indent(str(x), 4) for x in object) + '\n' + Utils.indent(']', 4)
        except TypeError: # fallback
            return str(object)
