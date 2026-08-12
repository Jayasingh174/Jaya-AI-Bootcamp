# 06 Pull Request

> **“I made some changes in my branch. Please review them and, if they're good, merge them into another branch.”**

A PR is mainly a **GitHub collaboration and code-review feature**. Git itself has branches and commits; GitHub adds the Pull Request workflow.

---

## 1. Why do we need Pull Requests?

Imagine a project has this structure:

```text
main
│
├── app.py
├── database.py
└── README.md
```

Suppose you want to add a login feature.

You **shouldn't directly modify `main`** in a team environment.

Instead:

```text
main
  │
  └── feature/login
          │
          ├── login.py
          ├── changes to app.py
          └── commits
```

Then you create a Pull Request:

```text
feature/login
      │
      │ Pull Request
      ▼
    main
```

The team can review your changes before they become part of `main`.

---

# 2. Pull Request vs Git Pull

This is one of the most important concepts.

### `git pull`

A Git command:

```bash
git pull
```

It means:

> Download changes from a remote repository and integrate them into your current local branch.

### Pull Request

A GitHub feature:

> Request that your branch's changes be reviewed and merged into another branch.

So:

```text
git pull       → Git command
Pull Request   → GitHub collaboration/review process
```

They are **not the same thing**.

---

# 3. Basic Pull Request Workflow

The standard workflow looks like this:

```text
1. Clone repository
       ↓
2. Create branch
       ↓
3. Make changes
       ↓
4. Commit changes
       ↓
5. Push branch
       ↓
6. Create Pull Request
       ↓
7. Code Review
       ↓
8. Fix requested changes
       ↓
9. Approval
       ↓
10. Merge
       ↓
11. Delete branch
```

Let's understand each step.

---

# 4. Step 1 — Clone the repository

Suppose the repository is:

```text
github.com/company/project
```

Clone it:

```bash
git clone https://github.com/company/project.git
```

Then:

```bash
cd project
```

---

# 5. Step 2 — Create a feature branch

Never work directly on `main` when following a team PR workflow.

```bash
git checkout -b feature/login
```

Modern Git also supports:

```bash
git switch -c feature/login
```

Now:

```text
main
  │
  └── feature/login
```

Your work happens on:

```text
feature/login
```

---

# 6. Step 3 — Make your changes

For example:

```text
login.py
```

You implement:

```python
def login(username, password):
    ...
```

Check what changed:

```bash
git status
```

You might see:

```text
modified: app.py
untracked: login.py
```

---

# 7. Step 4 — Commit your changes

Stage the files:

```bash
git add .
```

Then commit:

```bash
git commit -m "Add user login functionality"
```

Your local Git history now looks like:

```text
main
  │
  A
  │
  B
  │
  └── C  ← feature/login
```

---

# 8. Step 5 — Push the branch

Your branch currently exists locally.

Push it to GitHub:

```bash
git push -u origin feature/login
```

Now GitHub has:

```text
main
feature/login
```

---

# 9. Step 6 — Create the Pull Request

Go to GitHub.

You will usually see:

> Compare & pull request

Click it.

You'll select:

```text
base:    main
compare: feature/login
```

Meaning:

> Take the changes from `feature/login` and merge them into `main`.

This direction is extremely important.

```text
feature/login
      │
      │ PR
      ▼
     main
```

---

# 10. What does "base" mean?

Suppose GitHub shows:

```text
base: main
compare: feature/login
```

### Base

Where you want your changes to go.

```text
main
```

### Compare

The branch containing your changes.

```text
feature/login
```

Therefore:

> Compare `feature/login` against `main`, then merge the changes into `main`.

---

# 11. What happens inside a Pull Request?

A PR normally contains:

### Title

Example:

```text
Add user authentication
```

### Description

Explain:

* What did you change?
* Why did you change it?
* How did you test it?
* Are there any known limitations?

Example:

```text
## Changes

- Added login API
- Added password validation
- Added authentication middleware

## Testing

- Tested valid credentials
- Tested invalid credentials
- Tested missing password
```

---

# 12. PR Review

A teammate might review your code.

They could say:

> Please add validation for empty passwords.

You modify your code.

Then:

```bash
git add .
git commit -m "Add password validation"
git push
```

You **usually do not create another PR**.

The new commit automatically appears inside the existing PR.

```text
PR #15
│
├── Commit 1: Add login
├── Commit 2: Add password validation
└── Commit 3: Fix validation error
```

---

# 13. Approval

The reviewer may eventually click:

> Approve

Then the PR could look like:

