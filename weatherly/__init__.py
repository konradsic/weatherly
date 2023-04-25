"""
weatherly
===============
A simple Python wrapper around WeatherAPI. Get current weather, forecast, history and more.

:copyright: (c) 2023-present @konradsic
:license: MIT license, see LICENSE for details
"""

__title__ = 'weatherly'
__author__ = 'konradsic'
__license__ = 'MIT'
__copyright__ = 'Copyright 2023-present konradsic'
__version__ = '0.4.0'

from typing import NamedTuple, Literal

from .api import *
from .errors import *
from .enums import *
from .responses import *
from . import (
    utils as utils
)

class VersionInfo(NamedTuple):
    major: int
    minor: int
    micro: int
    release_type: Literal["alpha", "beta", "candidate", "final"]
    
version_info = VersionInfo(major=0, minor=4, micro=0, release_type="final")

del NamedTuple, Literal, VersionInfo
