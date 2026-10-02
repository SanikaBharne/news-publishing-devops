# Setup Verification

The following checks were performed during Week 3 to verify the local development environment.

| Check | Command / Action | Expected Result | Actual Result | Status |
|---|---|---|---|---|
| Python installed | `python --version` | Python 3.x | Python 3.14.7 | ✅ PASS |
| pip installed | `pip --version` | pip 2x.x | pip 26.2.1 | ✅ PASS |
| Git installed | `git --version` | git version 2.x | git version 2.52.0.windows.1 | ✅ PASS |
| Dependencies install | `pip install -r requirements.txt` | Flask and pytest install successfully | Flask 3.1.3 and pytest 9.1.1 installed | ✅ PASS |
| Flask available | `pip show flask` | Flask version shown | Flask 3.1.3 | ✅ PASS |
| pytest available | `pip show pytest` | pytest version shown | pytest 9.1.1 | ✅ PASS |
| Application starts | `python src/app.py` | Flask server starts on port 5000 | Running on http://127.0.0.1:5000 | ✅ PASS |
| Health endpoint | `curl http://127.0.0.1:5000/health` | JSON response with status ok | `{"message":"News Publishing Workflow MVP running","status":"ok"}` | ✅ PASS |
| Database connection | N/A | N/A (SQLite not yet created) | Not applicable for Week 3 | ⏳ DEFERRED |

## Notes
- The database (SQLite) will be created during Week 5-6 feature development. There is nothing to verify yet.
- All PASS results above were obtained from actual command execution, not invented.
