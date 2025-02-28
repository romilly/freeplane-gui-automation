#!/usr/bin/env python3
"""
Demo script for Freeplane automation.
Shows how to use the freeplane_commands library to create a simple mind map.
"""

import time
import pyautogui
import logging
from gui_automation.commands import (
    find_freeplane_window, new_map, edit_node_core_inline,
    type_text, new_child_node, new_sibling_node, goto_root,
    format_bold, add_modify_hyperlink, save_map_as
)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

def demo_create_simple_mindmap():
    """
    Demo function that creates a simple mind map
    """
    # Find and focus Freeplane window
    if not find_freeplane_window():
        logging.error("Couldn't find Freeplane window. Exiting.")
        return False
    
    # Create a new mind map and ensure it has focus
    if not new_map():
        logging.error("Failed to create new map or switch to it. Exiting.")
        return False
    
    # A short delay to ensure UI is ready
    time.sleep(0.5)
    
    # Edit the central node
    edit_node_core_inline()
    time.sleep(0.5)
    
    # Clear existing text ("New Mindmap") by selecting all and deleting
    pyautogui.hotkey('ctrl', 'a')
    time.sleep(0.2)
    pyautogui.press('delete')
    time.sleep(0.2)
    
    # Type new text
    type_text("My Project Plan")
    pyautogui.press('enter')
    time.sleep(0.5)
    
    # Create first child node
    new_child_node()
    time.sleep(0.5)
    type_text("Tasks")
    pyautogui.press('enter')
    
    # Create child under Tasks
    new_child_node()
    time.sleep(0.5)
    type_text("Research")
    pyautogui.press('enter')
    
    # Create sibling
    new_sibling_node()
    time.sleep(0.5)
    type_text("Development")
    pyautogui.press('enter')
    
    # Create sibling
    new_sibling_node()
    time.sleep(0.5)
    type_text("Testing")
    pyautogui.press('enter')
    
    # Go back to root
    goto_root()
    time.sleep(0.5)
    
    # Create another main branch
    new_child_node()
    time.sleep(0.5)
    type_text("Timeline")
    pyautogui.press('enter')
    
    # Format it bold
    format_bold()
    
    # Create another main branch
    goto_root()
    time.sleep(0.5)
    new_child_node()
    time.sleep(0.5)
    type_text("Resources")
    pyautogui.press('enter')

    add_modify_hyperlink("https://www.freeplane.com")

    save_map_as('demo1.mm')
    
    logging.info("Simple mind map created successfully")
    return True

if __name__ == "__main__":
    # Run the demo
    demo_create_simple_mindmap()
