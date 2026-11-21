#!/usr/bin/env python3
"""Builds corpusorum.sqlite from data/corpusorum.csv and data/works.csv.gz (standard library only).

  python3 tools/build_sqlite.py [output.sqlite]

Tables: corpora (one row per corpus, same columns as the CSV) and works (joins on corpus_id). Multi-valued fields keep the
`; ` separator of the CSV.
"""
import csv
import gzip
import sqlite3
import sys
from pathlib import Path

root = Path(__file__).resolve().parent.parent
out = Path(sys.argv[1]) if len(sys.argv) > 1 else root / "corpusorum.sqlite"
csv.field_size_limit(10**9)
INT = {"year_from", "year_to", "n_works", "n_authors", "extent_year_from", "extent_year_to", "work_id", "date_from", "date_to", "words"}


def load(f, table, key=None):
    rd = csv.reader(f)
    cols = next(rd)
    db.execute(f"CREATE TABLE {table} ({', '.join(c + (' INTEGER' if c in INT else ' TEXT') + (' PRIMARY KEY' if c == key else '') for c in cols)})")
    db.executemany(f"INSERT INTO {table} VALUES ({','.join('?' * len(cols))})",
                   ([(int(float(v)) if c in INT and v else (None if v == "" else v)) for c, v in zip(cols, row)] for row in rd))


out.unlink(missing_ok=True)
db = sqlite3.connect(out)
with open(root / "data" / "corpusorum.csv", encoding="utf-8", newline="") as f:
    load(f, "corpora", "id")
with gzip.open(root / "data" / "works.csv.gz", "rt", encoding="utf-8", newline="") as f:
    load(f, "works")
db.execute("CREATE INDEX works_corpus ON works(corpus_id)")
db.execute("CREATE INDEX works_author ON works(author)")
db.commit()
print(out, db.execute("SELECT count(*) FROM corpora").fetchone()[0], "corpora,", db.execute("SELECT count(*) FROM works").fetchone()[0], "works")
