# Python Frameworks & Libraries Learning

A multi-purpose repository of [marimo](https://marimo.io) notebooks for exploring and learning Python libraries and frameworks.

## Repository Organization

All learning materials live under the `notebooks/` directory, grouped first by **library/framework** and then by **numbered topic or module**:

```text
.
├── notebooks/
│   └── <framework>/                  # One directory per library or framework
│       ├── README.md                 # Framework-specific notes, setup, and tooling
│       └── <NN_topic>/               # Numbered lesson/topic folder (e.g., 00_intro)
│           ├── <topic>.py            # Marimo notebook
│           ├── data/                 # Optional local datasets for this notebook
│           ├── layouts/              # Optional marimo layout configurations
│           └── __marimo__/           # Marimo session cache
├── pyproject.toml                    # Shared project configuration and dependencies
├── uv.lock                           # Locked environment dependencies
└── README.md                         # Top-level repository guide
```

### Currently Included Frameworks

- **[LadybugDB](notebooks/ladybug/README.md)** (`notebooks/ladybug/`) — Embedded graph database (`00_intro/intro.py`).

## Standards for Adding New Notebooks

1. **Folder structure**: Create a folder for the library under `notebooks/<framework>/` and organize individual notebooks into numbered subdirectories (e.g., `notebooks/<framework>/00_intro/intro.py`, `notebooks/<framework>/01_advanced/advanced.py`) so each notebook is self-contained with its own local `data/`, artifacts, and marimo metadata.
2. **Relative paths in notebooks**: Never hardcode paths relative to the repository root. Instead, resolve paths relative to the notebook's own directory using `mo.notebook_dir()`:
   ```python
   from pathlib import Path
   import marimo as mo

   NOTEBOOK_DIR = mo.notebook_dir() or Path(__file__).resolve().parent
   DATA_DIR = NOTEBOOK_DIR / "data"
   ```
3. **Framework-specific documentation**: Place any external service commands (such as Docker containers or database explorers) in `notebooks/<framework>/README.md`.

## Working with Notebooks (marimo)

Open the marimo file picker in your browser:

```bash
uv run marimo edit
```

Create or edit a specific notebook:

```bash
uv run marimo edit notebooks/<framework>/<NN_topic>/<notebook>.py
# Example:
uv run marimo edit notebooks/ladybug/00_intro/intro.py
```

Run a notebook as a read-only web app:

```bash
uv run marimo run notebooks/ladybug/00_intro/intro.py
```

Execute a notebook directly as a Python script:

```bash
uv run notebooks/ladybug/00_intro/intro.py
```

Validate all notebooks in the repository:

```bash
uv run marimo check --strict .
```

## Managing Dependencies

Dependencies are managed across the workspace with [uv](https://docs.astral.sh/uv/):

```bash
uv add <package>      # Add a library/framework to pyproject.toml and uv.lock
uv remove <package>   # Remove a dependency
uv sync               # Sync .venv with uv.lock
```
