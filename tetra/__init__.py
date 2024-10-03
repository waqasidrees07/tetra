"""Full stack component framework for Django using Alpine.js"""

from .components import BasicComponent, Component, public
from .library import Library

__version__ = "0.1.2"
__version_info__ = tuple([int(num) for num in __version__.split(".")])
