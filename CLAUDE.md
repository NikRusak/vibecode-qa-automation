# Vibe Coding QA Automation Workshop

## Communication & Workflow Rules

1. **Always communicate in Russian** during workshop sessions.

2. **Input/Output Directory Protocol**
   - Never modify or delete files in `input` directories
   - Always save generated files to `output` directories
   - Input directories contain reference data and test fixtures

3. **Virtual Environment Requirement**
   - Always use a Python virtual environment for this project
   - Activate venv before running any Python code
   - Add `venv/` to `.gitignore`

4. **Code Quality Before Commits**
   - Run `ruff check` and `mypy` linters before committing any code
   - Ensure all linting passes before creating commits
   - Document any linter exceptions in comments with reasoning

## Workshop Modules

- **Module 2**: Bulk Renamer - CSV-driven file renaming automation
- **Module 3**: TDD API Diff - JSON comparison and diffing
- **Module 4**: CLI Debugging - Troubleshooting broken Python scripts
- **Module 5**: Homework Anonymizer - PII anonymization with CSV processing
