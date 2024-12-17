# Week 1: Python Basics

## Introduction to Python

### Introduction
- Computational thinking means that everything can be viewed as a math problem involving numbers and formulas.
- Computer Science is the study of how to utilize computers to solve problems.
- 2 things every computer can do are basically performing calculations and remembering the results.

### Knowledge
- Declarative knowledge is **statements of fact**.
- Imperative knowledge is a **recipe** or "how-to" information.

### Machines
- Fixed program computer is designed to do exactly one computation.
- Stored program computer is designed to run any computation, by interpreting instructions that are read into it.
- Basic machine architecture includes a memory, inputs, outputs and a heart containing arithmetic logic unit and control unit
    - ALU performs primitive ops, e.g., add, subtract, ...
    - In control unit, there is a **program counter** which points the computer to the next instruction to execute in the program.
- 6 primitives to compute anything (Turing): move left, move right, scan, print, erase, do nothing.
- Anything that this computable in one programming language is computable in any other programming language.
- In some languages, it can be easier to do something than others but nonetheless, they're all the same.

### Languages
- Primitive constructs: numbers, strings, simple operators (addition, subtraction, ...).
- Syntax: How to legally put primitive constructs together.
- Static semantics is which syntactically valid strings actually have a meaning.
- Semantics is the meaning associated with a syntactically correct expression without static semantic errors.
- Where things can go wrong:
    - Syntactic errors are common and easily caught by most modern programming languages.
    - Static semantic errors can cause unpredictable behaviors. Some programming languages check for these before running.
    - No semantic errors but leads to different meaning from intention.

### Types
- A program is a sequence of definitions (which can be evaluated) and commands (which can be executed).
- Programs manipulate data objects which have a type that is important as it defines the kinds of things programs can do to them.
- Objects are:
    - scalar: cannot be subdivided
    - non-scalar: have internal structure that can be accessed
- Scalar objects in Python: int, float, bool, NoneType (has one value: None)
- Casting: convert object of one type to another (change types).
- Objects and operators are combined to form expressions.

### Variables
- Values are assigned to variables.
- Reasons for giving names to values of expressions:
    - **reuse names** instead of values
    - easier to change code later

### Operators and Branching
- Arithmetic comparisons and logic operators.
- The simplest branching statement is a conditional.
- Branching programs allow us to make choices and do different things.
- At most, each statement gets executed once so these programs run in **constant time** (*linear programs*).

## Core elements of programs

### Bindings
- Bind the value in the right hand side to the variable (name) in the left hand side.
- **Be careful about the order in which things are done**.

### String
- A string is a sequence of characters, enclosed in quotation marks or single quotes.
- String is a non-scalar object! (In C, among primitives, there is only char which is a scalar object!).
- Operations on strings:
    - Concatenate strings: e.g., "+" in Python.
    - Getting the length of the string
    - Indexing (In Python, index starts from 0 from the left and -1 from the right!)
    - Slicing:
        - `s[i:j]` gives a portion of s from `i` to `j-1`
        - `s[i:j:k]` gives a portion of s from `i` to `j-1` with step `k`, negative `k` means step backwards.

### Input/Output




