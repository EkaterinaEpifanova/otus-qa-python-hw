# Python Learning Project

This repository contains a collection of simple Python scripts created as part of a learning journey in Python programming.

## 📚 Contents

- `fix_me.py` – Function to calculate the average of a list of numbers
- src/
Each class represents a geometric figure and supports:

  - `get_area()` → implemented as a `@property` named `area`
  - `get_perimeter()` → implemented as a `@property` named `perimeter`
  - `add_area(figure)` → returns the sum of the areas of two figures
- test/
This test suite verifies the correctness of object-oriented geometric classes:
- `Triangle`
- `Rectangle`
- `Square`
- `Circle`
Implemented tests validate area and perimeter calculations, as well as proper behavior of the `add_area()` method.

- test-data/ 
  - Reads a list of books from a CSV file 
  - Reads a list of users from a JSON file
  - Distributes the books as evenly as possible among the users 
  - Saves the result to result.json in proper JSON format
- More scripts coming soon as learning progresses...

## 🛠 Skills Covered

- Pylint linter
- flake8 linter

## ✅ Requirements

- Python 3.7 or higher

To check your version:
```bash
python --version