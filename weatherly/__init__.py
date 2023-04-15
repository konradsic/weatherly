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
__version__ = '0.0.1'

from typing import NamedTuple, Literal

from .api import *
from .errors import *
from . import (
    utils as utils
)

class VersionInfo(NamedTuple):
    major: int
    minor: int
    micro: int
    release_type: Literal["alpha", "beta", "pre", "final"]
    
version_info = VersionInfo(major=0, minor=0, micro=1, release_type="pre")


del NamedTuple, Literal, VersionInfo