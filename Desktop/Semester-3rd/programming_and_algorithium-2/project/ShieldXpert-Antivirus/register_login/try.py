import tkinter as tk
import subprocess

def open_login_page():
    # Create a new top-level window for the login page
    login_window = tk.Toplevel(window)
    
    # Hide the main window (optional, depending on your design)
    window.withdraw()

    # Execute the login page script
    subprocess.Popen(['python', r'C:\Users\asus\Desktop\Semester-3rd\programming_and_algorithium-2\project\ShieldXpert-Antivirus\Python Tkinter Modern GUI login and sign up form\login_page.py'])

    # Destroy the main window when the login page is closed
    login_window.protocol("WM_DELETE_WINDOW", lambda: on_login_window_close(login_window))

def on_login_window_close(main_window):
    # Unhide the main window when the login window is closed
    window.deiconify()
    main_window.destroy()

# Rest of your code...

switchLogin.config(command=open_login_page)

# Rest of your code...
