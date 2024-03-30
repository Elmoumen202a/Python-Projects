import json

def load_recipes():
    try:
        with open("recipes.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_recipes(recipes):
    with open("recipes.json", "w") as file:
        json.dump(recipes, file)

def add_recipe():
    name = input("Enter recipe name: ")
    ingredients = input("Enter recipe ingredients (comma-separated): ").split(",")
    instructions = input("Enter recipe instructions: ")
    category = input("Enter recipe category: ")
    recipe = {"name": name, "ingredients": ingredients, "instructions": instructions, "category": category}
    recipes = load_recipes()
    recipes.append(recipe)
    save_recipes(recipes)
    print("Recipe added successfully!")

def view_recipes():
    recipes = load_recipes()
    if not recipes:
        print("No recipes found.")
        return
    for index, recipe in enumerate(recipes, 1):
        print(f"{index}. {recipe['name']} - {recipe['category']}")

def delete_recipe():
    view_recipes()
    recipes = load_recipes()
    if not recipes:
        return
    try:
        index = int(input("Enter the number of the recipe to delete: ")) - 1
        if 0 <= index < len(recipes):
            del recipes[index]
            save_recipes(recipes)
            print("Recipe deleted successfully!")
        else:
            print("Invalid recipe number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def main():
    print("Welcome to Recipe Organizer!")
    while True:
        print("\nMenu:")
        print("1. Add Recipe")
        print("2. View Recipes")
        print("3. Delete Recipe")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_recipe()
        elif choice == "2":
            view_recipes()
        elif choice == "3":
            delete_recipe()
        elif choice == "4":
            print("Thank you for using Recipe Organizer. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()