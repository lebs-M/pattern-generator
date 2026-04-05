# Pattern Generator CLI

A Python command-line application that generates text-based geometric patterns. Built as part of my Software Engineering studies to strengthen skills in loops, logic, modular design, and unit testing.

---

## Patterns Available

| # | Pattern | Description |
|---|---------|-------------|
| 1 | Triangle | Right-angled triangle, grows row by row |
| 2 | Increasing Triangle | Centred triangle growing from tip to base |
| 3 | Decreasing Triangle | Centred triangle shrinking from base to tip |
| 4 | Hollow Triangle | Right-angled triangle with hollow interior |
| 5 | Square | Filled square of any size |
| 6 | Grid | Checkerboard pattern |
| 7 | Hollow Grid | Square border with hollow interior |

---

## How to Run

Make sure you have Python 3 installed, then:

```bash
# Clone the repository
git clone https://github.com/lebs-M/pattern-generator.git

# Navigate into the project folder
cd pattern-generator


# Run the program
python main.py
```

---

## Example Output

```
========================================
       PATTERN GENERATOR CLI
========================================
  1. Triangle
  2. Increasing Triangle
  ...
  0. Exit
========================================
Select an option: 5
Enter size (1-20): 4
Enter a symbol to use (default is *):

****
****
****
****
```

---

## Running Tests

```bash
pytest tests/
```

---

## Project Structure

```
pattern-generator/
│
├── pattern_generator/
│   ├── __init__.py       # Package initialisation
│   ├── patterns.py       # All 7 pattern functions
│   ├── cli.py            # Menu logic and user interaction
│   └── utils.py          # Input validation helpers
│
├── tests/
│   └── test_patterns.py  # Unit tests for all patterns
│
├── README.md
├── requirements.txt
└── main.py               # Entry point
```

---

## What I Learned

- Structuring a Python project using packages and modules
- Separating concerns: logic, UI, and utilities in different files
- Writing unit tests with pytest to verify each pattern
- Handling and validating user input cleanly
- Thinking algorithmically to build geometric shapes with loops

---

## Author

**Lebogang Manamela**
Aspiring Junior Developer | Pretoria, Gauteng
https://github.com/lebs-M
www.linkedin.com/in/lebogang-manamela-a30684207
