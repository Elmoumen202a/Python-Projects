import hashlib

def hash_file(file_path):
    # Initialize a SHA-1 hash object
    sha1 = hashlib.sha1()

    # Open the file in binary mode
    with open(file_path, "rb") as file:
        # Read the file in chunks of 1024 bytes
        chunk = 0
        while chunk := file.read(1024):
            # Update the hash with the current chunk
            sha1.update(chunk)

    # Return the hexadecimal digest of the hash
    return sha1.hexdigest()

def are_files_identical(file_path1, file_path2):
    # Calculate the hash for each file
    hash1 = hash_file(file_path1)
    hash2 = hash_file(file_path2)

    # Compare the hashes to determine file identity
    return hash1 == hash2

if __name__ == "__main__":
    # File paths to be compared
    file_path1 = "pd1.pdf"
    file_path2 = "pd1.pdf"

    # Check if the files are identical and print the result
    if are_files_identical(file_path1, file_path2):
        print("These files are identical")
    else:
        print("These files are not identical")
