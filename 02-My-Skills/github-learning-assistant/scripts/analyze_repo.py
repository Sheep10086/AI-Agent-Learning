import requests


def get_repository_info(repo_url):

    """
    Get GitHub repository information.
    """

    parts = repo_url.rstrip("/").split("/")

    owner = parts[-2]
    repo = parts[-1]


    api_url = (
        f"https://api.github.com/repos/{owner}/{repo}"
    )


try:
    response = requests.get(api_url)

except Exception as e:
    return {
        "error": str(e)
    }


    if response.status_code != 200:
        return {
            "error": "Cannot fetch repository information"
        }


    data = response.json()


    result = {

        "Name": data["name"],

        "Author": data["owner"]["login"],

        "Description": data["description"],

        "Stars": data["stargazers_count"],

        "Forks": data["forks_count"],

        "Last Update": data["updated_at"]

    }


    return result

def generate_learning_note(info):
    """
    Generate a simple learning note.
    """

    note = f"""
# {info['Name']} Learning Notes


## Overview

{info['Description']}


## Repository Information

- Author: {info['Author']}
- Stars: {info['Stars']}
- Forks: {info['Forks']}
- Last Update: {info['Last Update']}


## Technology

Possible technologies:

- Python
- Artificial Intelligence
- Machine Learning
- Large Language Model


## Learning Steps

1. Read README.md
2. Understand project structure
3. Explore important files
4. Try running examples
5. Modify and experiment


## Next Steps

Continue studying related AI concepts.
"""

    return note

if __name__ == "__main__":


    url = input(
        "Enter GitHub repository URL: "
    )


    info = get_repository_info(url)


    print("\n===== Repository Analysis =====\n")


note = generate_learning_note(info)

print(note)
