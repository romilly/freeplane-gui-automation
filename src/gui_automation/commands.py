#!/usr/bin/env python3
"""
Freeplane Commands Library

A comprehensive set of functions for automating Freeplane mind mapping software using keyboard shortcuts.
Each function sends the appropriate keystrokes to control Freeplane.
This script assumes that a mind map is already open in Freeplane.

Requirements:
- xdotool
- pyautogui
"""

import time
import pyautogui
import subprocess
import random
import logging

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
                
                # Check if this is a Freeplane mind map window
                if "Freeplane" in window_title and "Mind map mode" in window_title:
                    found_window_id = window_id
                    logging.info(f"Found Freeplane mind map window: '{window_title}'")
                    break
            except:
                continue
        
        if not found_window_id:
            logging.warning("No Freeplane windows found with 'Freeplane' and 'Mind map mode' in the title.")
            return None
        
        # Activate the window
        subprocess.run(["xdotool", "windowactivate", found_window_id], check=True)
        
        return found_window_id
    
    except Exception as e:
        logging.error(f"Error finding Freeplane window: {e}")
        return None

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
            time.sleep(0.05 + random.random() * 0.15)
    else:
        pyautogui.write(text)

#----------------------------------------
# File Menu Commands
#----------------------------------------

def new_map():
    """Create a new mind map (Ctrl+N) and ensure focus is on the new map"""
    logging.info("Creating new map")
    
    # Get current window title before creating new map
    window_id = find_freeplane_window()
    if not window_id:
        logging.warning("No Freeplane window found before creating new map")
        return False
    
    # Get the current window title
    old_title = subprocess.check_output(
        ["xdotool", "getwindowname", window_id], 
        text=True
    ).strip()
    logging.info(f"Current window before new map: '{old_title}'")
    
    # Create the new map
    pyautogui.hotkey('ctrl', 'n')
    time.sleep(1)  # Wait for the new map to be created
    
    # Try to find the new window and verify if it's different
    window_id = find_freeplane_window()
    if not window_id:
        logging.warning("Couldn't find Freeplane window after creating new map")
        return False
    
    # Get the new window title
    new_title = subprocess.check_output(
        ["xdotool", "getwindowname", window_id], 
        text=True
    ).strip()
    logging.info(f"Window after new map creation: '{new_title}'")
    
    # If the title hasn't changed, we need to switch to the new tab
    if new_title == old_title:
        logging.info("New map created but focus is still on old map. Switching tabs...")
        
        # Try tab navigation first (up to 5 tabs)
        for _ in range(5):
            pyautogui.hotkey('ctrl', 'tab')
            time.sleep(0.5)
            
            # Check if window title changed
            window_id = find_freeplane_window()
            if not window_id:
                continue
                
            current_title = subprocess.check_output(
                ["xdotool", "getwindowname", window_id], 
                text=True
            ).strip()
            
            if current_title != old_title:
                logging.info(f"Successfully switched to new map: '{current_title}'")
                return True
        
        logging.warning("Could not switch to new map after multiple attempts")
        return False
    
    logging.info("New map created and focused successfully")
    return True
    
def save_map():
    """Save the current map (Ctrl+S)"""
    logging.info("Saving map")
    pyautogui.hotkey('ctrl', 's')
    
def _save_map_as():
    """Save the map as (Ctrl+Shift+S)"""
    logging.info("Save map as")
    pyautogui.hotkey('ctrl', 'shift', 's')


