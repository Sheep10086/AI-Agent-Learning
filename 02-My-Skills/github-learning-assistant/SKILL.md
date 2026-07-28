---
name: github-learning-assistant
description: Analyze GitHub repositories and generate structured learning notes for AI engineering students.
---

# GitHub Learning Assistant


## Purpose

This skill helps users understand GitHub repositories,
especially AI and Agent related projects.


## When to Use This Skill

Use this skill when:

- User finds a new GitHub repository
- User wants to understand an AI project
- User needs a technical summary
- User wants learning notes


## Instructions


When analyzing a GitHub repository, follow these steps:


### Step 1: Collect Repository Information

First check:

- Repository name
- Author
- Description
- Stars
- Forks
- Last update


Use scripts/analyze_repo.py when repository information needs to be collected automatically.


### Step 2: Understand Project Structure

Analyze:

- README.md
- Main folders
- Source code
- Documentation
- Examples


### Step 3: Identify Technologies

Identify important technologies:

- Programming languages
- Frameworks
- AI models
- Agent frameworks
- RAG systems
- MCP
- Vector databases


Refer to:

resources/github-analysis-guide.md


### Step 4: Generate Learning Notes

Use:

templates/learning-note-template.md


The output should include:

- Project overview
- Technology stack
- Important files
- Core concepts
- Learning notes
- Next steps


### Step 5: Output Quality Rules

The final explanation should:

- Be understandable for AI engineering students
- Explain why technologies are used
- Explain project architecture
- Provide learning suggestions

## Output Format

Use this structure:


# Project Name


## Overview


## Technology


## Important Files


## Learning Notes


## Next Steps


## Examples

Example:

Input:

Analyze this GitHub repository:
https://github.com/example/project


Output:

A structured learning note about the project.
