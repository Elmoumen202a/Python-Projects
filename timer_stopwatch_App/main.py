# Import tkinter for GUI creation
import tkinter as tk  
# Import messagebox for dialog boxes
from tkinter import messagebox 
# Import time for time-related operations 
import time  

class TimerStopwatch:
    """
    - Start: Start the timer
    - Stop: Pause the timer
    - Reset: Reset the timer to 00:00:00
    """

    def __init__(self, root):
        """
        param root: Tk root window
        """
        self.root = root
        self.root.title("Timer/Stopwatch")  # Set the window title
        self.root.geometry("300x200")  # Set the window size
        self.time_elapsed = 0  # Initialize elapsed time
        self.running = False  # Flag to track whether the timer is running

        # Label to display the time
        self.label = tk.Label(root, text="00:00:00", font=("Helvetica", 24))
        self.label.pack(pady=20)

        # Buttons to control the timer
        self.start_button = tk.Button(root, text="Start", command=self.start, width=10)
        self.start_button.pack(side="left", padx=10)

        self.stop_button = tk.Button(root, text="Stop", command=self.stop, width=10)
        self.stop_button.pack(side="left", padx=10)

        self.reset_button = tk.Button(root, text="Reset", command=self.reset, width=10)
        self.reset_button.pack(side="left", padx=10)

    def update_time(self):
        """
        Update the timer display every second if the timer is running.
        """
        if self.running:
            self.time_elapsed += 1
            time_str = time.strftime('%H:%M:%S', time.gmtime(self.time_elapsed))
            self.label.config(text=time_str)
            # Schedule the next update after 1 second
            self.root.after(1000, self.update_time)

    def start(self):
        """
        Start the timer if it's not already running.
        """
        if not self.running:
            self.running = True
            self.update_time()

    def stop(self):
        """
        Stop the timer, keeping the current elapsed time.
        """
        self.running = False

    def reset(self):
        """
        Reset the timer to 00 and stop it.
        """
        self.stop()
        self.time_elapsed = 0
        self.label.config(text="00:00:00")

if __name__ == "__main__":
    root = tk.Tk()  # Create the main tkinter window
    app = TimerStopwatch(root)  # Instantiate the TimerStopwatch class
    root.mainloop()
