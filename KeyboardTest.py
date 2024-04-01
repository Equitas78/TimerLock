import ctypes
import tkinter as tk


# Load the user32.dll library
user32 = ctypes.windll.user32
root = tk.Tk()

# Constants
VK_LWIN = 0x5B
VK_RWIN = 0x5C

# Function to block the Windows key
def block_windows_key():
    # Block the left Windows key
    user32.MapVirtualKeyW(VK_LWIN, 0)
    user32.MapVirtualKeyW(VK_LWIN, 0)

    # Block the right Windows key
    user32.MapVirtualKeyW(VK_RWIN, 0)
    user32.MapVirtualKeyW(VK_RWIN, 0)

# Function to unblock the Windows key
def unblock_windows_key():
    # Unblock the left Windows key
    user32.MapVirtualKeyW(VK_LWIN, 2)
    user32.MapVirtualKeyW(VK_LWIN, 2)

    # Unblock the right Windows key
    user32.MapVirtualKeyW(VK_RWIN, 2)
    user32.MapVirtualKeyW(VK_RWIN, 2)

# Example usage
block_windows_key()
# The Windows key is blocked at this point
# To unblock the Windows key, call unblock_windows_key()

root.mainloop()