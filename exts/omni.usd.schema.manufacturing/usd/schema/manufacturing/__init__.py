from .extension import *
import os

from pxr import Plug

pluginsRoot = os.path.join(os.path.dirname(__file__), '../../../../plugins')
manufacturingSchemaPath = pluginsRoot + '/UsdManufacturing/resources'

Plug.Registry().RegisterPlugins(manufacturingSchemaPath)