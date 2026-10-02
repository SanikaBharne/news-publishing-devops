# Repository Structure

The following is the actual, clean repository structure established in Week 4.

```
project-root/
│
├── src/
│   └── app.py
│
├── docs/
│   ├── week-01/
│   │   ├── problem-definition.md
│   │   └── (other Week 1 docs...)
│   ├── week-02/
│   │   ├── agile-plan.md
│   │   └── (other Week 2 docs...)
│   ├── week-03/
│   │   ├── system-architecture.md
│   │   └── (other Week 3 docs...)
│   ├── week-04/
│   │   ├── branching-strategy.md
│   │   ├── git-setup.md
│   │   └── (other Week 4 docs...)
│   └── evidence/
│       ├── week-02/
│       ├── week-03/
│       └── week-04/
│
├── .gitignore
├── requirements.txt
└── README.md
```

## Folder Explanations
*   **`src/`**: Contains the actual application source code. Currently holds the minimal Flask `app.py` skeleton.
*   **`docs/`**: Contains all project planning, architecture, and weekly deliverables, organized by week.
*   **`docs/evidence/`**: Contains checklists and (eventually) screenshots proving the completion of tasks.
*   **`requirements.txt`**: Lists Python dependencies (Flask, pytest).
*   **`.gitignore`**: Defines files that Git should not track.
*   **`README.md`**: The professional front-page of the repository.

*Note: Folders for tests, templates, and Ansible will be created in future weeks when development begins.*
