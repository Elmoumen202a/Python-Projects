import os

def check_and_create_readme(repo_path):
    """
    Check if a readme.md file exists in the repository. If it does not exist, create it.

    Args:
    repo_path (str): The path of the repository to check.
    """
    readme_path = os.path.join(repo_path, 'readme.md')

    if not os.path.exists(readme_path):
        with open(readme_path, 'w') as f:
            # You can customize the content of the readme.md here
            f.write("# Project Title\n\n")
            f.write("A brief description of the project goes here.\n\n")
            f.write("## Installation\n\n")
            f.write("Describe how to install the project.\n\n")
            f.write("## Usage\n\n")
            f.write("Describe how to use the project.\n")
        
        print(f"Created readme.md in {repo_path}")
    else:
        print(f"readme.md already exists in {repo_path}")

def find_repos_without_readme(base_directory):
    """
    Find repositories (directories) without a readme.md file in the base directory.

    Args:
    base_directory (str): The base directory to search for repositories.
    """
    for root, dirs, files in os.walk(base_directory):
        if '.git' in dirs:  # Check if it's a git repository
            check_and_create_readme(root)

if __name__ == "__main__":
    base_dir = input("Enter the base directory path to check for repositories: ")
    find_repos_without_readme(base_dir)
