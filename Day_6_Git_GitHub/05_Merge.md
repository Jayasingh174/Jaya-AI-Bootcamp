# 05 Merge
## Day 6 — `05_Merge.md`

Save as:

```text
Day_6_Git_GitHub/
└── 05_Merge.md
```

````markdown
# 05 Merge

## What is Merge?

Merge combines changes from one branch
into another branch.

Example:

```text
feature-login
      ↓
    merge
      ↓
main
````

---

## 1. Check Branch

```bash
git branch
```

---

## 2. Switch to Main

```bash
git switch main
```

---

## 3. Merge a Branch

```bash
git merge feature-login
```

Now the changes from `feature-login`
are added to `main`.

---

## 4. Push the Merge

```bash
git push origin main
```

---

## 5. Delete Branch

After merging:

```bash
git branch -d feature-login
```

---

## Complete Workflow

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
switch main
 ↓
git merge feature-login
 ↓
git push
```

---

## 6. Merge Conflict

A merge conflict happens when two branches
modify the same part of a file differently.

Example:

```text
<<<<<<< HEAD
Main code
=======
Feature code
>>>>>>> feature-login
```

You must manually decide which code
should remain.

---

## 7. After Fixing Conflict

Add the file:

```bash
git add .
```

Commit the resolution:

```bash
git commit -m "Resolve merge conflict"
```

Push:

```bash
git push
```

---

## Key Commands

```bash
git switch main
git merge feature-login
git push origin main
git branch -d feature-login
```

---

## Practice

Create a branch:

```bash
git switch -c feature-test
```

Make a change and commit:

```bash
git add .
git commit -m "Add test feature"
```

Switch to main:

```bash
git switch main
```

Merge:

```bash
git merge feature-test
```

Push:

```bash
git push origin main
```

```
```
Unmute okay to use on ceremony,movement