import matplotlib.pyplot as plt  # Importing the matplotlib library to display images
import os  # Importing os library to work with file paths

def draw_image(image_name):
    """
    Draw an image based on the user-provided input name.
    
    Parameters:
    image_name (str): The name of the image to be displayed (without extension).
    """
    # Create a file path based on the user's input. The input is converted to lowercase
    # to match file naming convention and '.png' is appended to complete the file path.
    image_path = f'images/{image_name.lower()}.png'
    
    # Check if the image file exists at the specified path
    if os.path.exists(image_path):
        # Load the image using matplotlib's imread function
        img = plt.imread(image_path)
        # Display the image using imshow
        plt.imshow(img)
        # Hide the axes for a cleaner image display
        plt.axis('off')
        # Show the image window
        plt.show()
    else:
        # If the image doesn't exist, notify the user with a friendly message
        print(f"Image '{image_name}' not found. Please ensure the image is available in the 'images' folder.")

if __name__ == '__main__':
    # Start an infinite loop to continually ask the user for input
    while True:
        # Prompt the user to enter the image name or 'exit' to quit
        name = input("Enter the name of the image to draw (or type 'exit' to quit): ")
        # If the user types 'exit', break the loop and end the program
        if name.lower() == 'exit':
            print("Exiting the program. Goodbye!")
            break
        # Call the draw_image function to display the image based on user input
        draw_image(name)
