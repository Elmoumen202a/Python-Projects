import re

# Simulated database of motor data
MOTOR_DATA = [
    {"name": "Honda CB500", "type": "Motorcycle", "power": "471cc", "category": "Sports"},
    {"name": "Yamaha R15", "type": "Motorcycle", "power": "155cc", "category": "Sports"},
    {"name": "Tesla Model S", "type": "Car", "power": "Electric", "category": "Sedan"},
    {"name": "Ford F-150", "type": "Truck", "power": "450 HP", "category": "Utility"},
    {"name": "Kawasaki Ninja 300", "type": "Motorcycle", "power": "296cc", "category": "Sports"},
]

def search_motor(query):
    """
    Searches for motors that match the query in the MOTOR_DATA database.
    Returns a list of results.
    """
    query = query.lower()
    results = [
        motor for motor in MOTOR_DATA
        if any(query in str(value).lower() for value in motor.values())
    ]
    return results

def display_results(results):
    """
    Displays search results in a readable format.
    """
    if not results:
        print("No results found!")
    else:
        print("Search Results:")
        for i, motor in enumerate(results, 1):
            print(f"{i}. Name: {motor['name']}, Type: {motor['type']}, Power: {motor['power']}, Category: {motor['category']}")

if __name__ == "__main__":
    print("Welcome to the Motor Search Engine!")
    query = input("Enter your search query: ")
    results = search_motor(query)
    display_results(results)
