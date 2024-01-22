import cv2
import main

def test_generate_handwriting_image():
    text = "Testing text"
    output_path = "test_handwriting.png"
    main.generate_handwriting_image(text, output_path)
    assert cv2.imread(output_path) is not None

def test_display_handwriting_image(capfd):
    image_path = "handwriting.png"
    main.display_handwriting_image(image_path)

    captured = capfd.readouterr()
    assert "Text to Handwriting" in captured.out
