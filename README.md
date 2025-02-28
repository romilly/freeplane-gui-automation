# Freeplane GUI Automation

A Python package for automating interactions with the Freeplane mind mapping software. This package provides programmatic control over Freeplane's functionality through Python scripts.

## Overview

This project enables automated control of Freeplane, allowing you to:
- Create and modify mind maps programmatically
- Automate repetitive mind mapping tasks
- Script complex mind map operations
- Integrate Freeplane operations into your Python workflows

## Features

The package provides Python functions that map to Freeplane's commands and keyboard shortcuts, including:
- File operations (new map, save, open, etc.)
- Node manipulation (add, remove, edit)
- Formatting and styling
- Link management
- Navigation controls
- View operations
- And many more...

## Documentation

Comprehensive documentation of available commands can be found in `docs/freeplane-command-reference.md`. This includes:
- Freeplane keyboard shortcuts
- Corresponding Python function names
- Command categorization (File, Edit, Node, etc.)

## Project Structure

```
gui-automation/
├── docs/
│   └── freeplane-command-reference.md
├── src/
│   └── gui_automation/
├── test/
└── data/
```

## Getting Started

### Prerequisites

- Python 3.x
- Freeplane mind mapping software installed and accessible
- xdotool (Linux utility for X11 automation)
- pyautogui Python package

### Installing Freeplane

Before installing this automation package, you'll need to have Freeplane installed on your system. 

1. Visit the [Freeplane Documentation](https://docs.freeplane.org/home.html) for detailed installation instructions
2. Download and install the latest version of Freeplane for your operating system
3. Verify the installation by running Freeplane and creating a test mind map

### Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/gui-automation.git
   cd gui-automation
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Linux/Mac
   # or
   # .\venv\Scripts\activate  # On Windows
   ```

3. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

4. Install xdotool (on Ubuntu/Debian):
   ```bash
   sudo apt-get install xdotool
   ```

Note: Remember to activate the virtual environment (`source venv/bin/activate`) each time you work on the project.

### Running the Demo

1. Start Freeplane on your system

2. Run the demo script:
   ```bash
   python src/gui_automation/demo.py
   ```

The demo will create a simple mind map with:
- A central "My Project Plan" node
- Three main branches: Tasks, Timeline, and Resources
- Sub-tasks under the Tasks branch
- A hyperlink in the Resources branch
- The final mind map will be saved as 'demo.mm'

You can also import and use the demo function in your own scripts:
```python
from gui_automation.demo import demo_create_simple_mindmap

demo_create_simple_mindmap()
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Development Notes

### Git LFS

This project uses Git Large File Storage (LFS) for handling large media files. All `.mp4` files are tracked using Git LFS.

If you plan to work with video files in this project:

1. Install Git LFS if you haven't already:
   ```bash
   # For Ubuntu/Debian
   sudo apt-get install git-lfs
   
   # For other systems, see https://git-lfs.com
   ```

2. Enable Git LFS in your local repository:
   ```bash
   git lfs install
   ```

After this setup, any `.mp4` files you add will automatically be handled by Git LFS.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
