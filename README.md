# Vibe Coding for QA Automation

Hands-on workshop material that teaches QA engineers how to build test automation with an AI coding agent ([Claude Code](https://docs.anthropic.com/en/docs/claude-code)). Each module is a small, self-contained exercise: the engineer describes the task, the agent writes the code, and the engineer reviews, tests and corrects it.

The goal isn't the scripts themselves. It's the workflow: giving the agent the right context, splitting work across subagents, keeping it inside guardrails, and never trusting output you haven't tested.

## What the workshop covers

| Module | Folder | What you practice |
|---|---|---|
| Project rules | [`CLAUDE.md`](CLAUDE.md) | Setting persistent rules for the agent: input/output folder protocol, virtual env, linters before every commit |
| Skills | [`.claude/skills/git-skill.md`](.claude/skills/git-skill.md) | Teaching the agent a safe Git workflow: review the diff, ask before committing, Conventional Commits, safe undo |
| Subagents | [`.claude/agents/`](.claude/agents) | Two specialized subagents, an **implementer** and a **tester**, each running on a smaller model (Claude Haiku). Result: [`string_reversal.py`](string_reversal.py) with a 15-case test suite in [`test_string_reversal.py`](test_string_reversal.py) |
| Bulk renamer | [`demo_renamer/`](demo_renamer) | CSV-driven automation: renaming test-run screenshots to test-case IDs |
| TDD API diff | [`demo_api_diff/`](demo_api_diff) | Test-driven development with an agent: a recursive JSON diff for comparing API responses (baseline vs current) |
| CLI debugging | [`demo_debugging/`](demo_debugging) | Using the agent to diagnose and fix a deliberately broken script |
| Requirements extraction | [`demo_subagents/`](demo_subagents) | Turning a noisy meeting transcript into clean, testable requirements |
| Parallel agents | [`demo_parallel_agents/`](demo_parallel_agents) | Running several agents in parallel to derive test cases from two specs (authentication, checkout) |
| Homework: anonymizer | [`hw_anonymizer/`](hw_anonymizer) | Anonymizing PII in a CSV file, as practice for safe test-data handling |

## Getting started

```bash
git clone https://github.com/NikRusak/vibecode-qa-automation.git
cd vibecode-qa-automation
python3 -m venv venv && source venv/bin/activate
pip install pytest pillow ruff mypy
cp .env.example .env

# run the example test suite
python -m pytest test_string_reversal.py -v
```

Then open the folder in Claude Code and work through the modules. The rules in `CLAUDE.md` and the skill in `.claude/skills/` load automatically. Files in `input/` folders are reference data and are never modified; generated results go to `output/`.

## Principles taught

- **Context first.** Project rules, skills and clear specs reduce rework more than clever prompts do.
- **Split the work.** Separate agents for implementation and testing catch more problems than one agent doing both.
- **Guardrails over trust.** Linters, tests and a reviewed diff before every commit.
- **Test everything the agent produces.** AI-generated code is reviewed and tested like any other code.

## Author

Nik Rusak, AI Engineer and SDET. [LinkedIn](https://www.linkedin.com/in/nik-rusak-657941136)
