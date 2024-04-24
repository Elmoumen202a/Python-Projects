class BloodPressureMonitor:
    def __init__(self):
        self.readings = []  # // Initialize an empty list to store blood pressure readings.

    def add_reading(self, systolic, diastolic):
        self.readings.append((systolic, diastolic))  # // Add the new blood pressure reading to the list.

    def average_reading(self):
        if not self.readings:  # // Check if there are any readings.
            return None
        systolic_sum = sum(reading[0] for reading in self.readings)  # // Calculate the sum of systolic readings.
        diastolic_sum = sum(reading[1] for reading in self.readings)  # // Calculate the sum of diastolic readings.
        return systolic_sum / len(self.readings), diastolic_sum / len(self.readings)  # // Calculate and return the average readings.

    def check_reading(self, systolic, diastolic):
        if systolic > 140 or diastolic > 90:  # // Check for high blood pressure.
            return "High blood pressure. Please consult a doctor."
        elif systolic < 90 or diastolic < 60:  # // Check for low blood pressure.
            return "Low blood pressure. Please consult a doctor."
        else:
            return "Your blood pressure is within the normal range."  # // If blood pressure is normal.

if __name__ == "__main__":
    monitor = BloodPressureMonitor()  # // Create an instance of the BloodPressureMonitor class.
    while True:
        systolic = float(input("Enter systolic blood pressure (mmHg): "))  # // Prompt user for systolic reading.
        diastolic = float(input("Enter diastolic blood pressure (mmHg): "))  # // Prompt user for diastolic reading.
        monitor.add_reading(systolic, diastolic)  # // Add the readings to the monitor.
        average_systolic, average_diastolic = monitor.average_reading()  # // Calculate average readings.
        print("Average blood pressure: {:.2f}/{:.2f}".format(average_systolic, average_diastolic))  # // Print average readings.
        print(monitor.check_reading(systolic, diastolic))  # // Check the new reading and provide feedback.
