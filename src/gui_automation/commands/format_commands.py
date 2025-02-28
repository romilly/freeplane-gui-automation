"""
Format-related commands for Freeplane automation.
"""

import time
import logging
import pyautogui
from .common import DEFAULT_DELAY

__all__ = [
    'copy_format',
    'paste_format',
    'redefine_style',
    'copy_map_style',
    'edit_styles'
]

def copy_format():
    """Copy format of a node (Alt+Shift+C)"""
    logging.info("Copying node format")
    pyautogui.hotkey('alt', 'shift', 'c')
    time.sleep(DEFAULT_DELAY)

def paste_format():
    """Paste format to a node (Alt+Shift+V)"""
    logging.info("Pasting node format")
    pyautogui.hotkey('alt', 'shift', 'v')
    time.sleep(DEFAULT_DELAY)

def redefine_style():
    """Redefine style (Alt+R)"""
    logging.info("Redefining style")
    pyautogui.hotkey('alt', 'r')
    time.sleep(DEFAULT_DELAY)

def copy_map_style():
    """Copy map style from (Ctrl+Shift+O)"""
    logging.info("Opening copy map style dialog")
    pyautogui.hotkey('ctrl', 'shift', 'o')
    time.sleep(DEFAULT_DELAY)

def edit_styles():
    """Edit styles (Ctrl+F11)"""
    logging.info("Opening style editor")
    pyautogui.hotkey('ctrl', 'f11')
    time.sleep(DEFAULT_DELAY)
