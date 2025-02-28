"""
Note-related commands for Freeplane automation.
"""

import time
import logging
import pyautogui
from .common import DEFAULT_DELAY

__all__ = [
    'display_note_panel',
    'note_edit_switch'
]

def display_note_panel():
    """Display note panel (Ctrl+Greater)"""
    logging.info("Displaying note panel")
    pyautogui.hotkey('ctrl', '>')
    time.sleep(DEFAULT_DELAY)

def note_edit_switch():
    """Note Edit Switch (Ctrl+Less)"""
    logging.info("Switching note edit mode")
    pyautogui.hotkey('ctrl', '<')
    time.sleep(DEFAULT_DELAY)
