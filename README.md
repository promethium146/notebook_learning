# ladybugdb-learning

Notebooks for learning [LadybugDB](https://ladybugdb.com), an embedded graph database.

## Start the notebook (marimo)

Create or open a notebook in the project environment:

```bash
uv run marimo edit notebooks/intro.py
```

This opens the marimo editor in your browser. If the file doesn't exist,
marimo creates it. Run `uv run marimo edit` with no filename to get the
file picker instead.

Run a notebook as a read-only app:

```bash
uv run marimo run notebooks/intro.py
```

Run a notebook as a plain script:

```bash
uv run notebooks/intro.py
```

## Managing dependencies

```bash
uv add <package>      # add a dependency (updates pyproject.toml and uv.lock)
uv remove <package>   # remove one
uv sync               # re-sync .venv with uv.lock
```

## Updating the CLI

```bash
yay -Syu              # or: yay -Sua  (AUR packages only)
```

Read the `PKGBUILD` diff yay offers before accepting an update.
