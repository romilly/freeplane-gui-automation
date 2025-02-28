"""
Freeplane automation commands package.
Provides functions for automating Freeplane mind mapping software using keyboard shortcuts.
"""

from .file_commands import *
from .edit_commands import *
from .node_commands import *
from .link_commands import *
from .node_core_commands import *
from .node_properties_commands import *
from .note_commands import *
from .format_commands import *
from .view_commands import *
from .navigation_commands import *
from .fold_commands import *
from .presentation_commands import *
from .tools_commands import *
from .common import find_freeplane_window, type_text

# Version of the commands package
__version__ = '0.1.0'
