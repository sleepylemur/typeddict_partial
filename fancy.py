import builtins
from typing import Tuple, Type
from mypy.nodes import TypeInfo
from mypy.plugin import FunctionContext, Plugin
from mypy.types import Instance, Overloaded
from mypy.plugin import CheckerPluginInterface

# from mypy.checker import *


def zoop_return(ctx: FunctionContext) -> Type:
    checker: CheckerPluginInterface = ctx.api
    # res = checker.named_type("builtins.int")
    # print(res, type(res))
    # checker.fail("blarrgh", ctx.context)
    import pdb

    pdb.set_trace()
    print(ctx)
    typ: Instance = ctx.default_return_type
    x = typ.copy_modified(
        items=[checker.named_type("builtins.int"), checker.named_type("builtins.int")]
    )
    ctx.default_return_type.items
    print(x)
    print(typ)
    return checker.named_type("builtins.str")


class CustomPlugin(Plugin):
    def get_function_hook(self, fullname: str):
        print(fullname)
        if fullname == "main.zoop":
            return zoop_return


def plugin(version: str):
    # ignore version argument if the plugin works with all mypy versions.
    return CustomPlugin
