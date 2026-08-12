# 02 Git Commands
## Day 6 — `02_Git_Commands.md`

Save as:

```text
Day_6_Git_GitHub/
└── 02_Git_Commands.md
```

````markdown
# 02 Git Commands

## 1. Check Git

```bash
git --version
````

## 2. Initialize Repository

```bash
git init
```

## 3. Check Status

```bash
git status
```

## 4. Add One File

```bash
git add filename.py
```

## 5. Add All Files

```bash
git add .
```

## 6. Commit

```bash
git commit -m "Add Python files"
```

## 7. View Commits

```bash
git log
```

Short log:

```bash
git log --oneline
```

## 8. See Changes

```bash
git diff
```

## 9. Remove File from Git

```bash
git rm filename.py
```

## 10. Rename File

```bash
git mv old.py new.py
```

## 11. Check Remote

```bash
git remote -v
```

## 12. Add Remote

```bash
git remote add origin <repository-url>
```

## 13. Push Code

```bash
git push -u origin main
```

## 14. Pull Code

```bash
git pull origin main
```

## Basic Workflow

```text
git status
     ↓
git add .
     ↓
git commit -m "message"
     ↓
git push
```

## Practice

Run these commands:

```bash
git status
git add .
git commit -m "Practice Git commands"
git log --oneline
```

```
```
