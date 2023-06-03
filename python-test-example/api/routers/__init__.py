# # -*- encoding: utf-8 -*-
# import sys
# import pkgutil
# import importlib
#
# _self = sys.modules[__name__]
#
# endpoint_routers = [
#     importlib.import_module(mod.name).__dict__['router']
#     for mod in pkgutil.walk_packages(_self.__path__, prefix=_self.__name__ + '.')
# ]
