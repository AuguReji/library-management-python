# 📚 Library Management System (Python)

A command-line **Library Management System** written in Python. This is a Python port of an original [C++ implementation](https://github.com/AuguReji/library-management-cpp), built to practice translating OOP design, control flow, and file I/O concepts across languages.

The repo contains two versions, showing the progression from an in-memory system to a persistent one — mirroring the structure of the original C++ repo:

| File | Description |
|---|---|
| `library.py` | Base version — in-memory library system, data resets every run (pre-loaded with a starter catalogue). |
| `library_csv.py` | Extended version — adds **CSV-based file persistence** so the catalogue and borrow records survive between runs. |

---

## ✨ Features

Both versions share the same core functionality:

- **Add Book** — add a new title/author/year to the catalogue, or increment the copy count if it already exists.
- **Search Book** — case-insensitive substring search by title.
- **Borrow Book** — search first, then borrow by Book ID; decrements available copy count and updates status (`Available` / `Not Available`).
- **Return Book** — validates the book was actually borrowed (via a `borrow_list`) before restoring it; if it wasn't borrowed, offers to add it as a new entry instead.
- **Catalogue View** — lists every book with ID, title, author, year, status, and copy count.

**`library.py`** starts with a hardcoded catalogue of 5 books every run, and all changes are lost on exit.

**`library_csv.py`** starts empty (or loads whatever is already saved) and adds **persistent storage** — on exit, the full catalogue and current borrow list are written to disk (`books_details.csv`, `borrowList.csv`) and reloaded automatically the next time the program starts.

---

## 🗂️ Data Model

Each book is represented by a `Books` class with plain attributes (Python doesn't need explicit getters/setters):

- `id` — unique integer ID
- `title`, `author` — stored in uppercase for consistent, case-insensitive matching
- `year` — publication year
- `status` — `"Available"` / `"Not Available"`
- `count` — number of copies currently in the library

---

## 💾 Persistence Design (`library_csv.py`)

Two CSV files back the system:

**`books_details.csv`** — one row per book:
```
1,WINGS OF FIRE,Dr.A. P. J. ABDUL KALAM and ARUN TIWARI,1999,Available,1
2,GOD OF SMALL THINGS,ARUNDATHI ROY,1997,Available,1
```

**`borrowList.csv`** — one borrowed Book ID per line, tracking what's currently checked out.

### How it works
- `load_books()` / `load_borrow_list()` run at program start, using Python's built-in `csv` module to parse each row into a `Books` object (rows are only accepted if they split into exactly 6 fields, guarding against malformed data).
- `save_books()` / `save_borrow_list()` run when the user exits, writing the current in-memory state back to the same two files using `csv.writer`.
- If no CSV files exist yet (first run), both loaders catch `FileNotFoundError` and simply start with empty lists.
- Net effect: the library's state is **fully persistent across sessions** — no database required.

---

## 🚀 Getting Started

### Requirements
Python 3.10+ (uses `match`/`case` statements)

### Run the base (in-memory) version
```bash
python3 library.py
```
Starts with 5 pre-loaded books every time; nothing is saved on exit.

### Run the CSV-persistent version
```bash
python3 library_csv.py
```
Starts empty on first run (or loads `books_details.csv` / `borrowList.csv` if they already exist) — add a few books to get going. Everything is saved automatically on exit.

### Menu (same for both versions)
```
Add Book(a)
Search(s)
Borrow(b)
Return(r)
Catalogue(c)
Exit(y)
```

---

## 🧠 What This Project Practices

- Translating OOP design from C++ to Python (constructors, `self` vs. `this`, no access modifiers)
- Idiomatic Python control flow: `match`/`case`, `try`/`except` for input validation instead of stream failure checks
- File I/O with the `csv` module, replacing manual `stringstream` parsing
- List and object manipulation without manual memory management or references
- Debugging language-specific pitfalls (e.g. Python's function-local variable scoping vs. C++ globals, negative list indexing)

---

## 📌 Possible Next Steps

- Seed `books_details.csv` with starter data for a better first-run experience
- Support partial-title matching for return/add, not just exact matches
- Add a `requirements.txt` (not currently needed — no external dependencies) and packaging via `setup.py` or `pyproject.toml`
- Add unit tests for `add_search`, `borrow_book`, and `return_book` logic
