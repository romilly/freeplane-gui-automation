"""
Node properties commands for Freeplane automation.
"""

import time
import logging
import pyautogui
from .common import DEFAULT_DELAY

__all__ = [
    'edit_node_details_inline',
    'edit_node_details_dialog',
    'edit_attribute_inline'
]

def edit_node_details_inline():
    """Edit node details in-line (F3)"""
    logging.info("Editing node details inline")
    pyautogui.press('f3')
    time.sleep(DEFAULT_DELAY)

def edit_node_details_dialog():
    """Edit node details in dialog (Ctrl+F3)"""
    logging.info("Opening node details dialog")
    pyautogui.hotkey('ctrl', 'f3')
    time.sleep(DEFAULT_DELAY)

def edit_attribute_inline():
    """Edit attribute in-line (Alt+F9)"""
    logging.info("Editing attribute inline")
    pyautogui.hotkey('alt', 'f9')
    time.sleep(DEFAULT_DELAY)
