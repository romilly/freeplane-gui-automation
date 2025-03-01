"""
Edit menu commands for Freeplane automation.
"""

import time
import logging
import pyautogui
from gui_automation.commands.common import DEFAULT_DELAY

__all__ = [
    'add_remove_cloud',
    'connect_nodes',
    'remove_node',
    'undo',
    'redo',
    'cut',
    'copy',
    'paste',
    'paste_as',
    'paste_clone',
    'reset_node_position'
]

def add_remove_cloud():
    """Add or remove a cloud (Ctrl+Shift+B)"""
    logging.info("Adding/removing cloud")
    pyautogui.hotkey('ctrl', 'shift', 'b')
    time.sleep(DEFAULT_DELAY)

def connect_nodes():
    """Connect nodes (Ctrl+L)"""
    logging.info("Connecting nodes")
    pyautogui.hotkey('ctrl', 'l')
    time.sleep(DEFAULT_DELAY)

def remove_node():
    """Remove node (Delete)"""
    logging.info("Removing node")
    pyautogui.press('delete')
    time.sleep(DEFAULT_DELAY)

def undo():
    """Undo (Ctrl+Z)"""
    logging.info("Undoing last action")
    pyautogui.hotkey('ctrl', 'z')
    time.sleep(DEFAULT_DELAY)

def redo():
    """Redo (Ctrl+Y)"""
    logging.info("Redoing last undone action")
    pyautogui.hotkey('ctrl', 'y')
    time.sleep(DEFAULT_DELAY)

def cut():
    """Cut (Ctrl+X)"""
    logging.info("Cutting selection")
    pyautogui.hotkey('ctrl', 'x')
    time.sleep(DEFAULT_DELAY)

def copy():
    """Copy (Ctrl+C)"""
    logging.info("Copying selection")
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(DEFAULT_DELAY)

def paste():
    """Paste (Ctrl+V)"""
    logging.info("Pasting from clipboard")
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(DEFAULT_DELAY)

def paste_as():
    """Paste as (Ctrl+Shift+V)"""
    logging.info("Opening paste as dialog")
    pyautogui.hotkey('ctrl', 'shift', 'v')
    time.sleep(DEFAULT_DELAY)

def paste_clone():
    """Paste clone (Ctrl+D)"""
    logging.info("Pasting clone")
    pyautogui.hotkey('ctrl', 'd')
    time.sleep(DEFAULT_DELAY)

def reset_node_position():
    """Reset node position (Ctrl+R)"""
    logging.info("Resetting node position")
    pyautogui.hotkey('ctrl', 'r')
    time.sleep(DEFAULT_DELAY)
