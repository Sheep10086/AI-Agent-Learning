def generate_with_ai(repository_info):

    """
    Generate learning notes with AI model.
    """

    note = f"""
# {repository_info['Name']} Learning Notes


## Overview

{repository_info['Description']}


## Repository Information

- Author:
{repository_info['Author']}

- Stars:
{repository_info['Stars']}


## Learning Suggestions

1. Read README.md
2. Understand project structure
3. Explore source code
4. Try examples
5. Build your own project

"""

    return note
