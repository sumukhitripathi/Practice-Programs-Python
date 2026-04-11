# Python Lab Programs

This repository contains beginner-friendly Python lab exercises. Each script is a small standalone example focused on one core programming concept such as input/output, conditionals, functions, recursion, lists, tuples, exception handling, file operations, classes, data visualization, and introductory web scraping.

## Repository Structure

### Basics and conditionals

- `1Basic_input_output.py` - reads basic user input and prints the result
- `2if_else.py` - checks voting eligibility using conditional statements
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

### Lists and strings

- `5sort_list.py` - sorts a list manually using nested loops
- `6reverse_string.py` - reverses a string without built-in slicing shortcuts
- `list_input.py` - accepts list input and processes the values
- `max_in_list.py` - finds the maximum value in a list
- `pos_neg_list.py` - separates positive and negative values from a list
- `frequency_of_num.py` - counts how many times a number appears in a list
- `in_operator.py` - checks whether a value exists in a list

### Tuples

- `tuple_operations.py` - splits email addresses into usernames and domains
- `tuple_search.py` - searches for a value inside a tuple

### Exceptions, files, and classes

- `7exception_handling.py` - demonstrates `try`, `except`, `else`, and `finally`
- `8file_handling.py` - reads text data and writes it into a CSV file
- `9binary_file_operations.py` - stores and reads binary data using `pickle`
- `9class_usage.py` - demonstrates class creation and object usage with a `Car` example

### Visualization and web scraping

- `10data_visualisation.py` - reads values from `data.txt` and plots them with `matplotlib`
- `11web_scraping.py` - scrapes paragraph data from a sample e-commerce test site and stores it in SQLite

## Requirements

- Python 3.x
- Additional libraries for some scripts:
  - `matplotlib` for `10data_visualisation.py`
  - `requests` and `beautifulsoup4` for `11web_scraping.py`

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
- Most scripts are interactive and require keyboard input.
- Some scripts create output files such as CSV, binary, or database files when executed.