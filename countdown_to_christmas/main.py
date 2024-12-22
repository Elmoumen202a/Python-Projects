import datetime
import random

# Christmas date
CHRISTMAS_DATE = datetime.date(datetime.datetime.now().year, 12, 25)

def countdown_to_christmas():
    """Calculate the number of days until Christmas."""
    today = datetime.date.today()
    delta = (CHRISTMAS_DATE - today).days
    return delta if delta >= 0 else 0

def random_christmas_wish():
    """Generate a random Christmas wish."""
    wishes = [
        "🎅 Ho Ho Ho! Merry Christmas! 🎄",
        "✨ Wishing you a season filled with joy and cheer! 🌟",
        "🎁 May your Christmas be wrapped in happiness! 🎀",
        "❄️ Sending warm holiday hugs your way! 💖",
        "🎶 Joy to the World! Have a blessed Christmas! 🎵"
    ]
    return random.choice(wishes)

def main():
    """Main function to display the Christmas countdown and wish."""
    days_left = countdown_to_christmas()
    print(f"📅 Days until Christmas: {days_left}")
    print(random_christmas_wish())

if __name__ == "__main__":
    main()
