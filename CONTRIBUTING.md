# Contributing to Code Academy

Thank you for your interest in contributing to Code Academy.

## Before you contribute

1. Read the project README and understand the area you want to change.
2. Check existing issues and pull requests to avoid duplicate work.
3. Discuss major features or architectural changes with the maintainers before starting.
4. Do not work on an issue assigned to someone else without checking first.

## Contribution workflow

1. Fork the repository if you do not have direct contributor access.
2. Create a branch from the project's main development branch.
3. Make focused changes that address one issue or feature.
4. Run relevant tests and checks.
5. Update documentation if behaviour, setup, or configuration changes.
6. Open a pull request explaining what changed, why, and how you tested it.

Suggested branch names:
- `feature/course-progress`
- `fix/video-playback`
- `docs/update-setup-guide`

## Code standards

- Follow the conventions already used in the codebase.
- Use clear names and write maintainable code.
- Handle errors deliberately.
- Avoid unnecessary dependencies and unrelated refactoring.
- Do not commit build output, secrets, credentials, or local environment files.
- Never commit `.env` files, API keys, access tokens, passwords, private keys, or service-account credentials.
- Never include real student or user data in examples, tests, logs, or screenshots.

## Security and privacy

Do not weaken authentication, authorization, access-code validation, or other security controls. Do not expose student information, email addresses, phone numbers, access codes, or other private data.

If you discover a possible vulnerability, do not create a public issue. Follow [SECURITY.md](SECURITY.md).

## Pull request checklist

- [ ] The change has a clear purpose.
- [ ] The code follows existing project conventions.
- [ ] Relevant tests and checks have been run.
- [ ] Documentation has been updated where needed.
- [ ] No secrets or private user data are included.
- [ ] New dependencies are justified.
- [ ] The pull request explains how the change was tested.

## Bugs and feature requests

For bugs, include the expected behaviour, actual behaviour, steps to reproduce, and relevant error messages. Remove secrets and personal information from logs and screenshots.

## Review

Submitting a contribution does not guarantee acceptance or merging. Maintainers may request changes or close contributions that do not fit the project's goals, quality standards, or security requirements.

Thank you for helping improve Code Academy.
