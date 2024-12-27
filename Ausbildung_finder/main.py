import json

def load_ausbildung_data():
    # Simulates loading Ausbildung data from a file or API.
    return [
        {"title": "Fachinformatiker/in", "language_level": "B1", "field": "IT"},
        {"title": "Kaufmann/-frau für Büromanagement", "language_level": "B2", "field": "Business"},
        {"title": "Mediengestalter/in", "language_level": "B1", "field": "IT"},
        {"title": "Koch/Köchin", "language_level": "A2", "field": "Culinary"},
    ]

def find_matching_ausbildung(language_level, field):
    # Find Ausbildung opportunities that match the user's preferences.
    ausbildung_data = load_ausbildung_data()
    matching_programs = [
        program for program in ausbildung_data
        if program["language_level"] == language_level and program["field"] == field
    ]
    return matching_programs

def main():
    print("Welcome to the Ausbildung Finder!")
    user_language_level = "B1"
    user_field = "IT"
    
    print(f"Finding Ausbildung programs for language level {user_language_level} in {user_field} field...")
    results = find_matching_ausbildung(user_language_level, user_field)
    
    if results:
        print("\nMatching Ausbildung programs:")
        for program in results:
            print(f"- {program['title']}")
    else:
        print("\nNo matching programs found. Consider improving your language level or exploring other fields.")

if __name__ == "__main__":
    main()
