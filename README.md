# Propose:
This repository is designed so stakeholders can experience and validate the automated features of our internal GitHub Bot.
By creating a Pull Request (PR) and running the test workflow, you will see how the bot reacts when unit tests pass or fail.

## 🎯 What this demo showcases
When a PR is opened or updated, the bot automatically performs:

- ✅ Unit Test & Test Coverage Reporting
Runs all tests in the PR
Reports how many passed and failed
Shows failing test names and duration
Calculates coverage % per file
Posts a detailed comment in the PR

- 🐞 Automatic Issue Creation
If tests fail:
The bot detects the failure
Creates a GitHub Issue
Includes failure details for debugging

- 🔍 PR Review Automation
The bot can:
Add review comments
Suggest corrections

(Only enabled in selected environments)
- 🔔 Slack Alerting
If enabled for your team:
