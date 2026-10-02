# Commit Convention

This project follows a simplified version of Conventional Commits to ensure a clean, readable, and structured Git history.

## Format

Each commit message should follow this format:
```
<type>: <short description>
```

## Allowed Types

| Type | Description | Example |
| :--- | :--- | :--- |
| **`feat`** | A new feature or functionality | `feat: add article submission API` |
| **`fix`** | A bug fix | `fix: correct article validation error` |
| **`test`** | Adding missing tests or correcting existing tests | `test: add article submission unit tests` |
| **`docs`** | Changes to documentation | `docs: update project README and add week 4 docs` |
| **`chore`** | Routine tasks, maintenance, dependency updates, or project setup | `chore: add python gitignore and project structure` |
| **`ci`** | Changes to CI configuration files and scripts | `ci: update Jenkins pipeline configuration` |

## Guidelines

1.  **Use lowercase for the type:** Always use `feat:`, `fix:`, etc.
2.  **Use the imperative mood in the description:** Write "add feature" not "added feature" or "adding feature". (Think of it as completing the sentence: "If applied, this commit will...")
3.  **Keep it concise:** The first line (summary) should ideally be under 50-72 characters.
4.  **Logical Commits:** Group related changes into a single commit. Don't put unrelated changes in the same commit. Don't make a commit for every single typo fix if it can be squashed or grouped.
