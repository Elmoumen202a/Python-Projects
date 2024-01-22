# Import necessary libraries
import pywhatkit as kit
import cv2

# Function to generate an image with handwriting from text
def generate_handwriting_image(text, save_path):
    kit.text_to_handwriting(text, save_to=save_path)

# Function to display the generated handwriting image
def display_handwriting_image(image_path):
    # Read the image using OpenCV
    img = cv2.imread(image_path)

    # Display the image in a window titled "Text to Handwriting"
    cv2.imshow("Text to Handwriting", img)

    # Wait for a key press and close the window when any key is pressed
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Main block of code
if __name__ == "__main__":
    # Set the text to be converted to handwriting
    text_to_convert = "Happy coding"

    # Set the output image path
    output_image_path = "handwriting.png"

    # Generate an image with the specified text converted to handwriting
    generate_handwriting_image(text_to_convert, output_image_path)

    # Display the generated handwriting image
    display_handwriting_image(output_image_path)
