from datetime import datetime   
from playsound import playsound

def set_alarm():
    """
    Function to set an alarm and play a sound when the alarm time is reached.
    """
    # Get user input for the alarm time
    alarm_time = input("Enter the time of alarm to be set (HH:MM:SS AM/PM)\n")

    # Extract components of the alarm time
    alarm_hour = alarm_time[0:2]
    alarm_minute = alarm_time[3:5]
    alarm_seconds = alarm_time[6:8]
    alarm_period = alarm_time[9:11].upper()

    print("Setting up alarm..")

    # Infinite loop to continuously check the current time against the alarm time
    while True:
        now = datetime.now()
        current_hour = now.strftime("%I")
        current_minute = now.strftime("%M")
        current_seconds = now.strftime("%S")
        current_period = now.strftime("%p")

        # Check if the alarm time matches the current time
        if alarm_period == current_period and alarm_hour == current_hour and \
           alarm_minute == current_minute and alarm_seconds == current_seconds:
            print("Wake Up!")
            playsound('audio.mp3')
            break

# Uncomment the line below if you want the alarm to be set immediately
# set_alarm()