def save_map_as(filepath):
    """
    Save the map as with the specified filepath.
    Handles the full dialog interaction.

    Args:
        filepath (str): The full path or filename to save the map as
    """
    logging.info(f"Saving map as '{filepath}'")

    # First trigger the Save As dialog
    _save_map_as()
    time.sleep(1.0)  # Wait for dialog to appear

    # Extract just the filename from the path if a full path is provided
    if '/' in filepath:
        filename = filepath.split('/')[-1]
    else:
        filename = filepath

    # Make sure filename has .mm extension if not already present
    if not filename.lower().endswith('.mm'):
        filename += '.mm'

    # Clear any existing filename in the field and enter the new one
    for _ in range(50):  # Safe number of backspaces to clear field
        pyautogui.press('backspace')
    time.sleep(0.2)

    # Type the filename
    type_text(filename, human_like=False)  # Faster typing for filenames
    time.sleep(0.5)

    # If a directory was specified, we'd need to navigate to it
    # This would require additional logic to handle directory navigation
    # For now, we'll just use the default directory

    # Press the Save button
    pyautogui.press('tab')  # Ensure focus is on the Save button
    time.sleep(0.3)
    pyautogui.press('enter')  # Click the Save button

    # Wait for the save operation to complete
    time.sleep(1.0)

    # Check for overwrite confirmation dialog and handle it
    try:
        # Try to detect if an overwrite confirmation dialog appeared
        # This is a simple approach; might need adjusting based on the actual dialog
        window_text = subprocess.check_output(
            ["xdotool", "getactivewindow", "getwindowname"],
            text=True
        ).strip()

        if "already exists" in window_text.lower() or "confirm" in window_text.lower():
            logging.info("Overwrite confirmation dialog detected")
            pyautogui.press('enter')  # Confirm overwrite
            time.sleep(0.5)
    except Exception as e:
        logging.debug(f"No overwrite dialog detected: {e}")

    logging.info(f"Map saved as '{filename}'")
    return True
    
def open_map():
    """Open a saved map (Ctrl+O)"""
    logging.info("Opening map")
    pyautogui.hotkey('ctrl', 'o')
    
def print_map():
    """Print the map (Ctrl+P)"""
    logging.info("Print map")
    pyautogui.hotkey('ctrl', 'p')
    
def close_current_map():
    """Close the current map (Ctrl+W)"""
    logging.info("Closing current map")
    pyautogui.hotkey('ctrl', 'w')
    
def quit_freeplane():
    """Quit Freeplane (Ctrl+Q)"""
    logging.info("Quitting Freeplane")
    pyautogui.hotkey('ctrl', 'q')

#----------------------------------------
# Edit Menu Commands
#----------------------------------------

def add_remove_cloud():
    """Add or remove a cloud (Ctrl+Shift+B)"""
    logging.info("Add/remove cloud")
    pyautogui.hotkey('ctrl', 'shift', 'b')
    
def connect_nodes():
    """Connect nodes (Ctrl+L)"""
    logging.info("Connect nodes")
    pyautogui.hotkey('ctrl', 'l')
    
def remove_node():
    """Remove node (Delete)"""
    logging.info("Remove node")
    pyautogui.press('delete')
    
def undo():
    """Undo (Ctrl+Z)"""
    logging.info("Undo")
    pyautogui.hotkey('ctrl', 'z')
    
def redo():
    """Redo (Ctrl+Y)"""
    logging.info("Redo")
    pyautogui.hotkey('ctrl', 'y')
    
def cut():
    """Cut (Ctrl+X)"""
    logging.info("Cut")
    pyautogui.hotkey('ctrl', 'x')
    
def copy():
    """Copy (Ctrl+C)"""
    logging.info("Copy")
    pyautogui.hotkey('ctrl', 'c')
    
def paste():
    """Paste (Ctrl+V)"""
    logging.info("Paste")
    pyautogui.hotkey('ctrl', 'v')
    
def paste_as():
    """Paste as (Ctrl+Shift+V)"""
    logging.info("Paste as")
    pyautogui.hotkey('ctrl', 'shift', 'v')
    
def paste_clone():
    """Paste clone (Ctrl+D)"""
    logging.info("Paste clone")
    pyautogui.hotkey('ctrl', 'd')
    
def reset_node_position():
    """Reset node position (Ctrl+R)"""
    logging.info("Reset node position")
    pyautogui.hotkey('ctrl', 'r')

#----------------------------------------
# New Node Commands
#----------------------------------------

def new_child_node():
    """Create a new child node (Insert)"""
    logging.info("New child node")
    pyautogui.press('insert')
    
def new_sibling_node():
    """Create a new sibling node (Enter)"""
    logging.info("New sibling node")
    pyautogui.press('enter')
    
def new_previous_sibling_node():
    """Create a new previous sibling node (Shift+Enter)"""
    logging.info("New previous sibling node")
    pyautogui.hotkey('shift', 'enter')
    
def new_parent_node():
    """Create a new parent node (Shift+Insert)"""
    logging.info("New parent node")
    pyautogui.hotkey('shift', 'insert')
    
