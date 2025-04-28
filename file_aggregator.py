import tkinter as tk
from tkinter import filedialog, simpledialog, messagebox
import os

def select_files():
    """Opens a file dialog to select multiple files with improved file type filters."""
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    
    # Define file type options with specific extensions
    filetypes = [
        ("All Files", "*.*"),
        ("C/C++ Files", "*.c;*.h;*.cpp;*.hpp"),
        ("Python Files", "*.py"),
        ("Text Files", "*.txt"),
        ("JavaScript Files", "*.js"),
        ("HTML Files", "*.html;*.htm"),
        ("CSS Files", "*.css"),
        ("XML Files", "*.xml"),
        ("Markdown Files", "*.md"),
        ("JSON Files", "*.json")
    ]
    
    # Open file dialog to select multiple files
    file_paths = filedialog.askopenfilenames(
        title="Select files",
        filetypes=filetypes
    )
    
    root.destroy()
    return file_paths

def get_output_location():
    """Opens a dialog to select the output file location."""
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    
    # Open file dialog to select where to save the output file
    output_path = filedialog.asksaveasfilename(
        title="Save output file",
        initialfile="out.txt",
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt")]
    )
    
    root.destroy()
    return output_path

def process_files(file_paths, output_path):
    """Read contents of selected files and write to output file."""
    if not file_paths or not output_path:
        return False
    
    try:
        with open(output_path, 'w', encoding='utf-8') as out_file:
            for file_path in file_paths:
                filename = os.path.basename(file_path)
                
                # Write file separator with filename
                out_file.write(f"// {filename}\n\n")
                
                # Read and write file contents
                try:
                    with open(file_path, 'r', encoding='utf-8') as in_file:
                        content = in_file.read()
                        out_file.write(content)
                except UnicodeDecodeError:
                    # Try with a different encoding for binary files
                    try:
                        with open(file_path, 'r', encoding='latin-1') as in_file:
                            content = in_file.read()
                            out_file.write(content)
                    except Exception as e:
                        out_file.write(f"[Error reading file: {str(e)}]\n")
                except Exception as e:
                    out_file.write(f"[Error reading file: {str(e)}]\n")
                
                # Add an extra newline after each file's content
                out_file.write("\n\n")
        return True
    except Exception as e:
        messagebox.showerror("Error", f"Failed to write output file: {str(e)}")
        return False

def main():
    # Select input files
    file_paths = select_files()
    if not file_paths:
        messagebox.showinfo("Info", "No files selected. Exiting.")
        return
    
    # Get output location
    output_path = get_output_location()
    if not output_path:
        messagebox.showinfo("Info", "No output location selected. Exiting.")
        return
    
    # Process files
    success = process_files(file_paths, output_path)
    
    # Show completion message
    if success:
        messagebox.showinfo("Success", f"All file contents have been written to {output_path}")

if __name__ == "__main__":
    main()