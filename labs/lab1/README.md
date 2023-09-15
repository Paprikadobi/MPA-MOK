# Laboratory 1 - Introduction to Python

"Python is a clear and powerful object-oriented programming language, comparable to Perl, Ruby, Scheme, or Java.

Some of Python's notable features:

* Uses an elegant syntax, making the programs you write easier to read.
* Is an easy-to-use language that makes it simple to get your program working. This makes Python ideal for prototype development and other ad-hoc programming tasks, without compromising maintainability.
* Comes with a large standard library that supports many common programming tasks such as connecting to web servers, searching text with regular expressions, reading and modifying files.
* Python's interactive mode makes it easy to test short snippets of code. There's also a bundled development environment called IDLE.
* Is easily extended by adding new modules implemented in a compiled language such as C or C++.
* Can also be embedded into an application to provide a programmable interface.
* Runs anywhere, including Mac OS X, Windows, Linux, and Unix, with unofficial builds also available for Android and iOS.
* Is free software in two senses. It doesn't cost anything to download or use Python, or to include it in your application. Python can also be freely modified and re-distributed because while the language is copyrighted it's available under an open-source license [[ref](https://wiki.python.org/moin/BeginnersGuide/Overview)]."

"**Python** is a general-purpose, versatile, and powerful programming language. It’s a great first language because it’s concise and easy to read. Whatever you want to do, Python can do it. From web development to machine learning to data science, Python is the language for you":

* Great first language,
* Large programming community,
* Excellent online documentation,
* Endless libraries and packages,
* World-wide popularity,
* Powerful and flexible [[ref](https://www.codecademy.com/catalog/language/python)].

**We will use Python 3.** Some legacy applications still use Python 2, but we won't be our concern.

## Install python [[ref](https://wiki.python.org/moin/BeginnersGuide/Download)]

Python binaries and tarballs can be downloaded from [here](https://www.python.org/downloads/).

* **For Windows**: Latest stable version can be downloaded through [Python Releases for Windows](https://www.python.org/downloads/windows/) page. You will probably want the latest stable 64-bit version.
* **For MAC** click [here](https://www.python.org/downloads/macos/)
* **For Linux**: 
  * Most Python distributions come with Python pre-installed, as many system packages depend on it. You can check that by running `which python3` or `python3 --version`.
  * Install from a package manager:
    - For Red Hat, CentOS or Fedora: `sudo dnf install python3 python3-devel`,
    - For Debian or Ubuntu: `sudo apt install python3 python3-dev`.
  * Build from source code: check the [[ref](https://realpython.com/installing-python/#how-to-install-python-on-linux)].    

## How to run Python

* Useful commands

  ```console
  $ which python
  $ python -v
  ```

* Set interpreter in file header
  ```python
  #!/usr/bin/python3
  ```

* Run in interactive mode: `python3`

### Command Line

```console
$ python3
Python 3.8.2 (default, Jun  8 2021, 11:59:35) 
[Clang 12.0.5 (clang-1205.0.22.11)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> string = "Hello World!"
>>> print(string)
Hello World!
>>> locals()
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, 'string': 'Hello World!'}
>>> a = 5
>>> b = 3
>>> c = a + (2 * b)
>>> print(str(c))
11
>>> locals()
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, 'string': 'Hello World!', 'a': 5, 'b': 3, 'c': 11}
>>> exit()
$
```

### Write and run Python script (.py)

```console
$ cat hello_world.py
#!/usr/bin/python3

__author__ = "Peter Cíbik"
__email__ = "xcibik00@vutbr.cz"
__copyright__ = "Copyright 2021, MPA-MOK"
__credits__ = ["Peter Cíbik" , "Sara Ricci"]

def main():
    print("Hello World!")

if __name__ == "__main__":
    main()

$ chmod +x hello_world.py
$ ./hello_world.py  
Hello World!
```

Running Python file directly works fine for small projects, but starts to break down as the number of the files grows. While it won't be adressed here, you can check out [setuptools documenentation](https://setuptools.pypa.io/en/latest/userguide/index.html).

## EX1 - start with Python

**Indentation** - Some other languages use braces to show where blocks of code begin and end. In Python we use indentation of four spaces to enclose blocks of code.

### Arithmetic operators

- `+` Addition
- `-` Subtraction
- `*` Multiplication
- `/` Division
- `%` Mod (the remainder after dividing)
- `**` Exponentiation
- `//` Divides and rounds down to the nearest integer

**EX1:**
My electricity bills for the last four months have been 29€, 32€, 17€ and 84€. What is the average monthly electricity bill over the four month period? Display the number using the `print` function.

### Variables and Assignment Operators

- Only use ordinary letters, numbers and underscores in your variable names. They can’t have spaces, and need to start with a letter or and underscore.
- You can’t use Python's reserved words, or "keywords" as variable names - [keywords](https://docs.python.org/3/reference/lexical_analysis.html#keywords).
- The pythonic way to name variables is to use all lowercase letters and underscores to separate words.

```python
a = 3                                   # integer
b = 4.2                                 # float
c = int(5.4)                            # integer of value 5
d = float(5)                            # float of value 5.0
e = True                                # bool
f = False                               # bool
my_string = 'this is a string!'         # str
my_string2 = "this is also a string!!!" # str

```

```python
a += 2  # same as a = a + 2
b -= 2  # same as b = b - 2

```

```python
5 < 3   # Less Than
5 > 3   # Greater Than
3 <= 3  # Less Than or Equal To
3 >= 5  # Greater Than or Equal To
3 == 5  # Equal To
3 != 5  # Not Equal To
True is True      # Equal to (between object identities)
True is not None  # Not Equal To (between object identities)

5 < 3 and 5 == 5 # and - Evaluates if all provided statements are True
5 < 3 or 5 == 5  # or - Evaluates if at least one of many statements is True
not 5 < 3        # not - Flips the Bool Value
```

### Functions

```python
def function_name(input_1, input_2):
    pi = 3.14159
    return ((input_1 + input_2) * pi)
```

**Header:**

- The **function header** always starts with the `def` keyword, which indicates that this is a function definition.
- Then comes the function name (`function_name`), which follows the same naming conventions as variables.
- Immediately after the name are parentheses that may include arguments separated by commas (`input_1, input_2`). Arguments, or parameters, are values that are passed in as inputs when the function is called, and are used in the function body. If a function doesn't take arguments, these parentheses are left empty. 
- The header always end with a colon `:`.   

**Body:**

- The **body of a function** is the code indented after the header line. Here, it's the two lines that define `pi and return` the volume.
- Within this body, we can refer to the argument variables and define new variables, which can only be used within these indented lines.
- The body will often include a return statement, which is used to send back an output value from the function to the statement that called the function.
- A return statement consists of the `return` keyword followed by an expression that is evaluated to get the output value for the function. If there is no return statement, the function simply returns `None`.

#### Main function

```python
def main():
    print("Hello World!")

if __name__ == "__main__":
    main()
```

**EX2:**
Create a python file with functions for Addition, Subtraction, Multiplication and Division of two input numbers. Use `a = 12` and `b = 6` as input and print results.

### If Statement

An `if` statement is a conditional statement that runs or skips code based on whether a condition is true or false.

```python
if phone_balance < 5:
    phone_balance += 10
    bank_balance -= 10
```

- An if statement starts with the `if` keyword, followed by the condition to be checked, in this case `phone_balance < 5`, and then a colon. The condition is specified in a boolean expression that evaluates to either True or False.
- After this line is an indented block of code to be executed if that condition is true. Here, the lines that increment `phone_balance` and decrement `bank_balance` only execute if it is true that `phone_balance` is less than 5. If not, the code in this if block is simply skipped.

```python
if season == "spring":
    print("plant the garden!")
elif season == "summer":
    print("water the garden!")
elif season == "fall":
    print("harvest the garden!")
elif season == "winter":
    print("stay indoors!")
else:
    print("unrecognized season")
```

- An `if` statement must always start with an `if` clause, which contains the first condition that is checked. If this evaluates to True, Python runs the code indented in this if block and then skips to the rest of the code after the if statement.

- `elif` is short for "else if." An elif clause is used to check for an additional condition if the conditions in the previous clauses in the if statement evaluate to False. As you can see in the example, you can have multiple elif blocks to handle different situations.

- Last is the `else` clause, which must come at the end of an if statement if used. This clause doesn't require a condition. The code in an else block is run if all conditions above that in the if statement evaluate to False.

**EX3:**
Create a python file with function that compare two input numbers `a` and `b`, test on same values as in EX2 and print the output:
* if `a < b`: `return -1`
* if `a == b`: `return 0`
* if `a > b`: `return 1`

### Loops

Python has two keywords for loops: `for` and `while`. A `for` loop is used to "iterate", or do something repeatedly, over an iterable.
An iterable is an object that can return one of its elements at a time. This can include sequence types, such as strings, lists, and tuples, as well as non-sequence types, such as dictionaries and files.

```python
cities = ['new york city', 'mountain view', 'chicago', 'los angeles']
for city in cities:
    print(city)
```

- The first line of the loop starts with the `for` keyword, which signals that this is a for loop
- Following that is city in cities, indicating `city` is the iteration variable, and `cities` is the iterable being looped over. In the first iteration of the loop, city gets the value of the first element in cities, which is “new york city”.
- The for loop heading line always ends with a colon `:`
- Following the for loop heading is an indented block of code, the body of the loop, to be executed in each iteration of this loop. There is only one line in the body of this loop - `print(city)`.
- After the body of the loop has executed, we don't move on to the next line yet; we go back to the for heading line, where the iteration variable takes the value of the next element of the iterable. In the second iteration of the loop above, city takes the value of the next element in cities, which is "mountain view".
- This process repeats until the loop has iterated through all the elements of the iterable. Then, we move on to the line that follows the body of the loop - in this case, `print("Done!")`. We can tell what the next line after the body of the loop is because it is unindented. Here is another reason why paying attention to your indentation is very important in Python!

**EX4:**
Create a python file with function that print numbers in range using `for` loop. Use `a = 36` as input for range, print the results.

For loops are an example of "definite iteration" meaning that the loop's body is run a predefined number of times. This differs from "indefinite iteration" which is when a loop repeats an unknown number of times and ends when some condition is met, which is what happens in a `while` loop. Here's an example of a while loop.

```python
card_deck = [4, 11, 8, 5, 13, 2, 8, 10]
hand = []

# adds the last element of the card_deck list to the hand list
# until the values in hand add up to 17 or more
while sum(hand) < 17:
    hand.append(card_deck.pop())
```

- The first line starts with the `while` keyword, indicating this is a while loop.
- Following that is a condition to be checked. In this example, that's `sum(hand) <= 17`.
- The while loop heading always ends with a colon `:`.
- Indented after this heading is the body of the while loop. If the condition for the while loop is true, the code lines in the loop's body will be executed.
- We then go back to the while heading line, and the condition is evaluated again. This process of checking the condition and then executing the loop repeats until the condition becomes false.
- When the condition becomes false, we move on to the line following the body of the loop, which will be unindented.

Sometimes we need more control over when a loop should end, or skip an iteration. In these cases, we use the `break` and `continue` keywords, which can be used in both for and while loops.

- `break` terminates a loop
- `continue` skips one iteration of a loop

**EX5:**
Create a python file with function that finds sum of numbers in a list using `while` loop. Use list `a = [13,45,1,-10,273]` as input, print the result.

Check ⓒ Udacity – [Introduction to Python Programming](https://www.udacity.com/course/introduction-to-python--ud1110?autoenroll=true) for more and try it out ...  

## HW1 - prepare environment for Python 3 development

- Install python3 on your computer (*or use Virtualbox VM - [Download](https://drive.google.com/file/d/12cw4xfV7TnfzVBosFBTI46Dq8QwnJcTL/view?usp=sharing))
- Install IDE 
  - Visual Studio Code - [Download](https://code.visualstudio.com)
  - PyCharm - [Download](https://www.jetbrains.com/pycharm/)
- Write and run first program

**Resources**
- [Introductory presentation](https://docs.google.com/presentation/d/1ObqiRNVDBNBDjDc7OuFyEe6gQl5FnbOv3VKXLNWYS-c/edit?usp=sharing)
- Python org [website](https://www.python.org)
  - [Doc](https://www.python.org/doc/)
  - [Download](https://www.python.org/downloads/)
  - [Beginner's Guide](https://wiki.python.org/moin/BeginnersGuide)
- TutorialsPoint - [Python - Basic Syntax](https://www.tutorialspoint.com/python/python_basic_syntax.htm)
- Python [Cheat Sheet](https://blog.finxter.com/python-cheat-sheet/)
- Codecademy – [Python](https://www.codecademy.com/catalog/language/python)