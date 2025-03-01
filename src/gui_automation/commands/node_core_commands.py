"""
Node core editing and formatting commands for Freeplane automation.
"""

import time
import logging
import pyautogui
from gui_automation.commands.common import DEFAULT_DELAY

__all__ = [
    'edit_node_core_inline',
    'edit_node_core_dialog',
    'split_node',
    'join_nodes',
    'format_bold',
    'format_italic',
    'larger_font',
    'smaller_font',
    'node_color',
    'node_background_color',
    'use_plain_text'
]

def edit_node_core_inline():
    """Edit node core in-line (F2)"""
    logging.info("Editing node core inline")
    pyautogui.press('f2')
    time.sleep(DEFAULT_DELAY)

def edit_node_core_dialog():
    """Edit node core in dialog (Alt+Enter)"""
    logging.info("Opening node core edit dialog")
    pyautogui.hotkey('alt', 'enter')
    time.sleep(DEFAULT_DELAY)

def split_node():
    """Split node (Alt+S)"""
    logging.info("Splitting node")
    pyautogui.hotkey('alt', 's')
    time.sleep(DEFAULT_DELAY)

def join_nodes():
    """Join nodes with \\n (Ctrl+J)"""
    logging.info("Joining nodes")
    pyautogui.hotkey('ctrl', 'j')
    time.sleep(DEFAULT_DELAY)

def format_bold():
    """Format text as bold (Ctrl+B)"""
    logging.info("Formatting text as bold")
    pyautogui.hotkey('ctrl', 'b')
    time.sleep(DEFAULT_DELAY)

def format_italic():
    """Format text as italic (Ctrl+I)"""
    logging.info("Formatting text as italic")
    pyautogui.hotkey('ctrl', 'i')
    time.sleep(DEFAULT_DELAY)

def larger_font():
    """Increase font size (Ctrl+Plus)"""
    logging.info("Increasing font size")
    pyautogui.hotkey('ctrl', '+')
    time.sleep(DEFAULT_DELAY)

def smaller_font():
    """Decrease font size (Ctrl+Minus)"""
    logging.info("Decreasing font size")
    pyautogui.hotkey('ctrl', '-')
    time.sleep(DEFAULT_DELAY)

def node_color():
    """Change node color (Alt+Shift+F)"""
    logging.info("Opening node color dialog")
    pyautogui.hotkey('alt', 'shift', 'f')
    time.sleep(DEFAULT_DELAY)

def node_background_color():
    """Change node background color (Alt+B)"""
    logging.info("Opening node background color dialog")
    pyautogui.hotkey('alt', 'b')
    time.sleep(DEFAULT_DELAY)

def use_plain_text():
    """Use plain text (Alt+Shift+P)"""
    logging.info("Switching to plain text")
    pyautogui.hotkey('alt', 'shift', 'p')
    time.sleep(DEFAULT_DELAY)
