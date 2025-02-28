"""
Fold-related commands for Freeplane automation.
"""

import time
import logging
import pyautogui
from .common import DEFAULT_DELAY

__all__ = [
    'unfold',
    'show_next_child',
    'unfold_children',
    'unfold_one_level',
    'fold_one_level',
    'unfold_all',
    'fold_all'
]

def unfold():
    """Unfold node (Space)"""
    logging.info("Unfolding node")
    pyautogui.press('space')
    time.sleep(DEFAULT_DELAY)

def show_next_child():
    """Show next child (Shift+Space)"""
    logging.info("Showing next child")
    pyautogui.hotkey('shift', 'space')
    time.sleep(DEFAULT_DELAY)

def unfold_children():
    """Unfold children (Ctrl+Space)"""
    logging.info("Unfolding children")
    pyautogui.hotkey('ctrl', 'space')
    time.sleep(DEFAULT_DELAY)

def unfold_one_level():
    """Unfold one level (Alt+Page Down)"""
    logging.info("Unfolding one level")
    pyautogui.hotkey('alt', 'pagedown')
    time.sleep(DEFAULT_DELAY)

def fold_one_level():
    """Fold one level (Alt+Page Up)"""
    logging.info("Folding one level")
    pyautogui.hotkey('alt', 'pageup')
    time.sleep(DEFAULT_DELAY)

def unfold_all():
    """Unfold all (Alt+End)"""
    logging.info("Unfolding all nodes")
    pyautogui.hotkey('alt', 'end')
    time.sleep(DEFAULT_DELAY)

def fold_all():
    """Fold all (Alt+Home)"""
    logging.info("Folding all nodes")
    pyautogui.hotkey('alt', 'home')
    time.sleep(DEFAULT_DELAY)
