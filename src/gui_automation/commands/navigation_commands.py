"""
Navigation commands for Freeplane automation.
"""

import time
import logging
import pyautogui
from .common import DEFAULT_DELAY

__all__ = [
    'previous_map',
    'next_map',
    'select_all_visible_nodes',
    'select_visible_branch',
    'goto_root',
    'goto_previous_node',
    'goto_next_node',
    'goto_previous_node_fold',
    'goto_next_node_fold',
    'go_backward',
    'go_forward'
]

def previous_map():
    """Go to previous map (Ctrl+Shift+Tab)"""
    logging.info("Going to previous map")
    pyautogui.hotkey('ctrl', 'shift', 'tab')
    time.sleep(DEFAULT_DELAY)

def next_map():
    """Go to next map (Ctrl+Tab)"""
    logging.info("Going to next map")
    pyautogui.hotkey('ctrl', 'tab')
    time.sleep(DEFAULT_DELAY)

def select_all_visible_nodes():
    """Select all visible nodes (Ctrl+A)"""
    logging.info("Selecting all visible nodes")
    pyautogui.hotkey('ctrl', 'a')
    time.sleep(DEFAULT_DELAY)

def select_visible_branch():
    """Select visible branch (Ctrl+Shift+A)"""
    logging.info("Selecting visible branch")
    pyautogui.hotkey('ctrl', 'shift', 'a')
    time.sleep(DEFAULT_DELAY)

def goto_root():
    """Go to root node (Escape)"""
    logging.info("Going to root node")
    pyautogui.press('escape')
    time.sleep(DEFAULT_DELAY)

def goto_previous_node():
    """Go to previous node (Ctrl+Alt+Left)"""
    logging.info("Going to previous node")
    pyautogui.hotkey('ctrl', 'alt', 'left')
    time.sleep(DEFAULT_DELAY)

def goto_next_node():
    """Go to next node (Ctrl+Alt+Right)"""
    logging.info("Going to next node")
    pyautogui.hotkey('ctrl', 'alt', 'right')
    time.sleep(DEFAULT_DELAY)

def goto_previous_node_fold():
    """Go to previous node (fold) (Ctrl+Shift+Left)"""
    logging.info("Going to previous node (fold)")
    pyautogui.hotkey('ctrl', 'shift', 'left')
    time.sleep(DEFAULT_DELAY)

def goto_next_node_fold():
    """Go to next node (fold) (Ctrl+Shift+Right)"""
    logging.info("Going to next node (fold)")
    pyautogui.hotkey('ctrl', 'shift', 'right')
    time.sleep(DEFAULT_DELAY)

def go_backward():
    """Go backward in the select chain (Alt+Left)"""
    logging.info("Going backward in select chain")
    pyautogui.hotkey('alt', 'left')
    time.sleep(DEFAULT_DELAY)

def go_forward():
    """Go forward in the select chain (Alt+Right)"""
    logging.info("Going forward in select chain")
    pyautogui.hotkey('alt', 'right')
    time.sleep(DEFAULT_DELAY)
