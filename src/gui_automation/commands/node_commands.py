"""
Node creation commands for Freeplane automation.
"""

import time
import logging
import pyautogui
from gui_automation.commands.common import DEFAULT_DELAY

__all__ = [
    'new_child_node',
    'new_sibling_node',
    'new_previous_sibling_node',
    'new_parent_node',
    'new_summary_node'
]

def new_child_node():
    """Create a new child node (Insert)"""
    logging.info("Creating new child node")
    pyautogui.press('insert')
    time.sleep(DEFAULT_DELAY)

def new_sibling_node():
    """Create a new sibling node (Enter)"""
    logging.info("Creating new sibling node")
    pyautogui.press('enter')
    time.sleep(DEFAULT_DELAY)

def new_previous_sibling_node():
    """Create a new previous sibling node (Shift+Enter)"""
    logging.info("Creating new previous sibling node")
    pyautogui.hotkey('shift', 'enter')
    time.sleep(DEFAULT_DELAY)

def new_parent_node():
    """Create a new parent node (Shift+Insert)"""
    logging.info("Creating new parent node")
    pyautogui.hotkey('shift', 'insert')
    time.sleep(DEFAULT_DELAY)

def new_summary_node():
    """Create a new summary node for selected nodes (Alt+Shift+Insert)"""
    logging.info("Creating new summary node")
    pyautogui.hotkey('alt', 'shift', 'insert')
    time.sleep(DEFAULT_DELAY)