```text
✓ Approved
✓ CI checks passed
✓ No merge conflicts
```

Now it can be merged.

---

# 14. Merging a Pull Request

GitHub commonly provides different merge strategies.

The major ones are:

### Merge commit

```text
A---B---C-------M
     \         /
      D---E---
```

The branches are joined with a merge commit.

---

### Squash and merge

Several commits become one:

```text
Before:

A---B---C
     \
      D---E---F

After:

A---B---C---S
```

Where `S` represents one squashed commit.

Example:

```text
Add login feature
```

This produces a cleaner main branch.

---

### Rebase and merge

History is rewritten so the commits appear directly on top of the target branch:

```text
A---B---C---D---E
```

This can produce a very linear history.

---

# 15. Merge Conflict

One of the most important advanced concepts.

Suppose you modify:

```text
app.py
```

Another developer also modifies the same part of:

```text
app.py
```

Git may not know which version should win.

You get:

```text
CONFLICT
```

Example:

```python
<<<<<<< HEAD
print("Hello")
=======
print("Hello User")
>>>>>>> feature/login
```

You manually decide what the final code should be.

Then:

```bash
git add app.py
git commit
```

or, depending on the merge/rebase workflow, continue the operation.

---

# 16. Keeping Your PR Updated

Suppose you created a PR yesterday.

Meanwhile, someone merged changes into `main`.

Your branch:

```text
main
A---B---C
```

Your branch:

```text
A---B---D
```

But now `main` has:

```text
A---B---C---E
```

Your branch doesn't contain `E`.

You can update your branch.

One common approach:

```bash
git checkout main
git pull origin main

git checkout feature/login
git merge main
```

Resolve conflicts if necessary, then:

```bash
git push
```

Your existing PR updates automatically.

---

# 17. Better approach: Rebase

Instead of merging `main` into your feature branch, you can rebase:

```bash
git checkout feature/login
git fetch origin
git rebase origin/main
```

Conceptually:

Before:

```text
A---B---C---E     main
     \
      D---F       feature
```

After rebase:

```text
A---B---C---E---D'---F'
```

Your commits are replayed on top of the latest `main`.

Because rebase changes commit history, be careful when rebasing branches other people are already using.

---

# 18. What is `origin`?

When you clone a repository:

```bash
git clone https://github.com/company/project.git
```

Git normally creates a remote named:

```text
origin
```

You can check:

```bash
git remote -v
```

Example:

```text
origin  https://github.com/company/project.git
origin  https://github.com/company/project.git
```

So:

```bash
git push origin feature/login
```

means:

> Push my `feature/login` branch to the remote named `origin`.

---

# 19. Pull Request in Open Source

Open-source projects commonly use **fork-based workflows**.

Suppose you don't have permission to push to:

```text
company/project
```

You create your own fork:

```text
company/project
       │
       ▼
your-account/project
```

Then:

```text
Fork
 ↓
Clone
 ↓
Create branch
 ↓
Make changes
 ↓
Commit
 ↓
Push
 ↓
Create PR
```

Your PR might be:

```text
your-account/project:feature/login
             │
             ▼
company/project:main
```

This is extremely common in open source.

---

# 20. `origin` vs `upstream`

In a fork workflow:

```text
origin
   ↓
your GitHub fork

upstream
   ↓
original project
```

For example:

```bash
git remote -v
```

might show:

```text
origin    https://github.com/jaya/project.git
upstream  https://github.com/company/project.git
```

You can get the original project's latest changes:

```bash
git fetch upstream
```

Then update your branch from:

```bash
upstream/main
```

---

# 21. Draft Pull Request

A **Draft PR** means:

> “I'm working on this, but it's not ready for final review yet.”

Useful when you want early feedback.

Example:

```text
Draft Pull Request
       ↓
Developer continues working
       ↓
Ready for review
       ↓
Mark as ready
```

---

# 22. PR Checks / CI/CD

Professional repositories often automatically run checks after you create or update a PR.

For example:

```text
Pull Request
     │
     ├── Unit tests
     ├── Linting
     ├── Type checking
     ├── Security scanning
     ├── Build
     └── Deployment checks
```

GitHub Actions can automate these checks.

Example:

```text
✓ Tests passed
✓ Lint passed
✓ Build passed
✗ Security scan failed
```

The team may prevent merging until the failed check is fixed.

---

# 23. Branch Protection

Companies often protect `main`.

For example:

```text
main
 │
 ├── Direct push ❌
 ├── PR required ✓
 ├── 1 approval required ✓
 ├── Tests required ✓
 └── Status checks required ✓
```

