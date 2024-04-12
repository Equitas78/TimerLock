import time
import tkinter as tk
from Countdown import create_transparent_box
from ScreenLock import show_lock_screen

def build_window():
    root = tk.Tk()
    root.title("Time Selection")
    root.geometry("250x150+" + str(int(root.winfo_screenwidth()/2)) + "+" + str(int(root.winfo_screenheight()/2)) )
    label = tk.Label(root, text="Enter the time limit in hours:")
    label.pack()

    #hours_entry = tk.Entry(root)
    #hours_entry.pack()
    hours_var = tk.StringVar(root)
    hours_var.set("1")  # default value
    hours_menu = tk.OptionMenu(root, hours_var, "1", "2", "3", "4", "5")
    hours_menu.pack()

    def start_program_with_selected_time():
        hours = int(hours_var.get())
        time_limit = hours * 60 * 60
        root.destroy()
        
        create_transparent_box(time_limit)
        
        time.sleep(time_limit)
        
        show_lock_screen()
   
    start_button = tk.Button(root, text="Start Program", command=start_program_with_selected_time)
    start_button.pack()
      
    root.mainloop()



