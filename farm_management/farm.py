# farm.py

class Farm:
    def __init__(self):
        # Initialize empty dictionaries to store animals and crops
        self.animals = {}
        self.crops = {}

    def add_animal(self, animal_type, quantity):
        """
        Adds animals to the farm.
        
        Parameters:
        animal_type (str): Type of the animal (e.g., 'cow', 'chicken').
        quantity (int): Number of animals to add.
        """
        if animal_type in self.animals:
            self.animals[animal_type] += quantity
        else:
            self.animals[animal_type] = quantity

    def add_crop(self, crop_type, area):
        """
        Adds crops to the farm.
        
        Parameters:
        crop_type (str): Type of the crop (e.g., 'wheat', 'corn').
        area (float): Area covered by the crop in acres.
        """
        self.crops[crop_type] = area

    def total_animals(self):
        """
        Returns the total count of all animals on the farm.
        """
        return sum(self.animals.values())

    def total_area(self):
        """
        Returns the total area used for all crops on the farm.
        """
        return sum(self.crops.values())

    def farm_summary(self):
        """
        Returns a summary of the farm's animals and crops.
        """
        return {
            "animals": self.animals,
            "crops": self.crops,
            "total_animals": self.total_animals(),
            "total_area": self.total_area()
        }

# Example usage
if __name__ == "__main__":
    farm = Farm()
    farm.add_animal("cow", 10)
    farm.add_animal("chicken", 20)
    farm.add_crop("wheat", 15.5)
    farm.add_crop("corn", 12.0)
    
    # Print farm summary
    print("Farm Summary:", farm.farm_summary())
