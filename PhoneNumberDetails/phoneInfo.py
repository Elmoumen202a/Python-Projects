# Import necessary functions from the phonenumbers library
import phonenumbers as ph
from phonenumbers import carrier
from phonenumbers import geocoder
from phonenumbers import timezone

# Define a function to retrieve information about a phone number
def get_phone_info(phone_number):
    # Parse the input phone number using phonenumbers library
    number = ph.parse(phone_number)

    # Get the time zones associated with the phone number
    time_zones = timezone.time_zones_for_number(number)

    # Get the carrier name for the phone number in English
    carrier_name = carrier.name_for_number(number, "en")

    # Get the location description for the phone number in English
    location_description = geocoder.description_for_number(number, "en")

    # Return a dictionary containing the gathered information
    return {
        "time_zones": time_zones,
        "carrier_name": carrier_name,
        "location_description": location_description
    }

# Check if the script is being run as the main program
if __name__ == "__main__":
    # Example usage:
    
    # Define a sample phone number
    phone_number = "+212XXXXXXXX"
    
    # Call the get_phone_info function with the sample phone number
    info = get_phone_info(phone_number)
    
    # Print the gathered information
    print(info)
