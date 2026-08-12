# 03 GitHub Basics
## Day 6 — `03_GitHub_Basics.md`

Save as:

```text
Day_6_Git_GitHub/
└── 03_GitHub_Basics.md
```

````markdown
# 03 GitHub Basics

## What is GitHub?

GitHub is a cloud platform where developers
store and collaborate on Git repositories.

Git → Version control

GitHub → Online platform for Git repositories


## 1. Create a GitHub Repository

Go to GitHub and create a new repository.

Example:

```text
AI_Bootcamp
````

Do not add files if your project already exists locally.

## 2. Connect Local Project to GitHub

Open your project folder:

```bash
cd AI_Bootcamp
```

Initialize Git:

```bash
git init
```

Add files:

```bash
git add .
```

Commit:

```bash
git commit -m "Initial commit"
```

## 3. Add GitHub Remote

Copy your GitHub repository URL.

Then:

```bash
git remote add origin <repository-url>
```

Check remote:

```bash
git remote -v
```

## 4. Push Code to GitHub

If your branch is called main:

```bash
git branch -M main
```

Push:

```bash
git push -u origin main
```

## 5. Future Updates

After making changes:

```bash
git add .
```

```bash
git commit -m "Update project"
```

```bash
git push
```

## 6. Clone a Repository

To download an existing GitHub repository:

```bash
git clone <repository-url>
```

Example:

```bash
git clone https://github.com/username/project.git
```

## 7. Pull Latest Changes

Download the latest changes:

```bash
git pull
```

## Basic GitHub Workflow

```text
Local Project
     ↓
git add .
     ↓
git commit
     ↓
git push
     ↓
GitHub Repository
```

## Important Commands

```bash
git remote -v
git push
git pull
git clone
```

## Practice

Create a GitHub repository called:

```text
AI_Bootcamp
```

Then connect your local project:

```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin <repository-url>
git push -u origin main
```
