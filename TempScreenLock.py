import tkinter as tk
import time
import os
import json

with open('config.json') as config_file:
    config = json.load(config_file)   
    
# from Countdown import create_transparent_box

# Unlock Screen if password correct
def unlock(password_entry, root, error_label):
    password = password_entry.get()
    
    if password == config['password']:  
        root.destroy()
        print("Destroy")
    else:
        error_label.config(text="Incorrect password. Please try again.")  
        password_entry.delete(0, tk.END)

# Shutdown System if password correct
def temp_lock_screen(tempTime):
    def shutdown_windows(password_entry, error_label):
        password = password_entry.get()
        
        if password == config['password']:  
            os.system("shutdown /s /t 3")  
        else:
            error_label.config(text="Incorrect password. Please try again.")  
            password_entry.delete(0, tk.END)

    root = tk.Tk()
    root.attributes('-fullscreen', True)

    label = tk.Label(root, text="Enter password to unlock", font=("Helvetica", 24))
    label.pack(pady=50)

    error_label = tk.Label(root, text="", fg="red", font=("Helvetica", 12))
    error_label.pack(pady=10)

    password_entry = tk.Entry(root, show='*')
    password_entry.pack(pady=10)
    
    def unlock_and_destroy(event=None):
        unlock(password_entry, root, error_label)

        # Bind the Return key to call the unlock function
    password_entry.bind('<Return>', unlock_and_destroy)

    unlock_button = tk.Button(root, text="Unlock", command=lambda: unlock(password_entry, root, error_label))
    unlock_button.pack(pady=10)

    shutdown_button = tk.Button(root, text="ShutDown", command=lambda: shutdown_windows(password_entry, error_label))
    shutdown_button.pack(pady=10)

    def update_timer(temp_time):

        if temp_time > 0:
            mins, secs = divmod(temp_time, 60)
            timer_label.config(text=f'{mins:02d}:{secs:02d}')
            new_time = temp_time
            new_time -= 1
            root.after(1000, lambda: update_timer(new_time))
            print(new_time)
        else:
            root.destroy()
            print("root destroyed")
    
    LockTime = str(config['timeLock']) + " min Rest!"
    
    caption_label = tk.Label(root, text= LockTime, font=('Helvetica', 100))
    caption_label.pack(expand=True)

    timer_label = tk.Label(root, font=('Helvetica', 100))
    timer_label.pack(expand=True)

    # Start countdown for 15 minutes

    update_timer(tempTime)

    root.mainloop()

temp_lock_screen(15)