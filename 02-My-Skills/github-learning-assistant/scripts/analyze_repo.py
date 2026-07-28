import os


def analyze_repository(repo_url):
    """
    Analyze a GitHub repository.
    """

    result = {
        "Repository": repo_url,
        "Overview": "This repository is analyzed by GitHub Learning Assistant.",
        "Technologies": [
            "Python",
            "AI",
            "Machine Learning"
        ],
        "Learning Notes": [
            "Understand project structure",
            "Read important files",
            "Explore core technologies"
        ]
    }

    return result


if __name__ == "__main__":

    url = input(
        "Enter GitHub repository URL: "
    )

    analysis = analyze_repository(url)

    print("\n===== Learning Note =====\n")

    for key, value in analysis.items():
        print(key)
        print(value)
        print()
