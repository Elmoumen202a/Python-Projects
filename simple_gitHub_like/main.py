# Define a class for the Repository
class Repository:
    def __init__(self, name):
        # Initialize a repository with a name and an empty list for commits
        self.name = name
        self.commits = []
    
    def add_commit(self, message):
        # Add a commit message to the list of commits
        self.commits.append(message)
    
    def view_commits(self):
        # Check if there are any commits, if not return a message saying "No commits yet!"
        if not self.commits:
            return "No commits yet!"
        # If there are commits, list them in the order they were added
        return "\n".join(f"Commit {i + 1}: {msg}" for i, msg in enumerate(self.commits))

# Define a class for GitHub, which manages multiple repositories
class GitHub:
    def __init__(self):
        # Initialize an empty dictionary to store repositories by their names
        self.repositories = {}
    
    def create_repository(self, repo_name):
        # Check if a repository with the given name already exists
        if repo_name in self.repositories:
            return f"Repository '{repo_name}' already exists!"
        # If not, create a new repository and store it in the repositories dictionary
        self.repositories[repo_name] = Repository(repo_name)
        return f"Repository '{repo_name}' created."
    
    def add_commit_to_repository(self, repo_name, commit_message):
        # Check if the repository exists
        if repo_name not in self.repositories:
            return f"Repository '{repo_name}' not found!"
        # If it exists, add a commit message to the repository
        self.repositories[repo_name].add_commit(commit_message)
        return f"Commit added to repository '{repo_name}'."
    
    def view_repository_commits(self, repo_name):
        # Check if the repository exists
        if repo_name not in self.repositories:
            return f"Repository '{repo_name}' not found!"
        # If it exists, return the commit history for that repository
        return self.repositories[repo_name].view_commits()

# Example of how the project works
if __name__ == "__main__":
    # Create a GitHub instance to manage repositories
    github = GitHub()
    
    # Create a new repository named "MyRepo"
    print(github.create_repository("MyRepo"))
    
    # Add two commits to "MyRepo"
    print(github.add_commit_to_repository("MyRepo", "Initial commit"))
    print(github.add_commit_to_repository("MyRepo", "Added README file"))
    
    # View the commit history of "MyRepo"
    print(github.view_repository_commits("MyRepo"))
