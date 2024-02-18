def generate_story():
    """
    Generate a Mad Libs story based on user input.

    Returns:
        str: The generated Mad Libs story.
    """
    adj1 = input('Choose an adjective: ')
    color = input('Pick a color: ')
    adj2 = input('Choose another adjective: ')
    animal = input('Name an animal: ')
    verb = input('Choose a verb (past tense): ')
    adv = input('Choose an adverb: ')
    adj3 = input('Choose one more adjective: ')
    noun = input('Choose a noun: ')

    story = f"------------------------------------------\n"\
            f"The {adj1} {color} fox jumped over the {adj2} {animal}.\n"\
            f"It {verb} {adv} and looked very {adj3}.\n"\
            f"The quick, brown {animal} landed on a {noun}.\n"\
            f"------------------------------------------\n"
    return story

story_=generate_story()
print(story_)
# Uncomment the line below if you want to generate a story immediately when mad_libs_generator.py is executed.
# print(generate_story())
