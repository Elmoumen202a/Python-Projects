import os

def say_hello():
    print("Hello!")

if __name__ == "__main__":
    # Get the absolute path of the current directory
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # Get the absolute path of the parent directory of the current directory
    main_dir = os.path.dirname(current_dir)

    # Check if the current directory is the same as the parent directory
    if current_dir == main_dir:
        # If the current directory is the same as the parent directory,
        # it means the script is being run from its own folder
        say_hello()
    else:
        # If the current directory is different from the parent directory,
        # it means the script is being run from a different folder
        print("This is not your folder.")
