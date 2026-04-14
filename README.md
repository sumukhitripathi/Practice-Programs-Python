# Python Lab Programs

This repository contains beginner-friendly Python lab exercises. Each file is a small standalone program focused on a core programming concept such as input/output, conditionals, loops, functions, recursion, lists, tuples, exception handling, file storage, classes, data visualization, and basic web scraping.

## Repository Structure

### Basics and conditionals

- `1Basic_input_output.py` - reads user input and prints the output
- `2if_else.py` - checks voting eligibility using an `if-else` condition
- `check_even_odd.py` - returns whether a number is even or odd
- `check_positive_negative_zero.py` - identifies whether a number is positive, negative, or zero
- `print_largest_num.py` - prints the largest among three numbers
- `prime_num.py` - checks whether a number is prime

### Functions, loops, and recursion

- `3factorial.py` - calculates factorial using an iterative approach
- `4Func_calculate_area.py` - calculates the area of a circle using a function
- `factorial_using_function.py` - calculates factorial using a function
- `fibonacci_series.py` - generates a Fibonacci series
- `power_using_recusrion.py` - computes power using recursion
- `running_sum.py` - keeps adding numbers until a stopping condition is reached
- `concatenate_strings.py` - joins strings into a single result

### Lists, strings, and tuples

- `5sort_list.py` - sorts a list manually using nested loops
- `6reverse_string.py` - reverses a string
- `list_input.py` - accepts list input and processes the values
- `max_in_list.py` - finds the maximum value in a list
- `pos_neg_list.py` - separates positive and negative values from a list
- `frequency_of_num.py` - counts how many times a number appears in a list
- `in_operator.py` - checks whether a value exists in a list
- `tuple_operations.py` - performs simple tuple-based string processing
- `tuple_search.py` - searches for a value inside a tuple

### Files, storage, and classes

- `7exception_handling.py` - demonstrates `try`, `except`, `else`, and `finally`
- `8file_handling.py` - reads text data and writes it into another file format
- `9binary_file_operations.py` - stores and reads binary data using `pickle`
- `9class_usage.py` - demonstrates class creation and object usage with a `Car` example
- `shelve_file_operations.py` - stores and updates key-value data using Python `shelve`

### Visualization and web scraping

- `10data_visualisation.py` - reads values from `data.txt` and plots them with `matplotlib`
- `11web_scraping.py` - extracts paragraph text from a sample website and stores it in SQLite

## Requirements

- Python 3.x
- Optional libraries for selected programs:
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
- Most scripts are simple practice programs and can be run separately.
- Some scripts require keyboard input.