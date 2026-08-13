# 06 Pull Request
## Day 6 — `06_Pull_Request.md`

Save as:

```text
Day_6_Git_GitHub/
└── 06_Pull_Request.md
```

````markdown id="8z7v8x"
# 06 Pull Request

## What is a Pull Request?

A Pull Request (PR) is a request to merge
changes from one branch into another branch.

Usually:

```text
feature branch
      ↓
Pull Request
      ↓
main branch
````

A PR allows the team to:

* Review code
* Discuss changes
* Find bugs
* Approve changes
* Merge code

## 1. Create a Feature Branch

```bash id="q9h9we"
git switch -c feature-login
```

## 2. Make Changes

Create or modify your code.

Example:

```text
login.py
```

## 3. Check Changes

```bash id="xj9n7w"
git status
```

## 4. Add Changes

```bash id="p8h5jd"
git add .
```

## 5. Commit Changes

```bash id="j4c0q1"
git commit -m "Add login feature"
```

## 6. Push Branch

```bash id="w0i1j8"
git push -u origin feature-login
```

## 7. Create Pull Request

Go to your GitHub repository.

GitHub will usually show:

```text
Compare & pull request
```

Click it.

Select:

```text
base: main
compare: feature-login
```

Add:

```text
Title:
Add login feature

Description:
Implemented user login functionality.
```

Then click:

```text
Create pull request
```

## 8. Code Review

A team member reviews the code.

They can:

* Approve
* Request changes
* Comment

## 9. Merge Pull Request

After approval:

```text
Merge pull request
```

Then:

```text
Confirm merge
```

## 10. Update Local Main

After the PR is merged:

```bash id="wqf6l8"
git switch main
```

Pull the latest code:

```bash id="2r8k0b"
git pull origin main
```

## Complete PR Workflow

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
 ↓
GitHub
 ↓
Pull Request
 ↓
Code Review
 ↓
Approval
 ↓
Merge
 ↓
main
```

## Real-World Example

For an AI Assistant project:

```text
main
 │
 ├── feature-chat
 ├── feature-auth
 └── feature-rag
```

A developer works on:

```text
feature-rag
```

Then creates a Pull Request:

```text
feature-rag → main
```

## Key Commands

```bash id="4p8qf3"
git switch -c feature-name
git add .
git commit -m "Add feature"
git push -u origin feature-name
git switch main
git pull origin main
```

## Practice

Create:

```bash id="zq5h0f"
git switch -c feature-profile
```

Make a change.

Then:

```bash id="f6v7jq"
git add .
git commit -m "Add profile feature"
git push -u origin feature-profile
```

Go to GitHub and create a Pull Request:

```text
feature-profile → main
```

```
```
