import random

# Dictionary mapping categories to potential names
name_data = {
    "points": {
        "high": ["Alexander", "Sophia"],
        "medium": ["Mia", "Liam"],
        "low": ["Oliver", "Ava"]
    },
    "color": {
        "blue": ["Sky", "Azure"],
        "red": ["Ruby", "Scarlett"],
        "green": ["Jade", "Forest"]
    },
    "style": {
        "classic": ["William", "Elizabeth"],
        "modern": ["Zayn", "Nova"]
    }
}

def suggest_name(points, color, style):
    """Suggest a name based on user preferences."""
    suggestions = []
    suggestions.extend(name_data["points"].get(points, []))
    suggestions.extend(name_data["color"].get(color, []))
    suggestions.extend(name_data["style"].get(style, []))
    return random.choice(suggestions) if suggestions else "No suggestions available."

if __name__ == "__main__":
    print("Welcome to Baby Name Chooser!")
    points = input("Enter points (high, medium, low): ").strip().lower()
    color = input("Enter favorite color (blue, red, green): ").strip().lower()
    style = input("Enter name style (classic, modern): ").strip().lower()
    name = suggest_name(points, color, style)
    print(f"Suggested name: {name}")
