import os
from folder_count import count_folders  # Replace 'your_module_name' with the actual module name

def test_count_folders():
    # Specify a temporary test folder with a known number of folders
    test_folder_path = "/path/to/your/test/folder"
    expected_folder_count = 3  # Adjust to the actual number of folders in the test folder

    # Create test folders
    os.makedirs(os.path.join(test_folder_path, "folder1"))
    os.makedirs(os.path.join(test_folder_path, "folder2"))
    os.makedirs(os.path.join(test_folder_path, "folder3"))

    # Call the function to get the count of folders
    folder_count = count_folders(test_folder_path)

    # Clean up: Remove the test folders
    for folder_name in ["folder1", "folder2", "folder3"]:
        os.rmdir(os.path.join(test_folder_path, folder_name))

    # Perform the test
    assert folder_count == expected_folder_count, f"Expected {expected_folder_count} folders, but got {folder_count}."
