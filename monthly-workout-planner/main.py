import calendar

class WorkoutPlanner:
    def __init__(self):
        self.workouts = {
            'January': ['Legs', 'Cardio'],
            'February': ['Arms', 'Core'],
            'March': ['Back', 'Cardio'],
            'April': ['Legs', 'Cardio'],
            'May': ['Arms', 'Core'],
            'June': ['Legs', 'Cardio'],
            'July': ['Back', 'Cardio'],
            'August': ['Arms', 'Core'],
            'September': ['Legs', 'Cardio'],
            'October': ['Arms', 'Core'],
            'November': ['Legs', 'Cardio'],
            'December': ['Arms', 'Core']
        }

    def suggest_workout(self, month):
        month_name = calendar.month_name[month]
        return f"For {month_name}, you can train: {', '.join(self.workouts[month_name])}"

if __name__ == "__main__":
    planner = WorkoutPlanner()
    month = 1  # Example: January
    print(planner.suggest_workout(month))
