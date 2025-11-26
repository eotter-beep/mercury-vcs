# Mercury VCS

Mercury VCS is a lightweight, beginner-friendly version control system with features Git doesn’t natively provide. It focuses on **simplicity, workflow control, and commit rules enforcement** for teams or solo developers.

---

## **Features**

- **Commit Rules Enforcement** – Define rules for commit messages or file structures to maintain a clean and consistent repository.
- **Simplified Versioning** – Create unique versions with `new-ver` and automatically prevent duplicates.
- **Beginner-Friendly CLI** – Commands are easy to remember and use:
  - `commit <file>` – Save a file (or files) to Mercury.
  - `commit-msg <message>` – Add a commit message (supports spaces).
  - `restart-branch <branch>` – Restart a branch quickly.
  - `list-ver` – List all repository versions.
  - `newrule <message>` – Create a `commitrules.txt` file.
  - `new-ver <version>` – Create a new Mercury version.
  - `version` – Show Mercury VC version info.
  - `--ignore-unique` – Ignore Uniqueness, only avaliable in `new-ver`
- **Lightweight and Focused** – Avoids Git complexity while still providing essential version control functionality.