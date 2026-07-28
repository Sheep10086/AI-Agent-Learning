from analyze_repo import get_repository_info
from ai_generator import generate_with_ai


def main():

    print("=== GitHub Learning Assistant ===")

    url = input(
        "Enter GitHub repository URL: "
    )


    print("\nAnalyzing repository...")


    repo_info = get_repository_info(url)


    if "error" in repo_info:
        print(repo_info["error"])
        return


    print("\nGenerating learning notes...")


    note = generate_with_ai(repo_info)


    filename = "learning_note.md"


    with open(
        filename,
        "w",
        encoding="utf-8"
    ) as f:

        f.write(note)


    print(
        "\nDone!"
    )

    print(
        f"Learning note saved to {filename}"
    )


if __name__ == "__main__":
    main()
