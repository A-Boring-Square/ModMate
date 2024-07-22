import tkinter as tk
from tkinter import ttk
import os
import subprocess
import sys


def RunTool(Path: str, Args: str):
    subprocess.Popen(["python", Path, Args])
    sys.exit(0)

def maximize_window(event):
    root.state('zoomed')  # Maximize the window

def adjust_widgets(event=None):
    # Adjust the position of the frame and its contents dynamically
    frame.update_idletasks()
    width = frame.winfo_width()
    height = frame.winfo_height()
    root_width = root.winfo_width()
    root_height = root.winfo_height()
    
    frame.place(x=(root_width - width) / 2, y=(root_height - height) / 2)

def main():
    global root, frame  # Declare global variables for use in event handlers
    
    root = tk.Tk()
    root.title("ModMateApp")
    
    # Load the Azure theme
    root.tk.call("source", os.path.join("Theme", "azure.tcl"))
    root.tk.call("set_theme", "dark")
    
    # Configure styles
    style = ttk.Style()
    style.configure('ToolButton.TButton', 
                    relief='flat', 
                    padding=10, 
                    font=('Helvetica', 12))
    style.map('ToolButton.TButton', 
              background=[('active', '#3a3a3a')])
    
    # Create a frame to hold the buttons
    frame = ttk.Frame(root, padding="10")
    frame.pack(expand=True, fill='both')
    
  # Define tools with corresponding commands
    tools = [
        ('Config Editor', lambda: RunTool(os.path.join("GameModding", "__main__.py"), "--config")),
        ('Memory Explorer', lambda: RunTool(os.path.join("GameModding", "__main__.py"), "--memory")),
        ('Pyinstaller Executable Code Injector', lambda: RunTool(os.path.join("PyinstallerTools", "__main__.py"), "--code_inject")),
        ('Pyinstaller Executable Extractor', lambda: RunTool(os.path.join("PyinstallerTools", "__main__.py"), "--extract")),
        ('Pyinstaller Executable Packer', lambda: RunTool(os.path.join("PyinstallerTools", "__main__.py"), "--pack")),
        ('Python Bytecode Patcher', lambda: RunTool(os.path.join("PythonTools", "__main__.py"), "--patch"))
    ]
    
    # Add buttons to the frame
    for tool_label, tool_command in tools:
        button = ttk.Button(frame, text=tool_label, command=tool_command, style='ToolButton.TButton')
        button.pack(pady=5, fill='x')
    
    # Center the buttons in the frame
    adjust_widgets()
    
    # Bind hotkey (Ctrl+M) to maximize window
    root.bind('<Control-m>', maximize_window)
    
    # Bind resize event to adjust widgets
    root.bind('<Configure>', adjust_widgets)
    
    root.geometry("500x400")  # Set the size of the window initially
    root.mainloop()

if __name__ == "__main__":
    main()
