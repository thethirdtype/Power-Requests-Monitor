import tkinter as tk
from tkinter import Scrollbar
import subprocess
import sys
import ctypes


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


def get_powercfg_requests():
    try:
        result = subprocess.check_output(['powercfg', '/requests'], text=True)
        return result
    except Exception as e:
        return f"Error: {e}"


def refresh_powercfg_requests():
    output_text.delete(1.0, tk.END)
    result = get_powercfg_requests()
    # Insert the result with the specified text color
    output_text.insert(tk.END, result, "text_color")


def is_dark_mode():
    try:
        # Check the system-wide color preferences using SystemParametersInfoW
        SPI_GETCLIENTAREAANIMATION = 0x1042
        ui_param = ctypes.c_uint(0)
        pv_param = ctypes.c_uint(0)
        ctypes.windll.user32.SystemParametersInfoW(SPI_GETCLIENTAREAANIMATION, 0, ctypes.byref(ui_param), 0)
        return ui_param.value == 1
    except Exception as e:
        print(f"Error detecting dark mode: {e}")
        return None


# Check if running with admin privileges
if is_admin():
    # Create the main window
    root = tk.Tk()
    root.title("Power Requests Monitor")

    # Set initial window size
    window_width = 800
    window_height = 600
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x_coordinate = (screen_width - window_width) // 2
    y_coordinate = (screen_height - window_height) // 2

    root.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")

    # Check if dark mode is enabled
    dark_mode = is_dark_mode()

    # Set window colors based on dark mode
    if dark_mode is not None and dark_mode:
        root.configure(bg="#2C2C2C")  # Dark background color
        refresh_button_bg_color = "#383838"  # Dark button color
        refresh_button_fg_color = "#FFFFFF"  # Dark button foreground color
        text_widget_bg_color = "#191919"  # Dark text widget background color
        text_widget_fg_color = "#8FD139"  # Dark text widget foreground color
    else:
        # Use default light mode colors
        refresh_button_bg_color = None
        refresh_button_fg_color = None
        text_widget_bg_color = None
        text_widget_fg_color = None

    # Create a Refresh button
    refresh_button = tk.Button(root, text="Refresh", command=refresh_powercfg_requests,
                               bg=refresh_button_bg_color, fg=refresh_button_fg_color)
    refresh_button.pack(pady=10)

    # Create a text widget to display the output with a vertical scrollbar
    output_text = tk.Text(root, wrap=tk.WORD, bg=text_widget_bg_color, fg=text_widget_fg_color)
    output_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    scrollbar = Scrollbar(root, command=output_text.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    output_text.config(yscrollcommand=scrollbar.set)

    # Populate the text widget initially
    refresh_powercfg_requests()

    # Set Icon
    root.iconbitmap("prm_icon.ico")

    # Run the Tkinter event loop
    root.mainloop()
else:
    # If not running with admin privileges, request elevation
    try:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, ' '.join(sys.argv), None, 1)
    except Exception as e:
        print(e)
