# Project: Python - if/else, loops, functions

**Author:** Guillaume

**Weight:** 1

**Project Start:** Oct 31, 2023, 4:00 AM

**Project End:** Nov 1, 2023, 4:00 AM

**Checker Release:** Oct 31, 2023, 10:00 AM

**Auto Review Deadline:** Project deadline

## Resources

**Read or watch:**
- [More Control Flow Tools](URL) (Read until "4.6. Defining Functions" included)
- [IndentationError](URL)
- [How To Use String Formatters in Python 3](URL)
- [Learn to Program](URL)
- [Learn to Program 2: Looping](URL)
- [Pycodestyle – Style Guide for Python Code](URL)

**Man or Help:**
- `python3`

## Learning Objectives

By the end of this project, you should be able to explain:

### General
- Why Python programming is awesome
- Why indentation is so important in Python
- How to use the if and if-else statements
- How to use comments
- How to assign values to variables
- How to use the while and for loops
- How Python's 'for' differs from 'C's 'for'
- How to use the break and continue statements
- How to use else clauses on loops
- What the 'pass' statement does and when to use it
- How to use the `range` function
- What is a function and how to use functions
- What a function returns if it doesn't use a 'return' statement
- Scope of variables
- What's a traceback
- What the arithmetic operators are and how to use them

### Copyright and Plagiarism
- You are not allowed to publish any content of this project.
- Any form of plagiarism is strictly forbidden and will result in removal from the program.

## Requirements

### Python Scripts
- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/python3`
- A `README.md` file at the root of the project folder is mandatory
- Your code should use `pycodestyle` (version 2.8.*)
- All your files must be executable
- The length of your files will be tested using `wc`

### C Scripts
- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be compiled on Ubuntu 20.04 LTS using `gcc`, using the options `-Wall -Werror -Wextra -pedantic -std=gnu89`
- All your files should end with a new line
- Your code should use the Betty style. It will be checked using `betty-style.pl` and `betty-doc.pl`
- You are not allowed to use global variables
- No more than 5 functions per file
- The prototypes of all your functions should be included in your header file called `lists.h`
- Don’t forget to push your header file
- All your header files should be include guarded

## Quiz Questions

You've completed the quiz successfully! Keep going!

## Tasks

### 0. Positive anything is better than negative nothing

This program will assign a random signed number to the variable `number` each time it is executed. Complete the source code to print whether the number stored in the variable `number` is positive or negative.

You can find the source code [here](URL).

The variable `number` will store a different value every time you run this program.

The output of the program should be:

```bash
The number, followed by
if the number is greater than 0: is positive
if the number is 0: is zero
if the number is less than 0: is negative
followed by a new line

$ ./0-positive_or_negative.py
-4 is negative
$ ./0-positive_or_negative.py
0 is zero
$ ./0-positive_or_negative.py
-3 is negative
$ ./0-positive_or_negative.py
-10 is negative
$ ./0-positive_or_negative.py
10 is positive
$ ./0-positive_or_negative.py
-5 is negative
$ ./0-positive_or_negative.py
6 is positive
$ ./0-positive_or_negative.py
7 is positive
$ ./0-positive_or_negative.py
5 is positive

