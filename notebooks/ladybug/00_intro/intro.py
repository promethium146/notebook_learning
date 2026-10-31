import marimo

__generated_with = "0.25.2"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    This exploration is taken from https://docs.ladybugdb.com/get-started/
    """)
    return


@app.cell
def _(mo):
    import ladybug as lb
    from pathlib import Path

    NOTEBOOK_DIR = mo.notebook_dir() or Path(__file__).resolve().parent
    DATA_DIR = NOTEBOOK_DIR / "data"
    DB_PATH = NOTEBOOK_DIR / "intro.lbdb"

    db = lb.Database(str(DB_PATH))
    conn = lb.Connection(db)

    conn.execute("CREATE NODE TABLE IF NOT EXISTS User(name STRING PRIMARY KEY, age INT64)")
    conn.execute("CREATE NODE TABLE IF NOT EXISTS City(name STRING PRIMARY KEY, population INT64)")
    conn.execute("CREATE REL TABLE IF NOT EXISTS Follows(FROM User TO User, since INT64)")
    conn.execute("CREATE REL TABLE IF NOT EXISTS LivesIn(FROM User TO City)")

    user_count = conn.execute("MATCH (u:User) RETURN count(*)").get_next()[0]
    if user_count == 0:
        for table, csv in [("User", "user.csv"), ("City", "city.csv"),
                           ("Follows", "follows.csv"), ("LivesIn", "lives-in.csv")]:
            conn.execute(f'COPY {table} FROM "{DATA_DIR / csv}"')
    return (conn,)


@app.cell
def _(conn):
    response = conn.execute(
        "MATCH (a:User)-[f:Follows]->(b:User) RETURN a.name, b.name, f.since"
    )
    rows = list(response.rows_as_dict())
    rows
    return


@app.cell
def _(conn):
    # query to find all people that can be reached starting from adam, with a maximum number of hops being 5

    def _():
        response = conn.execute(
            """
            MATCH p = (a:User)-[:Follows*1..5]->(b:User)
            WHERE a.name = 'Adam'
            RETURN properties(nodes(p), 'name') AS chain, length(p) AS hops
            ORDER BY hops;
            """
        )
        rows = list(response.rows_as_dict())
        return rows


    _()
    return


@app.cell
def _(conn):
    # Distance from Adam ordered by number of hops from least hops to most

    def _():
        response = conn.execute(
            """
            MATCH (a:User)-[r:Follows*1..5]->(b:User)
            WHERE a.name = 'Adam'
            RETURN b.name, length(r) AS hops
            ORDER BY hops;
            """
        )
        rows = list(response.rows_as_dict())
        return rows

    _()
    return


@app.cell
def _(conn):
    # FINDING ALL PATHS BETWEEN TWO PEOPLE ORDERED BY PATH LENGTH

    def find_paths(source, target, max_hops=5):
        query = f"""
            MATCH p = (a:User)-[:Follows* ACYCLIC 1..{int(max_hops)}]->(b:User)
            WHERE a.name = $source AND b.name = $target
            RETURN properties(nodes(p), 'name') AS chain, length(p) AS hops
            ORDER BY hops
        """
        result = conn.execute(query, parameters={"source": source, "target": target})
        return list(result.rows_as_dict())

    find_paths("Adam", "Noura")
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
