# GitHub Learning Assistant

A skill for analyzing GitHub repositories and generating structured learning notes.

This project helps AI engineering students understand open-source projects,
especially projects related to AI Agents, LLM, RAG and modern AI systems.


## Features

This skill can help users:

- Understand GitHub repositories
- Analyze project structure
- Identify important technologies
- Generate structured learning notes
- Extract key files and concepts


## Project Structure


github-learning-assistant/

├── SKILL.md
│ Skill definition and instructions

├── scripts/
│ Automated analysis tools

│ └── analyze_repo.py

├── templates/
│ Learning note templates

│ └── learning-note-template.md

├── resources/
│ Reference documents

│ └── github-analysis-guide.md

└── README.md

## Installation

### 1. Clone this repository

```bash
git clone https://github.com/Sheep10086/AI-Agent-Learning.git

### 2. Enter the project directory
cd 02-My-Skills/github-learning-assistant

### 3. Install dependencies
pip install -r requirements.txt

## Usage

Run the analyzer:

python scripts/analyze_repo.py

Then enter a GitHub repository URL.

Example:

https://github.com/openai/openai-python

The assistant will generate:

Repository information
Technology overview
Learning steps
Suggested exploration direction

## Example Output

Example:

Repository Analysis

Name:
openai-python

Author:
openai

Stars:
xxxxx

Forks:
xxxxx

Technology:

- Python
- Artificial Intelligence
- Machine Learning


Learning Steps:

1. Read README.md
2. Understand project structure
3. Explore important files
4. Run examples
5. Modify and experiment

## Future Improvements

Planned features:

Automatically analyze project structure
Detect programming languages
Analyze source code
Generate AI learning roadmap
Support LLM based explanations
- Better code understanding
- Dependency analysis
- Architecture visualization
- AI-powered project summaries
