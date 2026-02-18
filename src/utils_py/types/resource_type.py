"""
#
#
#  ESTE MODULO ESTA CREADO PARA DECLARAR TODOS LOS TIPOS DEDICADOS A LOS RECURSOS
#   
#
"""

import re
import os
from enum import Enum

from pubsub import pub

#region declaration

#region enumeradores

class PathType(Enum):
    COMPLETE = 0
    RELATIVE = 1


class PathExtensionType(Enum):
    FOLDER = 0
    FILE = 1

#endregion enumeradores

#region clases

#endregion clases

    

#endregion declaration