This prevents developers from accidentally breaking production code.

---

# 24. CODEOWNERS

Large repositories may use a `CODEOWNERS` file.

For example:

```text
/backend/    @backend-team
/frontend/   @frontend-team
/ml/         @ml-team
```

If you modify:

```text
/ml/model.py
```

GitHub can automatically request review from the ML team.

This is useful in large engineering organizations.

---

# 25. PR Best Practices

A good PR should be:

### Small

Avoid:

```text
PR #100

2,000 files changed
```

Prefer focused changes.

### Descriptive

Bad:

```text
fix stuff
```

Better:

```text
Fix authentication token expiration
```

### Tested

Explain how you tested your changes.

### Easy to review

Avoid mixing unrelated changes.

Bad:

```text
Login feature
+ database migration
+ UI redesign
+ 500 lines of formatting changes
```

Better:

```text
PR 1 → Login feature
PR 2 → Database migration
PR 3 → UI redesign
```

---

# 26. Good Branch Naming

Common patterns:

```text
feature/login
feature/payment-api

bugfix/login-error
bugfix/token-expiration

hotfix/payment-failure

docs/update-readme

refactor/authentication
```

For your AI engineering projects, you could use:

```text
feature/rag-pipeline
feature/fastapi-auth
feature/langgraph-agent
bugfix/vector-search
docs/api-documentation
```

---

# 27. A Real AI Engineer Example

Imagine you're building a RAG application.

Your main branch:

```text
main
```

You want to add FAISS retrieval.

Create:

```bash
git switch -c feature/faiss-retrieval
```

Implement the feature.

Then:

```bash
git status
git add .
git commit -m "Add FAISS document retrieval"
git push -u origin feature/faiss-retrieval
```

Create:

```text
PR #24
Add FAISS document retrieval
```

Reviewer says:

> Add tests for empty query handling.

You implement them:

```bash
git add .
git commit -m "Add empty query validation tests"
git push
```

Now PR #24 contains both commits.

Reviewer approves.

CI runs:

```text
✓ Unit tests
✓ API tests
✓ Lint
✓ Build
```

Then:

```text
Merge PR
```

Your feature becomes part of:

```text
main
```

---

# 28. Pull Request Mental Model

Remember this simple picture:

```text
                GitHub
                  │
       ┌──────────┴──────────┐
       │                     │
     main              feature/login
       │                     │
       │                     │
       │        commits      │
       │          ↓          │
       │       changes       │
       │                     │
       └─────── PR ──────────┘
                  │
             Code Review
                  │
             CI / Tests
                  │
              Approval
                  │
                Merge
                  │
                  ▼
                main
```

---

# 29. Commands You Should Know

### Create branch

```bash
git switch -c feature/login
```

### Check branch

```bash
git branch
```

### Check changes

```bash
git status
```

### Stage

```bash
git add .
```

### Commit

```bash
git commit -m "Add login feature"
```

### Push

```bash
git push -u origin feature/login
```

### Fetch remote changes

```bash
git fetch origin
```

### Pull

```bash
git pull origin main
```

### Merge

```bash
git merge main
```

### Rebase

```bash
git rebase main
```

### View history

```bash
git log --oneline --graph --all
```

---

# 30. Beginner → Advanced Learning Path

For your `Day_6_Git_GitHub`, I'd learn Pull Requests in this order:

```text
LEVEL 1 — Beginner
│
├── What is a Pull Request?
├── Branch vs PR
├── Base vs Compare
├── Create PR
└── Merge PR
│
LEVEL 2 — Intermediate
│
├── Code review
├── Review comments
├── Requested changes
├── Draft PR
├── Merge conflicts
└── Updating a PR
│
LEVEL 3 — Advanced
│
├── Merge commit
├── Squash merge
├── Rebase merge
├── Fork workflow
├── origin vs upstream
├── CI/CD checks
├── Branch protection
└── CODEOWNERS
│
LEVEL 4 — Professional
│
├── PR templates
├── Automated testing
├── GitHub Actions
├── Required approvals
├── Security checks
├── Release workflows
└── Production deployment
```

## The one sentence to remember

**A Pull Request is a request to review and integrate the changes from one branch into another branch.**

For a professional AI/software engineer workflow, the most important pattern is:

```text
main
 ↓
create feature branch
 ↓
write code
 ↓
commit
 ↓
push
 ↓
Pull Request
 ↓
review + CI tests
 ↓
fix feedback
 ↓
approval
 ↓
merge
 ↓
delete feature branch
```


