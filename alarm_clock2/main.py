import time
from datetime import datetime
import threading

# Function to check and notify if the alarm time is reached
def alarm_checker(alarm_time, message):
    while True:
        # Get the current time
        current_time = datetime.now().strftime("%H:%M")
        if current_time == alarm_time:
            print(f"⏰ Alarm! {message}")
            break
        time.sleep(1)  # Prevent CPU overload

# Function to set an alarm
def set_alarm():
    alarm_time = input("Enter alarm time (HH:MM): ")
    message = input("Enter a message for the alarm: ")
    print(f"Alarm set for {alarm_time} with message: '{message}'")
    # Start a thread to check the alarm
    threading.Thread(target=alarm_checker, args=(alarm_time, message), daemon=True).start()

# Main menu
def main():
    print("=== Alarm Clock ===")
    while True:
        print("\nOptions:")
        print("1. Set an Alarm")
        print("2. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            set_alarm()
        elif choice == "2":
            print("Exiting Alarm Clock. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
