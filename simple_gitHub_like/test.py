import unittest
from main import GitHub

# Define a class for testing the GitHub-like project
class TestGitHub(unittest.TestCase):
    
    # Test creating a repository
    def test_create_repository(self):
        github = GitHub()
        result = github.create_repository("TestRepo")
        self.assertEqual(result, "Repository 'TestRepo' created.")
        
        # Check that trying to create the same repository again returns an error
        result = github.create_repository("TestRepo")
        self.assertEqual(result, "Repository 'TestRepo' already exists!")

    # Test adding commits to a repository
    def test_add_commit(self):
        github = GitHub()
        github.create_repository("TestRepo")
        
        # Add a commit to the repository
        result = github.add_commit_to_repository("TestRepo", "First commit")
        self.assertEqual(result, "Commit added to repository 'TestRepo'.")
        
        # Check commit history to ensure the commit was added
        commit_history = github.view_repository_commits("TestRepo")
        self.assertIn("First commit", commit_history)

    # Test viewing commit history
    def test_view_commits(self):
        github = GitHub()
        github.create_repository("TestRepo")
        
        # Test viewing commits in an empty repository
        empty_history = github.view_repository_commits("TestRepo")
        self.assertEqual(empty_history, "No commits yet!")
        
        # Add a commit and check history again
        github.add_commit_to_repository("TestRepo", "Initial commit")
        history = github.view_repository_commits("TestRepo")
        self.assertIn("Commit 1: Initial commit", history)
    
    # Test viewing commits from a non-existent repository
    def test_view_commits_non_existent_repo(self):
        github = GitHub()
        result = github.view_repository_commits("NonExistentRepo")
        self.assertEqual(result, "Repository 'NonExistentRepo' not found!")

# Run the tests
if __name__ == "__main__":
    unittest.main()
