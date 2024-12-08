# Define a class to represent a car
class Car:
    def __init__(self, car_id, model, rent_per_day):
        """
        Initialize a car object with the following attributes:
        - car_id: Unique identifier for the car (e.g., 1, 2, 3).
        - model: The model name of the car (e.g., "Toyota Corolla").
        - rent_per_day: The cost to rent the car per day.
        """
        self.car_id = car_id
        self.model = model
        self.rent_per_day = rent_per_day
        # Tracks whether the car is rented (False by default).
        self.is_rented = False  

    def __str__(self):
        """
        Define how the car object is represented as a string.
        Returns details about the car, including its rental status.
        """
        return f"Car ID: {self.car_id}, Model: {self.model}, Rent/Day: ${self.rent_per_day}, Rented: {self.is_rented}"

# Define a class to manage car rentals
class CarRental:
    def __init__(self):
        """
        Initialize the CarRental system.
        This system uses a list to store all cars available for rent.
        """
        # List to hold Car objects.
        self.cars = []  

    def add_car(self, car_id, model, rent_per_day):
        """
        Add a new car to the rental system.
        Parameters:
        - car_id: Unique ID for the car.
        - model: Model of the car.
        - rent_per_day: Rental price per day.
        """
        # Create a new Car object.
        car = Car(car_id, model, rent_per_day)  
        # Add the car to the list of available cars.
        self.cars.append(car)  

    def rent_car(self, car_id):
        """
        Rent out a car if it is available.
        Parameters:
        - car_id: The ID of the car to rent.
        Returns a message indicating whether the rental was successful or not.
        """
        for car in self.cars:
            # Check if the car is available for rent
            if car.car_id == car_id and not car.is_rented:
                car.is_rented = True  # Mark the car as rented
                return f"Car {car_id} has been rented out."
        return f"Car {car_id} is not available."  # If car is already rented or does not exist.

    def return_car(self, car_id):
        """
        Return a rented car to the system.
        Parameters:
        - car_id: The ID of the car to return.
        Returns a message indicating whether the return was successful or not.
        """
        for car in self.cars:
            # Check if the car is currently rented
            if car.car_id == car_id and car.is_rented:
                car.is_rented = False  # Mark the car as available
                return f"Car {car_id} has been returned."
        return f"Car {car_id} was not rented."  # If the car was not rented or does not exist.

    def list_cars(self):
        """
        List all cars in the system, including their rental status.
        Returns a list of strings, each describing a car.
        """
        return [str(car) for car in self.cars]  # Use the __str__ method of Car for each car.

# Example usage of the CarRental system
if __name__ == "__main__":
    # Create a car rental system object
    rental_system = CarRental()

    # Add some cars to the system
    rental_system.add_car(1, "Toyota Corolla", 40)
    rental_system.add_car(2, "Honda Civic", 50)
    rental_system.add_car(3, "Tesla Model 3", 100)

    # Display the list of cars
    print("Available cars:")
    print(rental_system.list_cars())

    # Rent a car
    print("\nRenting Car 2:")
    print(rental_system.rent_car(2))

    # Display the updated list of cars
    print("\nUpdated car list:")
    print(rental_system.list_cars())

    # Return a car
    print("\nReturning Car 2:")
    print(rental_system.return_car(2))

    # Display the final list of cars
    print("\nFinal car list:")
    print(rental_system.list_cars())
