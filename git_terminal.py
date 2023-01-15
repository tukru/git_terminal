from github import Github
import getpass

# Authenticate using an access token or username and password
username = input("Enter your Github username:")
password = getpass.getpass(prompt="Enter your Github password:")
g = Github(username, password)

# Search for repositories
query = input("Enter your search query:")
repos = g.search_repositories(query)

# Print repository details
for repo in repos:
    print("Name: ", repo.name)
    print("Full Name: ", repo.full_name)
    print("Description: ", repo.description)
    print("URL: ", repo.html_url)
    print("\n")
