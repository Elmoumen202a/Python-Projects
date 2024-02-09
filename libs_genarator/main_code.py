def generate_mad_libs():
    # Questions for the user to answer
    adjective = input('Choose an adjective: ')
    verb = input('Choose a verb: ')
    animal = input('Choose an animal: ')
    color = input('Choose a color: ')
    food = input('Choose a food: ')
    number = input('Choose a number: ')

    # Print a story from the user input
    print('------------------------------------------')
    print('Once upon a time, in a', adjective, 'forest,')
    print('A curious squirrel decided to', verb, 'with a friendly', animal, '.')
    print('They traveled through the', color, 'woods, searching for', food, '.')
    print('After a journey of', number, 'days, they discovered a magical clearing.')
    print('In the center, there was a', color, 'castle where they lived happily ever after.')
    print('------------------------------------------')

# Example with different inputs
generate_mad_libs()
