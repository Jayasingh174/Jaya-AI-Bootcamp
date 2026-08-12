# 09 Practice
# Day 6 — `09_Practice.md`

Save as:

```text
Day_6_Git_GitHub/
└── 09_Practice.md
```

````markdown
# 09 GitHub Practice

# Day 6 - Final Git & GitHub Challenge


## Project

Create a GitHub repository:

```text
AI_Bootcamp
````

Your goal is to upload your complete
Python Bootcamp project to GitHub.

# 1. Initialize Git

Open your project folder:

```bash
cd AI_Bootcamp
```

Initialize Git:

```bash
git init
```

# 2. Create .gitignore

Create:

```text
.gitignore
```

Add:

```text
venv/
.venv/
.env
__pycache__/
*.pyc
.vscode/
.DS_Store
```

# 3. Check Status

```bash
git status
```

# 4. Add Files

```bash
git add .
```

# 5. First Commit

```bash
git commit -m "Initial AI Bootcamp project"
```

# 6. Connect GitHub

Create a GitHub repository called:

```text
AI_Bootcamp
```

Then connect it:

```bash
git remote add origin <repository-url>
```

# 7. Rename Branch

```bash
git branch -M main
```

# 8. Push to GitHub

```bash
git push -u origin main
```

# 9. Create Feature Branch

Create a new branch:

```bash
git switch -c feature-student-system
```

# 10. Make Changes

Modify or create:

```text
Projects/
└── Student_Management_System/
```

Add your Python code.

# 11. Commit Changes

```bash
git add .
```

```bash
git commit -m "Add student management system"
```

# 12. Push Feature Branch

```bash
git push -u origin feature-student-system
```

# 13. Create Pull Request

On GitHub create:

```text
feature-student-system
        ↓
       main
```

Add:

```text
Title:
Add Student Management System

Description:
Added a terminal-based Student Management System
using Python.
```

# 14. Review and Merge

Review your Pull Request.

Then merge it into:

```text
main
```

# 15. Update Local Main

```bash
git switch main
```

```bash
git pull origin main
```

# 16. Verify

Check:

```bash
git status
```

Check branches:

```bash
git branch
```

Check commits:

```bash
git log --oneline
```

# Final Workflow

```text
Create Project
      ↓
git init
      ↓
.gitignore
      ↓
git add .
      ↓
git commit
      ↓
GitHub
      ↓
git push
      ↓
Create Branch
      ↓
Write Code
      ↓
Commit
      ↓
Push Branch
      ↓
Pull Request
      ↓
Code Review
      ↓
Merge
      ↓
git pull
```

# Final Checklist

* [ ] Git installed
* [ ] Git configured
* [ ] Repository created
* [ ] .gitignore created
* [ ] Project committed
* [ ] GitHub connected
* [ ] Code pushed
* [ ] Feature branch created
* [ ] Feature committed
* [ ] Pull Request created
* [ ] Pull Request merged
* [ ] Main branch updated

# Interview Questions

## 1. What is Git?

Git is a version control system used
to track changes in code.

## 2. What is GitHub?

GitHub is a platform for hosting and
collaborating on Git repositories.

## 3. What is a commit?

A commit is a saved snapshot of changes.

## 4. What is a branch?

A branch is an independent line of development.

## 5. What is a Pull Request?

A Pull Request is a request to merge
changes from one branch into another.

## 6. What is .gitignore?

`.gitignore` tells Git which files
should not be tracked.

## 7. Difference between git pull and git push?

git pull → Downloads changes

git push → Uploads changes

# Final Challenge

Push your complete AI Bootcamp project
to GitHub.

Your repository should contain:

```text
AI_Bootcamp/
│
├── Day_1_Python_Basics/
├── Day_2_Control_Flow/
├── Day_3_OOP/
├── Day_4_Exception_Handling/
├── Day_5_File_Handling/
├── Day_6_Git_GitHub/
│
├── Projects/
│   ├── Calculator/
│   ├── Student_Management_System/
│   └── AI_Assistant/
│
└── .gitignore
```

# Success Criteria

Your project should be:

1. On GitHub
2. Properly committed
3. Using branches
4. Using Pull Requests
5. Using .gitignore
6. Organized professionally

````

### Day 6 is complete ✅

```text
Day 6 — Git & GitHub

01 Git Basics        ✅
02 Git Commands      ✅
03 GitHub Basics     ✅
04 Branches          ✅
05 Merge             ✅
06 Pull Request      ✅
07 Git Ignore        ✅
08 GitHub Workflow   ✅
09 Practice          ✅
````

**Days 1–6 of the Python foundation are now complete.**
