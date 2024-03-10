# test.py can remain the same as before
import os

def count_folders(main_folder):
    try:
        # Get a list of all entries in the main folder
        entries = os.listdir(main_folder)

        # Filter out only the folders
        folders = [entry for entry in entries if os.path.isdir(os.path.join(main_folder, entry))]

        # Return the count of folders
        return len(folders)
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Specify the main folder path
main_folder_path = "C:\\Users\\your\\Desktop\\Python-Projects"    #"//path//to//your//main//folder"

# Call the function to get the count of folders
folder_count = count_folders(main_folder_path)

if folder_count is not None:
    print(f"The main folder '{main_folder_path}' contains {folder_count} folders.")
else:
    print("Unable to determine the folder count.")
