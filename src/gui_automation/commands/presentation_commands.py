"""
Presentation-related commands for Freeplane automation.
"""

import time
import logging
import pyautogui
from gui_automation.commands.common import DEFAULT_DELAY

__all__ = [
    'run_presentation',
    'stop_presentation',
    'previous_slide'
]

def run_presentation():
    """Run presentation / Next slide (F5)"""
    logging.info("Running presentation/Next slide")
    pyautogui.press('f5')
    time.sleep(DEFAULT_DELAY)

def stop_presentation():
    """Stop presentation (Shift+F5)"""
    logging.info("Stopping presentation")
    pyautogui.hotkey('shift', 'f5')
    time.sleep(DEFAULT_DELAY)

def previous_slide():
    """Go to previous slide (Ctrl+F5)"""
    logging.info("Going to previous slide")
    pyautogui.hotkey('ctrl', 'f5')
    time.sleep(DEFAULT_DELAY)
