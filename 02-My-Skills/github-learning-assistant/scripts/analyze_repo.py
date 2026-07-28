import os


def analyze_repository(path):
    """
    Analyze a local GitHub repository structure.
    """

    print("Repository Analysis")
    print("-------------------")

    for root, dirs, files in os.walk(path):
        level = root.replace(path, "").count(os.sep)

        indent = " " * 4 * level

        print(f"{indent}{os.path.basename(root)}/")

        for file in files[:5]:
            print(f"{indent}    {file}")


if __name__ == "__main__":

    repo_path = "."

    analyze_repository(repo_path)