def new_summary_node():
    """Create a new summary node for selected nodes (Alt+Shift+Insert)"""
    logging.info("New summary node")
    pyautogui.hotkey('alt', 'shift', 'insert')

#----------------------------------------
# Link Commands
#----------------------------------------

def add_hyperlink():
    """Add hyperlink (Ctrl+Shift+K)"""
    logging.info("Add hyperlink")
    pyautogui.hotkey('ctrl', 'shift', 'k')


def _add_modify_hyperlink():
    """Add or modify hyperlink with type (Ctrl+K) - Internal function"""
    logging.info("Opening add or modify hyperlink dialog")
    pyautogui.hotkey('ctrl', 'k')


def add_modify_hyperlink(url):
    """
    Add or modify a hyperlink with the specified URL.
    Handles the full dialog interaction.

    Args:
        url (str): The URL for the hyperlink
    """
    logging.info(f"Adding hyperlink with URL: '{url}'")

    # First trigger the hyperlink dialog
    _add_modify_hyperlink()
    time.sleep(0.8)  # Wait for dialog to appear

    # Clear any existing URL in the field
    pyautogui.hotkey('ctrl', 'a')  # Select all text
    time.sleep(0.2)
    pyautogui.press('delete')  # Delete selected text
    time.sleep(0.2)

    # Type the URL
    type_text(url, human_like=False)  # Faster typing for URLs
    time.sleep(0.3)

    # Press the OK button
    pyautogui.press('tab')  # Ensure focus is on the OK button
    time.sleep(0.2)
    pyautogui.press('enter')  # Click the OK button

    # Wait for the operation to complete
    time.sleep(0.5)

    logging.info(f"Hyperlink '{url}' added")
    return True
    
def add_local_hyperlink():
    """Add local hyperlink (Alt+Shift+L)"""
    logging.info("Add local hyperlink")
    pyautogui.hotkey('alt', 'shift', 'l')
    
def follow_link():
    """Follow link (Ctrl+Enter)"""
    logging.info("Follow link")
    pyautogui.hotkey('ctrl', 'enter')

#----------------------------------------
# Node Core Commands
#----------------------------------------

def edit_node_core_inline():
    """Edit node core in-line (F2)"""
    logging.info("Edit node core in-line")
    pyautogui.press('f2')
    
def edit_node_core_dialog():
    """Edit node core in dialog (Alt+Enter)"""
    logging.info("Edit node core in dialog")
    pyautogui.hotkey('alt', 'enter')
    
def split_node():
    """Split node (Alt+S)"""
    logging.info("Split node")
    pyautogui.hotkey('alt', 's')
    
def join_nodes():
    """Join nodes with \\n (Ctrl+J)"""
    logging.info("Join nodes")
    pyautogui.hotkey('ctrl', 'j')
    
def format_bold():
    """Format text as bold (Ctrl+B)"""
    logging.info("Bold formatting")
    pyautogui.hotkey('ctrl', 'b')
    
def format_italic():
    """Format text as italic (Ctrl+I)"""
    logging.info("Italic formatting")
    pyautogui.hotkey('ctrl', 'i')
    
def larger_font():
    """Increase font size (Ctrl+Plus)"""
    logging.info("Larger font")
    pyautogui.hotkey('ctrl', 'plus')
    
def smaller_font():
    """Decrease font size (Ctrl+Minus)"""
    logging.info("Smaller font")
    pyautogui.hotkey('ctrl', 'minus')
    
def node_color():
    """Change node color (Alt+Shift+F)"""
    logging.info("Change node color")
    pyautogui.hotkey('alt', 'shift', 'f')
    
def node_background_color():
    """Change node background color (Alt+B)"""
    logging.info("Change node background color")
    pyautogui.hotkey('alt', 'b')
    
def use_plain_text():
    """Use plain text (Alt+Shift+P)"""
    logging.info("Use plain text")
    pyautogui.hotkey('alt', 'shift', 'p')

#----------------------------------------
# Node Properties Commands
#----------------------------------------

def edit_node_details_inline():
    """Edit node details in-line (F3)"""
    logging.info("Edit node details in-line")
    pyautogui.press('f3')
    
def edit_node_details_dialog():
    """Edit node details in dialog (Ctrl+F3)"""
    logging.info("Edit node details in dialog")
    pyautogui.hotkey('ctrl', 'f3')
    
