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


    response = requests.get(api_url)


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



if __name__ == "__main__":


    url = input(
        "Enter GitHub repository URL: "
    )


    info = get_repository_info(url)


    print("\n===== Repository Analysis =====\n")


    for key, value in info.items():

        print(key + ":")

        print(value)

        print()
