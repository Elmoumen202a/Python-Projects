class Car:
    def __init__(self, speed_limit=100):
        # Initialize car attributes
        self.speeds = []
        self.speed_limit = speed_limit

    def check_speed(self, speed):
       # Check if the car is over the speed limit
        self.speeds.append(speed)
        if speed > self.speed_limit:
            return f"Speed {speed} km/h is over the limit!"
        return f"Speed {speed} km/h is within the limit."

    def average_speed(self):
        #Calculate the average speed of the car
        if not self.speeds:
            return "No speeds recorded."
        avg_speed = sum(self.speeds) / len(self.speeds)
        return f"Average speed: {avg_speed:.2f} km/h"

    def speed_history(self):
       # Return the history of recorded speeds
        return self.speeds


if __name__ == "__main__":
    # Main program logic
    car = Car(speed_limit=80)
    
    while True:
        speed = float(input("Enter the current speed of the car (km/h): "))
        print(car.check_speed(speed))
        
        choice = input("Do you want to check average speed? (yes/no): ").strip().lower()
        if choice == 'yes':
            print(car.average_speed())

        more = input("Do you want to add more speeds? (yes/no): ").strip().lower()
        if more == 'no':
            print("Speed history:", car.speed_history())
            break
