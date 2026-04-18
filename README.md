# Python Lab Programs

This repository contains beginner-friendly Python lab exercises. Each script is a small standalone program focused on a core concept such as input/output, conditionals, loops, functions, recursion, strings, lists, tuples, exception handling, file storage, object-oriented programming, data visualization, and basic web scraping.

## Programs Included

### Basics and conditionals

- `1Basic_input_output.py` - reads a name and age from the user and prints them
- `2if_else.py` - checks voting eligibility using an `if-else` condition
- `check_even_odd.py` - checks whether a number is even or odd
- `check_positive_negative_zero.py` - identifies whether a number is positive, negative, or zero
- `print_largest_num.py` - prints the largest among three numbers
- `prime_num.py` - checks whether a number is prime

### Functions, loops, and recursion

- `3factorial.py` - calculates factorial using an iterative approach
- `4Func_calculate_area.py` - calculates the area of a circle using a function
- `factorial_using_function.py` - calculates factorial using a function
- `fibonacci_series.py` - generates a Fibonacci series
- `power_using_recusrion.py` - computes a power using recursion
- `running_sum.py` - keeps adding numbers until a stopping condition is reached
- `concatenate_strings.py` - joins multiple strings into a single result

### Lists, strings, and pattern problems

- `5sort_list.py` - sorts a list manually using nested loops
- `6reverse_string.py` - reverses a string
- `list_input.py` - accepts list input from the user
- `max_in_list.py` - finds the maximum value in a list
- `pos_neg_list.py` - separates positive and negative numbers from a list
- `frequency_of_num.py` - counts how many times a number appears in a list
- `in_operator.py` - checks whether a value exists in a list
- `filtering_list.py` - filters elements from a list based on a condition
- `largest_common_prefix.py` - finds the common prefix among strings
- `magic_square.py` - creates and prints a 3 x 3 magic square

### Tuples, exceptions, and classes

- `tuple_operations.py` - performs simple tuple operations
- `tuple_search.py` - searches for a value inside a tuple
- `7exception_handling.py` - demonstrates `try`, `except`, `else`, and `finally`
- `9class_usage.py` - demonstrates class creation and object usage with a `Car` example

### Files, storage, and persistence

- `8file_handling.py` - reads comma-separated text from `input.txt` and writes it to `output.csv`
- `9binary_file_operations.py` - stores and reads binary data using `pickle`
- `shelve_file_operations.py` - stores and updates key-value data using Python `shelve`

### Visualization and web scraping

- `10data_visualisation.py` - reads values from `data.txt` and plots them using `matplotlib`
- `11web_scraping.py` - extracts paragraph text from a sample website and stores it in SQLite

## Requirements

- Python 3.x
- Standard library modules used in some scripts: `csv`, `pickle`, `sqlite3`, and `shelve`
- Optional third-party libraries for selected programs:
  - `matplotlib` for `10data_visualisation.py`
  - `requests` and `beautifulsoup4` for `11web_scraping.py`

Install optional packages with:

```bash
pip install matplotlib requests beautifulsoup4
```

## How To Run

Run any script from the repository folder:

```bash
python 1Basic_input_output.py
```

If your system uses `python3`, run:

```bash
python3 1Basic_input_output.py
```

## Notes

- This repository is a collection of independent lab programs, not a single integrated application.
- Most scripts are intended for practice and can be run separately.
- Some scripts require keyboard input.
- A few scripts depend on local input files or internet access.