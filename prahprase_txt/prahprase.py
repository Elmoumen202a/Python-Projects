import random

# Function to generate Prahprase text
def generate_prahprase():
    # Lists of possible subjects, verbs, and objects
    subjects = ['John', 'Alice', 'The cat', 'A dog', 'The tree']
    verbs = ['runs', 'jumps', 'eats', 'sleeps', 'laughs']
    objects = ['the cake', 'the book', 'a banana', 'the stars', 'the ocean']

    # Choosing a random subject, verb, and object
    subject = random.choice(subjects)
    verb = random.choice(verbs)
    obj = random.choice(objects)

    # Combining them into a Prahprase text
    prahprase = f"{subject} {verb} {obj}."
    return prahprase
