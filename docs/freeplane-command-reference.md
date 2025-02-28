# Freeplane Commands Reference

This document provides a reference for Freeplane keyboard shortcuts and their corresponding Python functions from the automation library.

## File Menu Commands

| Command | Keyboard Shortcut | Python Function |
|---------|-------------------|-----------------|
| New map | Ctrl+N | `new_map()` |
| Save map | Ctrl+S | `save_map()` |
| Save map as... | Ctrl+Shift+S | `save_map_as()` |
| Open saved map... | Ctrl+O | `open_map()` |
| Print map... | Ctrl+P | `print_map()` |
| Close current map | Ctrl+W | `close_current_map()` |
| Quit Freeplane | Ctrl+Q | `quit_freeplane()` |

## Edit Menu Commands

| Command | Keyboard Shortcut | Python Function |
|---------|-------------------|-----------------|
| Add/remove cloud (default) | Ctrl+Shift+B | `add_remove_cloud()` |
| Connect | Ctrl+L | `connect_nodes()` |
| Remove node | Delete | `remove_node()` |
| Undo | Ctrl+Z | `undo()` |
| Redo | Ctrl+Y | `redo()` |
| Cut | Ctrl+X | `cut()` |
| Copy | Ctrl+C | `copy()` |
| Paste | Ctrl+V | `paste()` |
| Paste as... | Ctrl+Shift+V | `paste_as()` |
| Paste Clone | Ctrl+D | `paste_clone()` |
| Reset node position | Ctrl+R | `reset_node_position()` |

## New Node Commands

| Command | Keyboard Shortcut | Python Function |
|---------|-------------------|-----------------|
| New child node | Insert | `new_child_node()` |
| New sibling node | Enter | `new_sibling_node()` |
| New previous sibling node | Shift+Enter | `new_previous_sibling_node()` |
| New parent node | Shift+Insert | `new_parent_node()` |
| New summary node (selected nodes) | Alt+Shift+Insert | `new_summary_node()` |

## Link Commands

| Command | Keyboard Shortcut | Python Function |
|---------|-------------------|-----------------|
| Add hyperlink (choose)... | Ctrl+Shift+K | `add_hyperlink()` |
| Add or modify hyperlink (type)... | Ctrl+K | `add_modify_hyperlink()` |
| Add local hyperlink | Alt+Shift+L | `add_local_hyperlink()` |
| Follow link | Ctrl+Enter | `follow_link()` |

## Node Core Commands

| Command | Keyboard Shortcut | Python Function |
|---------|-------------------|-----------------|
| Edit node core in-line | F2 | `edit_node_core_inline()` |
| Edit node core in dialog | Alt+Enter | `edit_node_core_dialog()` |
| Split node | Alt+S | `split_node()` |
| Join nodes with "\n" | Ctrl+J | `join_nodes()` |
| Bold | Ctrl+B | `format_bold()` |
| Italic | Ctrl+I | `format_italic()` |
| Larger font | Ctrl+Plus | `larger_font()` |
| Smaller font | Ctrl+Minus | `smaller_font()` |
| Node color... | Alt+Shift+F | `node_color()` |
| Node background color... | Alt+B | `node_background_color()` |
| Use plain text | Alt+Shift+P | `use_plain_text()` |

## Node Properties Commands

| Command | Keyboard Shortcut | Python Function |
|---------|-------------------|-----------------|
| Edit node details in-line | F3 | `edit_node_details_inline()` |
| Edit node details in dialog | Ctrl+F3 | `edit_node_details_dialog()` |
| Edit attribute in-line | Alt+F9 | `edit_attribute_inline()` |

## Note Commands

| Command | Keyboard Shortcut | Python Function |
|---------|-------------------|-----------------|
| Display note panel | Ctrl+Greater | `display_note_panel()` |
| Note Edit Switch | Ctrl+Less | `note_edit_switch()` |

## Format Commands

| Command | Keyboard Shortcut | Python Function |
|---------|-------------------|-----------------|
| Copy format | Alt+Shift+C | `copy_format()` |
| Paste format | Alt+Shift+V | `paste_format()` |
| Redefine style | Alt+R | `redefine_style()` |
| Copy map style from... | Ctrl+Shift+O | `copy_map_style()` |
| Edit styles | Ctrl+F11 | `edit_styles()` |

## View Commands

| Command | Keyboard Shortcut | Python Function |
|---------|-------------------|-----------------|
| Full screen mode | F11 | `full_screen_mode()` |

## Navigate Commands

| Command | Keyboard Shortcut | Python Function |
|---------|-------------------|-----------------|
| Previous map | Ctrl+Shift+Tab | `previous_map()` |
| Next map | Ctrl+Tab | `next_map()` |
| Select all visible nodes | Ctrl+A | `select_all_visible_nodes()` |
| Select visible branch | Ctrl+Shift+A | `select_visible_branch()` |
| Goto root | Escape | `goto_root()` |
| Goto previous node | Ctrl+Alt+Left | `goto_previous_node()` |
| Goto next node | Ctrl+Alt+Right | `goto_next_node()` |
| Goto previous node (fold) | Ctrl+Shift+Left | `goto_previous_node_fold()` |
| Goto next node (fold) | Ctrl+Shift+Right | `goto_next_node_fold()` |
| Go backward | Alt+Left | `go_backward()` |
| Go forward | Alt+Right | `go_forward()` |

## Fold Commands

| Command | Keyboard Shortcut | Python Function |
|---------|-------------------|-----------------|
| (Un)fold | Space | `unfold()` |
| Show next child | Shift+Space | `show_next_child()` |
| (Un)fold children | Ctrl+Space | `unfold_children()` |
| Unfold one level | Alt+Page Down | `unfold_one_level()` |
| Fold one level | Alt+Page Up | `fold_one_level()` |
| Unfold all | Alt+End | `unfold_all()` |
| Fold all | Alt+Home | `fold_all()` |

## Presentation Commands

| Command | Keyboard Shortcut | Python Function |
|---------|-------------------|-----------------|
| Run presentation/Next slide | F5 | `run_presentation()` |
| Stop presentation | Shift+F5 | `stop_presentation()` |
| Previous slide | Ctrl+F5 | `previous_slide()` |

## Tools Commands

| Command | Keyboard Shortcut | Python Function |
|---------|-------------------|-----------------|
| Manage time... | Ctrl+T | `manage_time()` |
| Clear dependencies | Alt+F6 | `clear_dependencies()` |
| Trace Precedents | Alt+F7 | `trace_precedents()` |
| Trace Dependents | Alt+F8 | `trace_dependents()` |
| Preferences... | Ctrl+Comma | `preferences()` |

## Maps Modes Commands

| Command | Keyboard Shortcut | Python Function |
|---------|-------------------|-----------------|
| Mind map editor | Alt+1 | `mind_map_editor()` |
| File explorer | Alt+3 | `file_explorer()` |

## Help Commands

| Command | Keyboard Shortcut | Python Function |
|---------|-------------------|-----------------|
| Documentation | F1 | `documentation()` |

## Utility Functions

| Function | Description |
|----------|-------------|
| `find_freeplane_window()` | Finds and activates the Freeplane window |
| `type_text(text, human_like=True)` | Types text with optional human-like delays |
| `demo_create_simple_mindmap()` | Creates a sample mind map (demonstration) |
