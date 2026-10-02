# Definition of Done (DoD)

## Project-Level Definition of Done
A task should only be considered DONE when:
- The requirement is fully implemented.
- Code/configuration follows project conventions.
- All code/scripts are committed to Git (GitHub).
- Peer check / instructor review completed (where applicable).
- Continuous Integration Build succeeds without errors.
- Related documentation is updated.
- Acceptance criteria are strictly satisfied.
- No known blocking defects exist.
- Evidence/screenshot is captured in the `docs/evidence/` folder when required.

## Application Features Definition of Done
- Feature matches the MVP scope exactly (no extra/unapproved features).
- Manual testing passes on the local machine.
- Automated UI tests (once implemented) pass successfully.

## DevOps Pipeline Definition of Done
- Tool is installed and securely configured.
- Pipeline code (e.g., Jenkinsfile) is version-controlled.
- Pipeline accurately executes the required stage (Build, Test, Deploy).
- Pipeline fails securely (it blocks deployment if prior steps fail).
- Deployment environments are reproducible via code.

## Documentation Definition of Done
- Markdown files are properly formatted and grammatically correct.
- Stored in the correct `docs/week-XX/` directory.
- Reviewed and approved against the week's requirements.
