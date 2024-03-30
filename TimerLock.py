import tkinter as tk
import time
from Countdown import create_transparent_box
from ScreenLock import show_lock_screen

def main():
    time_limit = 2 * 60 * 60 
    
    try:
        seconds = int(input("Enter the time limit in hours: "))
        time_limit = seconds
    except ValueError:
        print("Numeric value required.")

    create_transparent_box(time_limit)

    time.sleep(time_limit)
    
    show_lock_screen()

if __name__ == "__main__":
    main()
