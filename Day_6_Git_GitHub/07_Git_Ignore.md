# 07 Git Ignore
## Day 6 — `07_Git_Ignore.md`

Save as:

```text
Day_6_Git_GitHub/
└── 07_Git_Ignore.md
```

````markdown
# 07 Git Ignore

## What is .gitignore?

`.gitignore` is a file that tells Git which
files and folders should NOT be tracked.

Common examples:

- Virtual environments
- Passwords
- API keys
- Temporary files
- Cache files
- IDE files


## 1. Create .gitignore

In your project root:

```text
.gitignore
````

## 2. Ignore a File

Example:

```text
.env
```

Git will ignore the `.env` file.

## 3. Ignore a Folder

Example:

```text
venv/
```

This ignores the entire virtual environment.

## 4. Python .gitignore

Example:

```text
# Virtual environment
venv/

# Environment variables
.env

# Python cache
__pycache__/

# Compiled Python files
*.pyc

# IDE
.vscode/

# macOS
.DS_Store
```

## 5. AI Project Example

For an AI project:

```text
venv/
.env
__pycache__/
*.pyc
.vscode/
```

You should NOT upload API keys.

For example, do NOT commit:

```text
OPENAI_API_KEY=your-secret-key
```

Instead, keep it in:

```text
.env
```

## 6. Check Git Status

```bash
git status
```

Ignored files should not normally appear
as untracked files.

## 7. Add and Commit

```bash
git add .
```

```bash
git commit -m "Add gitignore"
```

## 8. Important

If a file was already committed before adding
it to `.gitignore`, Git will continue tracking it.

For example:

```bash
git rm --cached .env
```

Then:

```bash
git add .
git commit -m "Remove env file from tracking"
```

## Recommended AI Project .gitignore

```text
# Environment
.env
.env.*

# Virtual environment
venv/
.venv/

# Python
__pycache__/
*.pyc

# IDE
.vscode/
.idea/

# OS
.DS_Store

# Logs
*.log
```

## Key Point

```text
.gitignore
    ↓
Tell Git what NOT to track
```

## Practice

Create a `.gitignore` file.

Add:

```text
venv/
.env
__pycache__/
*.pyc
.vscode/
```

Then run:

```bash
git status
```
