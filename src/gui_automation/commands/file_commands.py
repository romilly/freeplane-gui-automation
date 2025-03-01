"""
File menu commands for Freeplane automation.
"""

import time
import logging
import pyautogui
from gui_automation.commands.common import DEFAULT_DELAY, type_text

__all__ = [
    'new_map',
    'save_map',
    '_save_map_as',
    'save_map_as',
    'open_map',
    'print_map',
    'close_current_map',
    'quit_freeplane'
]

def new_map():
    """Create a new mind map (Ctrl+N) and ensure focus is on the new map"""
    logging.info("Creating new map")
    pyautogui.hotkey('ctrl', 'n')
    time.sleep(DEFAULT_DELAY)
    return True

def save_map():
    """Save the current map (Ctrl+S)"""
    logging.info("Saving map")
    pyautogui.hotkey('ctrl', 's')
    time.sleep(DEFAULT_DELAY)

def _save_map_as():
    """Save the map as (Ctrl+Shift+S)"""
    logging.info("Opening Save As dialog")
    pyautogui.hotkey('ctrl', 'shift', 's')
    time.sleep(DEFAULT_DELAY)

def save_map_as(filepath):
    """
    Save the map as with the specified filepath.
    Handles the full dialog interaction.

    Args:
        filepath (str): The full path or filename to save the map as
    """
    logging.info(f"Saving map as: {filepath}")
    
    # Open Save As dialog
    _save_map_as()
    time.sleep(DEFAULT_DELAY * 2)  # Give dialog time to open
    
    # Type the filepath
    type_text(filepath, human_like=False)
    time.sleep(DEFAULT_DELAY)
    
    # Press Enter to confirm
    pyautogui.press('enter')
    time.sleep(DEFAULT_DELAY * 2)  # Give save operation time to complete

def open_map():
    """Open a saved map (Ctrl+O)"""
    logging.info("Opening map selection dialog")
    pyautogui.hotkey('ctrl', 'o')
    time.sleep(DEFAULT_DELAY)

def print_map():
    """Print the map (Ctrl+P)"""
    logging.info("Opening print dialog")
    pyautogui.hotkey('ctrl', 'p')
    time.sleep(DEFAULT_DELAY)

def close_current_map():
    """Close the current map (Ctrl+W)"""
    logging.info("Closing current map")
    pyautogui.hotkey('ctrl', 'w')
    time.sleep(DEFAULT_DELAY)

def quit_freeplane():
    """Quit Freeplane (Ctrl+Q)"""
    logging.info("Quitting Freeplane")
    pyautogui.hotkey('ctrl', 'q')
    time.sleep(DEFAULT_DELAY)
