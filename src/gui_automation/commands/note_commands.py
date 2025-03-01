"""
Note-related commands for Freeplane automation.
"""

import time
import logging
import pyautogui
from gui_automation.commands.common import DEFAULT_DELAY, type_text

__all__ = [
    'display_note_panel',
    'edit_note'
]

def display_note_panel():
    """Display note panel (Ctrl+Greater)"""
    logging.info("Displaying note panel")
    pyautogui.hotkey('ctrl', '>')
    time.sleep(DEFAULT_DELAY)

def _note_edit_switch():
    """Note Edit Switch (Ctrl+Less)"""
    logging.info("Switching note edit mode")
    pyautogui.hotkey('ctrl', '<')
    time.sleep(DEFAULT_DELAY)

def edit_note(text: str) -> None:
    _note_edit_switch()
    type_text(text)
    _note_edit_switch()

