"""
Link-related commands for Freeplane automation.
"""

import time
import logging
import pyautogui
from gui_automation.commands.common import DEFAULT_DELAY, type_text

__all__ = [
    'add_hyperlink',
    '_add_modify_hyperlink',
    'add_modify_hyperlink',
    'add_local_hyperlink',
    'follow_link'
]

def add_hyperlink():
    """Add hyperlink (Ctrl+Shift+K)"""
    logging.info("Opening add hyperlink dialog")
    pyautogui.hotkey('ctrl', 'shift', 'k')
    time.sleep(DEFAULT_DELAY)

def _add_modify_hyperlink():
    """Add or modify hyperlink with type (Ctrl+K) - Internal function"""
    logging.info("Opening add/modify hyperlink dialog")
    pyautogui.hotkey('ctrl', 'k')
    time.sleep(DEFAULT_DELAY)

def add_modify_hyperlink(url):
    """
    Add or modify a hyperlink with the specified URL.
    Handles the full dialog interaction.

    Args:
        url (str): The URL for the hyperlink
    """
    logging.info(f"Adding/modifying hyperlink: {url}")
    
    # Open hyperlink dialog
    _add_modify_hyperlink()
    time.sleep(DEFAULT_DELAY * 2)  # Give dialog time to open
    
    # Type the URL
    type_text(url, human_like=False)
    time.sleep(DEFAULT_DELAY)
    
    # Press Enter to confirm
    pyautogui.press('enter')
    time.sleep(DEFAULT_DELAY)

def add_local_hyperlink():
    """Add local hyperlink (Alt+Shift+L)"""
    logging.info("Adding local hyperlink")
    pyautogui.hotkey('alt', 'shift', 'l')
    time.sleep(DEFAULT_DELAY)

def follow_link():
    """Follow link (Ctrl+Enter)"""
    logging.info("Following link")
    pyautogui.hotkey('ctrl', 'enter')
    time.sleep(DEFAULT_DELAY)