def edit_attribute_inline():
    """Edit attribute in-line (Alt+F9)"""
    logging.info("Edit attribute in-line")
    pyautogui.hotkey('alt', 'f9')

#----------------------------------------
# Note Commands
#----------------------------------------

def display_note_panel():
    """Display note panel (Ctrl+Greater)"""
    logging.info("Display note panel")
    pyautogui.hotkey('ctrl', 'greater')
    
def note_edit_switch():
    """Note Edit Switch (Ctrl+Less)"""
    logging.info("Note edit switch")
    pyautogui.hotkey('ctrl', 'less')

#----------------------------------------
# Format Commands
#----------------------------------------

def copy_format():
    """Copy format of a node (Alt+Shift+C)"""
    logging.info("Copy format")
    pyautogui.hotkey('alt', 'shift', 'c')
    
def paste_format():
    """Paste format to a node (Alt+Shift+V)"""
    logging.info("Paste format")
    pyautogui.hotkey('alt', 'shift', 'v')
    
def redefine_style():
    """Redefine style (Alt+R)"""
    logging.info("Redefine style")
    pyautogui.hotkey('alt', 'r')
    
def copy_map_style():
    """Copy map style from (Ctrl+Shift+O)"""
    logging.info("Copy map style")
    pyautogui.hotkey('ctrl', 'shift', 'o')
    
def edit_styles():
    """Edit styles (Ctrl+F11)"""
    logging.info("Edit styles")
    pyautogui.hotkey('ctrl', 'f11')

#----------------------------------------
# View Commands
#----------------------------------------

def full_screen_mode():
    """Toggle full screen mode (F11)"""
    logging.info("Toggle full screen mode")
    pyautogui.press('f11')

#----------------------------------------
# Navigate Commands
#----------------------------------------

def previous_map():
    """Go to previous map (Ctrl+Shift+Tab)"""
    logging.info("Go to previous map")
    pyautogui.hotkey('ctrl', 'shift', 'tab')
    
def next_map():
    """Go to next map (Ctrl+Tab)"""
    logging.info("Go to next map")
    pyautogui.hotkey('ctrl', 'tab')
    
def select_all_visible_nodes():
    """Select all visible nodes (Ctrl+A)"""
    logging.info("Select all visible nodes")
    pyautogui.hotkey('ctrl', 'a')
    
def select_visible_branch():
    """Select visible branch (Ctrl+Shift+A)"""
    logging.info("Select visible branch")
    pyautogui.hotkey('ctrl', 'shift', 'a')
    
def goto_root():
    """Go to root node (Escape)"""
    logging.info("Go to root")
    pyautogui.press('escape')
    
def goto_previous_node():
    """Go to previous node (Ctrl+Alt+Left)"""
    logging.info("Go to previous node")
    pyautogui.hotkey('ctrl', 'alt', 'left')
    
def goto_next_node():
    """Go to next node (Ctrl+Alt+Right)"""
    logging.info("Go to next node")
    pyautogui.hotkey('ctrl', 'alt', 'right')
    
def goto_previous_node_fold():
    """Go to previous node (fold) (Ctrl+Shift+Left)"""
    logging.info("Go to previous node (fold)")
    pyautogui.hotkey('ctrl', 'shift', 'left')
    
def goto_next_node_fold():
    """Go to next node (fold) (Ctrl+Shift+Right)"""
    logging.info("Go to next node (fold)")
    pyautogui.hotkey('ctrl', 'shift', 'right')
    
def go_backward():
    """Go backward in the select chain (Alt+Left)"""
    logging.info("Go backward")
    pyautogui.hotkey('alt', 'left')
    
def go_forward():
    """Go forward in the select chain (Alt+Right)"""
    logging.info("Go forward")
    pyautogui.hotkey('alt', 'right')

#----------------------------------------
# Fold Commands
#----------------------------------------

def unfold():
    """Unfold node (Space)"""
    logging.info("Unfold node")
    pyautogui.press('space')
    
def show_next_child():
    """Show next child (Shift+Space)"""
    logging.info("Show next child")
    pyautogui.hotkey('shift', 'space')
    
