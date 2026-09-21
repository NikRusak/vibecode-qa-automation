# Git Safety & Workflow

## Before Committing

1. **Always run git status**
   - Check for unintended files or changes
   - Verify staging area contains only intentional changes

2. **Always run git diff**
   - Review all staged and unstaged changes
   - Ensure no secrets, credentials, or sensitive data are being committed

3. **Request Permission**
   - Pause and ask for user approval before creating any commit
   - Show summary of what will be committed

## Commit Message Format

Follow Conventional Commits specification:
- `feat:` for new features
- `fix:` for bug fixes
- `refactor:` for code refactoring
- `test:` for test additions/changes
- `docs:` for documentation
- `chore:` for maintenance tasks

Example: `feat: implement bulk file renamer with CSV mapping`

## Undo Operations

On "undo" or "revert" requests:
- Use `git restore` for unstaged changes
- Use `git restore --staged` for staged changes
- Use `git reset HEAD~1` only with explicit user approval
- Never use `--hard` flag without explicit confirmation

## Safe Workflows

- Create feature branches before significant changes
- Keep commits atomic and focused
- Use `.gitignore` to exclude generated outputs and sensitive files
