"""
View-related commands for Freeplane automation.
"""

import time
import logging
import pyautogui
from gui_automation.commands.common import DEFAULT_DELAY

__all__ = [
    'full_screen_mode'
]

def full_screen_mode():
    """Toggle full screen mode (F11)"""
    logging.info("Toggling full screen mode")
    pyautogui.press('f11')
    time.sleep(DEFAULT_DELAY)
