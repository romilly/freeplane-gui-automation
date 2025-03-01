"""
Tools menu commands for Freeplane automation.
"""

import time
import logging
import pyautogui
from gui_automation.commands.common import DEFAULT_DELAY

__all__ = [
    'manage_time',
    'clear_dependencies',
    'trace_precedents',
    'trace_dependents',
    'preferences',
    'mind_map_editor',
    'file_explorer'
]

def manage_time():
    """Manage time (Ctrl+T)"""
    logging.info("Opening time management")
    pyautogui.hotkey('ctrl', 't')
    time.sleep(DEFAULT_DELAY)

def clear_dependencies():
    """Clear dependencies (Alt+F6)"""
    logging.info("Clearing dependencies")
    pyautogui.hotkey('alt', 'f6')
    time.sleep(DEFAULT_DELAY)

def trace_precedents():
    """Trace precedents (Alt+F7)"""
    logging.info("Tracing precedents")
    pyautogui.hotkey('alt', 'f7')
    time.sleep(DEFAULT_DELAY)

def trace_dependents():
    """Trace dependents (Alt+F8)"""
    logging.info("Tracing dependents")
    pyautogui.hotkey('alt', 'f8')
    time.sleep(DEFAULT_DELAY)

def preferences():
    """Open preferences (Ctrl+Comma)"""
    logging.info("Opening preferences")
    pyautogui.hotkey('ctrl', ',')
    time.sleep(DEFAULT_DELAY)

def mind_map_editor():
    """Switch to mind map editor (Alt+1)"""
    logging.info("Switching to mind map editor")
    pyautogui.hotkey('alt', '1')
    time.sleep(DEFAULT_DELAY)

def file_explorer():
    """Switch to file explorer (Alt+3)"""
    logging.info("Switching to file explorer")
    pyautogui.hotkey('alt', '3')
    time.sleep(DEFAULT_DELAY)