def unfold_children():
    """Unfold children (Ctrl+Space)"""
    logging.info("Unfold children")
    pyautogui.hotkey('ctrl', 'space')
    
def unfold_one_level():
    """Unfold one level (Alt+Page Down)"""
    logging.info("Unfold one level")
    pyautogui.hotkey('alt', 'pagedown')
    
def fold_one_level():
    """Fold one level (Alt+Page Up)"""
    logging.info("Fold one level")
    pyautogui.hotkey('alt', 'pageup')
    
def unfold_all():
    """Unfold all (Alt+End)"""
    logging.info("Unfold all")
    pyautogui.hotkey('alt', 'end')
    
def fold_all():
    """Fold all (Alt+Home)"""
    logging.info("Fold all")
    pyautogui.hotkey('alt', 'home')

#----------------------------------------
# Presentation Commands
#----------------------------------------

def run_presentation():
    """Run presentation / Next slide (F5)"""
    logging.info("Run presentation / Next slide")
    pyautogui.press('f5')
    
def stop_presentation():
    """Stop presentation (Shift+F5)"""
    logging.info("Stop presentation")
    pyautogui.hotkey('shift', 'f5')
    
def previous_slide():
    """Go to previous slide (Ctrl+F5)"""
    logging.info("Previous slide")
    pyautogui.hotkey('ctrl', 'f5')

#----------------------------------------
# Tools Commands
#----------------------------------------

def manage_time():
    """Manage time (Ctrl+T)"""
    logging.info("Manage time")
    pyautogui.hotkey('ctrl', 't')
    
def clear_dependencies():
    """Clear dependencies (Alt+F6)"""
    logging.info("Clear dependencies")
    pyautogui.hotkey('alt', 'f6')
    
def trace_precedents():
    """Trace precedents (Alt+F7)"""
    logging.info("Trace precedents")
    pyautogui.hotkey('alt', 'f7')
    
def trace_dependents():
    """Trace dependents (Alt+F8)"""
    logging.info("Trace dependents")
    pyautogui.hotkey('alt', 'f8')
    
def preferences():
    """Open preferences (Ctrl+Comma)"""
    logging.info("Open preferences")
    pyautogui.hotkey('ctrl', 'comma')

#----------------------------------------
# Maps Modes Commands
#----------------------------------------

def mind_map_editor():
    """Switch to mind map editor (Alt+1)"""
    logging.info("Switch to mind map editor")
    pyautogui.hotkey('alt', '1')
    
def file_explorer():
    """Switch to file explorer (Alt+3)"""
    logging.info("Switch to file explorer")
    pyautogui.hotkey('alt', '3')

#----------------------------------------
# Help Commands
#----------------------------------------

def documentation():
    """Open documentation (F1)"""
    logging.info("Open documentation")
    pyautogui.press('f1')

# Define __all__ for better import control
__all__ = [
    'find_freeplane_window',
    'type_text',
    'new_map',
    'save_map',
    '_save_map_as',
    'save_map_as',
    'open_map',
    'print_map',
    'close_current_map',
    'quit_freeplane',
    'add_remove_cloud',
    'connect_nodes',
    'remove_node',
    'undo',
    'redo',
    'cut',
    'copy',
    'paste',
    'paste_as',
    'paste_clone',
    'reset_node_position',
    'new_child_node',
    'new_sibling_node',
    'new_previous_sibling_node',
    'new_parent_node',
    'new_summary_node',
    'add_hyperlink',
    '_add_modify_hyperlink',
    'add_modify_hyperlink',
    'add_local_hyperlink',
    'follow_link',
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
    'use_plain_text',
    'edit_node_details_inline',
    'edit_node_details_dialog',
    'edit_attribute_inline',
    'display_note_panel',
    'note_edit_switch',
    'copy_format',
    'paste_format',
    'redefine_style',
    'copy_map_style',
    'edit_styles',
    'full_screen_mode',
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
    'go_forward',
    'unfold',
    'show_next_child',
    'unfold_children',
    'unfold_one_level',
    'fold_one_level',
    'unfold_all',
    'fold_all',
    'run_presentation',
    'stop_presentation',
    'previous_slide',
    'manage_time',
    'clear_dependencies',
    'trace_precedents',
    'trace_dependents',
    'preferences',
    'mind_map_editor',
    'file_explorer',
    'documentation'
]
