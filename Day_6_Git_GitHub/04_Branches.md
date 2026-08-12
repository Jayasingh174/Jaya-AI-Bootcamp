# 04 Branches
## Day 6 — `04_Branches.md`

Save as:

```text
Day_6_Git_GitHub/
└── 04_Branches.md
```

````markdown
# 04 Branches

## What is a Branch?

A branch is a separate line of development.

It allows developers to work on features
without changing the main code.

Example:

```text
main
 │
 ├── feature-login
 │
 └── feature-payment
````

## 1. Check Current Branch

```bash
git branch
```

## 2. Create a Branch

```bash
git branch feature-login
```

## 3. Switch Branch

```bash
git switch feature-login
```

## 4. Create and Switch

```bash
git switch -c feature-login
```

## 5. List Branches

```bash
git branch
```

## 6. Switch Back to Main

```bash
git switch main
```

## 7. Delete a Branch

```bash
git branch -d feature-login
```

## 8. Push Branch to GitHub

```bash
git push -u origin feature-login
```

## Branch Workflow

```text
main
 ↓
create branch
 ↓
feature-login
 ↓
write code
 ↓
git add .
 ↓
git commit
 ↓
git push
```

## Real-World Example

A team is building an AI Assistant.

```text
main
 │
 ├── feature-chat
 ├── feature-auth
 └── feature-rag
```

Each developer can work on a
separate feature.

## Key Commands

```bash
git branch
git branch feature-name
git switch feature-name
git switch -c feature-name
git switch main
git branch -d feature-name
git push -u origin feature-name
```

## Practice

Create a branch:

```bash
git switch -c feature-student
```

Create or modify a file.

Then:

```bash
git add .
git commit -m "Add student feature"
git push -u origin feature-student
```

```
```
