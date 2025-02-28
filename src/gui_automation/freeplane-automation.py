#!/usr/bin/env python3
"""
Freeplane Automation Script for Linux X11
This script starts Freeplane and creates a new mind map using Ctrl+N.
"""

import subprocess
import time
import pyautogui
import os

def start_freeplane_and_create_map():
    """
    Start Freeplane and create a new mind map using keyboard shortcuts.
    
    Requires:
    - Freeplane to be installed
    - PyAutoGUI package (pip install pyautogui)
    - X11 display server running
    """
    print("Starting Freeplane...")
    
    # Start Freeplane (adjust path if needed)
    try:
        # Common locations for Freeplane executable
        possible_paths = [
            "freeplane",  # If in PATH
            "/usr/bin/freeplane",
            "/usr/local/bin/freeplane",
            os.path.expanduser("~/Freeplane/freeplane.sh")
        ]
        
        # Try to find and run Freeplane
        for path in possible_paths:
            try:
                subprocess.Popen([path])
                break
            except (FileNotFoundError, PermissionError):
                if path == possible_paths[-1]:
                    raise Exception("Could not find Freeplane executable. Please provide the correct path.")
                continue
                
        # Wait for Freeplane to start
        print("Waiting for Freeplane to start...")
        time.sleep(5)  # Adjust time as needed for your system
        
        # Create a new map with Ctrl+N
        print("Creating a new map with Ctrl+N...")
        pyautogui.hotkey('ctrl', 'n')
        
        print("New mind map created successfully!")
        
    except Exception as e:
        print(f"Error: {e}")
        
if __name__ == "__main__":
    # Check if DISPLAY is set (X11 is running)
    if "DISPLAY" not in os.environ:
        print("Error: X11 display not found. Make sure X is running.")
        exit(1)
        
    # Check if pyautogui is installed
    try:
        import pyautogui
    except ImportError:
        print("PyAutoGUI is not installed. Please install it with: pip install pyautogui")
        exit(1)
        
    start_freeplane_and_create_map()
