import marimo

__generated_with = "0.25.2"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    This exploration is taken from https://docs.ladybugdb.com/get-started/
    """)
    return


app._unparsable_cell(
    """
        import marimo as mo
    import ladybug as lb
    from pathlib import Path

    NOTEBOOK_DIR = mo.notebook_dir() or Path.cwd()
    DATA_DIR = NOTEBOOK_DIR / \"data\"
    DB_PATH = NOTEBOOK_DIR / \"intro.lbdb\"   # DB file lives next to intro.py

    def main():
        db = lb.Database(str(DB_PATH))
        conn = lb.Connection(db)

        conn.execute(\"CREATE NODE TABLE IF NOT EXISTS User(name STRING PRIMARY KEY, age INT64)\")
        conn.execute(\"CREATE NODE TABLE IF NOT EXISTS City(name STRING PRIMARY KEY, population INT64)\")
        conn.execute(\"CREATE REL TABLE IF NOT EXISTS Follows(FROM User TO User, since INT64)\")
        conn.execute(\"CREATE REL TABLE IF NOT EXISTS LivesIn(FROM User TO City)\")

        conn.execute(f'COPY User FROM \"{DATA_DIR / \"user.csv\"}\"')
        conn.execute(f'COPY City FROM \"{DATA_DIR / \"city.csv\"}\"')
        conn.execute(f'COPY Follows FROM \"{DATA_DIR / \"follows.csv\"}\"')
        conn.execute(f'COPY LivesIn FROM \"{DATA_DIR / \"lives-in.csv\"}\"')

        # Execute Cypher query
        response = conn.execute(
            \"\"\"
            MATCH (a:User)-[f:Follows]->(b:User)
            RETURN a.name, b.name, f.since;
            \"\"\"
        )
        for row in response:
            print(row)

    if __name__ == \"__main__\":
        main()
    """,
    name="_"
)


@app.cell
def _():
    ## TO DELETE THE DB

    # for suffix in ("", ".wal", ".shadow", ".tmp"):
    #     Path(str(DB_PATH) + suffix).unlink(missing_ok=True)
    return


@app.cell
def _(DB_PATH, lb):
    db = lb.Database(str(DB_PATH))
    conn = lb.Connection(db)
    response = conn.execute(
        """
        MATCH (a:User)-[f:Follows]->(b:User)
        RETURN a.name, b.name
        """
    )
    return (response,)


@app.cell
def _(response):
    for row in response.rows_as_dict():
        print(row)
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
