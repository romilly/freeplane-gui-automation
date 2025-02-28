#!/usr/bin/env python3
"""
Freeplane Branch Creation Script
This script finds an open Freeplane window, creates a new branch,
and adds text to it.
"""

import time
import pyautogui
import subprocess
import re
import random

def find_freeplane_window():
    """
    Find the Freeplane window using xdotool and activate it.
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
                
                # Check if this is a Freeplane mind map window
                if "Freeplane" in window_title and "Mind map mode" in window_title:
                    found_window_id = window_id
                    print(f"Found Freeplane mind map window: '{window_title}'")
                    break
            except:
                continue
        
        if not found_window_id:
            print("No Freeplane windows found with 'Freeplane' and 'Mind map mode' in the title. Make sure Freeplane is running with a map open.")
            return None
        
        # Activate the window
        subprocess.run(["xdotool", "windowactivate", found_window_id], check=True)
        
        return found_window_id
    
    except subprocess.CalledProcessError as e:
        print(f"Error finding Freeplane window: {e}")
        return None
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None

def create_new_branch(text="Claude is amazing"):
    """
    Creates a new branch in Freeplane and adds the specified text.
    """
    try:
        # Find and focus the Freeplane window
        window_id = find_freeplane_window()
        if not window_id:
            return False
        
        # Give the window a moment to get focus
        time.sleep(0.5)
        
        # Press Enter to create a new branch
        print("Creating new branch...")
        pyautogui.press('enter')
        
        # Wait a moment for the node to be ready for editing
        time.sleep(0.5)
        
        # Type the text with realistic typing speed
        print(f"Typing: '{text}'")
        for char in text:
            # Type each character with a slight random delay
            pyautogui.write(char)
            # Random delay between 0.05 and 0.2 seconds for realistic typing
            time.sleep(0.05 + random.random() * 0.15)
        
        # Press Enter to confirm
        time.sleep(0.5)
        pyautogui.press('enter')
        
        print("Branch created successfully!")
        return True
        
    except Exception as e:
        print(f"Error creating branch: {e}")
        return False

if __name__ == "__main__":
    # Check if required tools are available
    try:
        # Check for xdotool
        subprocess.check_output(["which", "xdotool"])
    except subprocess.CalledProcessError:
        print("Error: xdotool is not installed. Install it with: sudo apt install xdotool")
        exit(1)
    
    # Check for pyautogui
    try:
        import pyautogui
    except ImportError:
        print("PyAutoGUI is not installed. Please install it with: pip install pyautogui")
        exit(1)
    
    # Create the branch
    create_new_branch()
