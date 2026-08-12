# 08 GitHub Workflow
## Day 6 — `08_GitHub_Workflow.md`

Save as:

```text
Day_6_Git_GitHub/
└── 08_GitHub_Workflow.md
```

````markdown
# 08 GitHub Workflow

## What is GitHub Workflow?

GitHub Workflow is the process developers
follow to work on a project using Git and GitHub.

Basic workflow:

```text
Clone
  ↓
Branch
  ↓
Code
  ↓
Add
  ↓
Commit
  ↓
Push
  ↓
Pull Request
  ↓
Code Review
  ↓
Merge
````

---

## 1. Clone Repository

Download the project:

```bash
git clone <repository-url>
```

Move into the project:

```bash
cd project-name
```

---

## 2. Check Status

```bash
git status
```

---

## 3. Get Latest Changes

Before starting work:

```bash
git pull origin main
```

---

## 4. Create Feature Branch

```bash
git switch -c feature-login
```

---

## 5. Write Code

Example:

```text
login.py
```

---

## 6. Check Changes

```bash
git status
```

See exact changes:

```bash
git diff
```

---

## 7. Add Changes

```bash
git add .
```

---

## 8. Commit Changes

```bash
git commit -m "Add login feature"
```

---

## 9. Push Branch

```bash
git push -u origin feature-login
```

---

## 10. Create Pull Request

On GitHub:

```text
feature-login → main
```

Create the Pull Request.

---

## 11. Code Review

Team members review the code.

They can:

* Comment
* Approve
* Request changes

---

## 12. Merge

After approval:

```text
Merge Pull Request
```

---

## 13. Update Local Main

Switch to main:

```bash
git switch main
```

Pull latest code:

```bash
git pull origin main
```

---

# Real-World AI Project Workflow

Suppose the team is building an:

```text
AI Assistant
```

Branches:

```text
main
 │
 ├── feature-chat
 ├── feature-auth
 ├── feature-rag
 └── feature-api
```

Developer works on:

```text
feature-rag
```

Then:

```bash
git add .
git commit -m "Implement RAG pipeline"
git push -u origin feature-rag
```

Create:

```text
Pull Request
feature-rag → main
```

After review:

```text
Approve → Merge
```

---

# Daily Developer Workflow

Use this every day:

```bash
git switch main
git pull origin main
git switch -c feature-name
```

Work on your code.

Then:

```bash
git status
git add .
git commit -m "Describe your changes"
git push -u origin feature-name
```

Create a Pull Request on GitHub.

---

# Key Commands

```bash
git clone
git status
git pull
git branch
git switch
git add
git commit
git push
git diff
```

---

# Important Rule

Never work directly on `main`
for a team project.

Prefer:

```text
main
 ↓
feature branch
 ↓
Pull Request
 ↓
Code Review
 ↓
Merge
```

---

# Practice

Create a complete workflow:

```bash
git clone <repository-url>

cd project-name

git pull origin main

git switch -c feature-student

# Make your changes

git status

git add .

git commit -m "Add student feature"

git push -u origin feature-student
```

Then create a Pull Request on GitHub.

````

```text
01 Git Basics       ✅
02 Git Commands     ✅
03 GitHub Basics    ✅
04 Branches         ✅
05 Merge            ✅
06 Pull Request     ✅
07 Git Ignore       ✅
08 GitHub Workflow  ✅
09 Practice         ⏭️
````

