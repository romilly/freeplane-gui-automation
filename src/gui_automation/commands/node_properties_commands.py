"""
Node properties commands for Freeplane automation.
"""

import time
import logging
import pyautogui
from gui_automation.commands.common import DEFAULT_DELAY, type_text

__all__ = [
    'edit_node_details_inline',
    'edit_node_details_dialog',
    'edit_attribute_inline'
]

def _edit_node_details_inline():
    """Edit node details in-line (F3)"""
    logging.info("Editing node details inline")
    pyautogui.press('f3')
    time.sleep(DEFAULT_DELAY)

def edit_node_details_inline(text: str, human_like=True):
    """Edit node details in-line with specified text"""
    _edit_node_details_inline()
    type_text(text, human_like=human_like)
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
