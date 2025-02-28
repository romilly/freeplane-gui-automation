"""
Common utilities and functions used across the Freeplane automation commands.
"""

import time
import random
import logging
import subprocess
import pyautogui

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

# Constants
DEFAULT_DELAY = 0.2  # Default delay between actions in seconds

def find_freeplane_window():
    """
    Find and activate the Freeplane mind map window.
    Returns the window ID if found, None otherwise.
    """
    try:
        # Get all window IDs
        all_windows = subprocess.check_output(
            ["xdotool", "search", "--all", "--onlyvisible", "--name", "."], 
            text=True
        ).strip().split('\n')
        
        found_window_id = None
        
        # Check each window for Freeplane mind map title
        for window_id in all_windows:
            if not window_id:
                continue
                
            try:
                window_title = subprocess.check_output(
                    ["xdotool", "getwindowname", window_id], 
                    text=True
                ).strip()
                
                if "Freeplane -" in window_title:
                    found_window_id = window_id
                    break
            except subprocess.CalledProcessError:
                continue
        
        if found_window_id:
            # Activate the window
            subprocess.run(["xdotool", "windowactivate", found_window_id])
            time.sleep(DEFAULT_DELAY)
            return True
            
    except subprocess.CalledProcessError:
        pass
        
    return False

def type_text(text, human_like=True):
    """
    Type text with optional human-like delays between keystrokes.
    
    Args:
        text (str): The text to type
        human_like (bool): If True, adds random delays between keystrokes
    """
    if human_like:
        for char in text:
            pyautogui.write(char)
            time.sleep(random.uniform(0.05, 0.15))
    else:
        pyautogui.write(text)
    time.sleep(DEFAULT_DELAY)
