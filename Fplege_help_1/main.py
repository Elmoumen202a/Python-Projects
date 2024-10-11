import time

# This dictionary holds the medication schedule. 
# Each key (Morning, Afternoon, Evening) contains a list of medications with their dosages.
medication_schedule = {
    "Morning": [("Aspirin", "100mg"), ("Vitamin D", "500 IU")],
    "Afternoon": [("Metformin", "500mg")],
    "Evening": [("Ibuprofen", "200mg")]
}

# This dictionary holds body parts and their translations from English to German.
body_parts = {
    "Head": "Kopf",
    "Arm": "Arm",
    "Leg": "Bein",
    "Heart": "Herz",
    "Lungs": "Lunge"
}

def show_medication(time_of_day):
    """
    Shows the medications to be taken at a specific time of day.
    """
    if time_of_day in medication_schedule:
        meds = medication_schedule[time_of_day]
        print(f"Medications for {time_of_day}:")
        # Go through each medication and print its name and dosage.
        for med in meds:
            print(f"- {med[0]}: {med[1]}")
    else:
        print("No medications scheduled for this time.")

def translate_body_part(part):
    """
    Translates an English body part into German.
    """
    if part in body_parts:
        return f"{part} in German is {body_parts[part]}"
    else:
        return "Body part not found."

def medication_reminder():
    """
    Shows reminders for all times of the day when medications should be taken.
    """
    for time_of_day in medication_schedule:
        print(f"Reminder for {time_of_day}:")
        show_medication(time_of_day)
        # Wait for 2 seconds before showing the next reminder.
        time.sleep(2)

if __name__ == "__main__":
    # Example: Translate the word 'Heart' into German.
    print(translate_body_part("Heart"))
    
    # Show reminders for all medication times (morning, afternoon, evening).
    medication_reminder()
