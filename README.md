# File Content Aggregator

A Python utility that allows users to select and combine the contents of multiple files into a single output file.

## Features

- Select multiple files with an intuitive file dialog
- Filter files by type (C/C++, Python, Text, JavaScript, HTML, CSS, and more)
- Combine all selected file contents into a single output file
- Each file's content is clearly separated with headers
- Choose your own output file location

## Installation

1. **Install Python**:
   - Windows: Download and install from [python.org](https://www.python.org/downloads/)
   - macOS: `brew install python` (using Homebrew) or download from [python.org](https://www.python.org/downloads/)
   - Linux: `sudo apt install python3` (Ubuntu/Debian) or `sudo dnf install python3` (Fedora)

2. No additional dependencies required beyond Python's standard library.

## Usage

Run the script from your terminal:

```
python3 file_aggregator.py
```

Follow the interactive prompts to:
1. Select input files
2. Choose an output file location
3. View the success message when processing is complete

## How It Works

The script:
1. Opens a file selection dialog with customizable type filters
2. Allows you to select an output file location
3. Processes each selected file and combines their contents
4. Separates each file's content with a header: `// filename.extension`
5. Handles encoding issues gracefully

