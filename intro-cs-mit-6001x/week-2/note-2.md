# Week 2: Simple Programs

## Simple Algorithms

### Quick recaps
- Strings can be indexed and sliced.
- Strings are immutable and iterable.
- Loops have a loop variable and a terminating condition to control flows.

### Approximate solutions
- Instead of getting an exact solution, we can use the idea of guess and check to get an approximate solution.
- We will need to define what is a **good enough** solution.
- Trade-off between the **correction** of the solution and the **performance** of the program.
- The initial point is important for the idea of GnC.

### Bisection search
- Divide and conquer class of algorithms.
- Bisection search is a logarithmic time algorithm.
- Bisection search will work on any problems with **ordering** property.

### Floats and fractions
- Be careful with **floating point errors**
- When comparing 2 floats, x == y should be avoided. Instead: abs(x - y) < epsilon.
- When representing fractions, unless the denominator can be expressed in power of 2, the representation will be only be approximate.
- E.g., 
    - 0.5 and 0.75 can be represented correctly: 0.1 and 0.11 (1 * 1/2, 1 * 1/2 + 1 * 1/4).
    - 0.1 cannot be represented correctly as it cannot be expressed as the sum of (1 / the power of 2).

### Newton-Raphson
- General approximation algorithm to find roots of a polynomial in 1 variable
    - Suppose we have $p(x) = a_nx^n + a_{n-1}x^{n-1} + ... + a_1x + a_0$
    - We want to find r such that p(r) = 0
    - If g is an approximation of r then a better approximation is: $g - p(g)/p'(g)$ where p' is derivative of p
- This is a very efficient root finding algorithm.

## Functions

### Decomposition and Abstraction
- **Decomposition**: break problem into smaller different, self-contained, pieces
    - Dividing code into **modules** can:
        - allow codes to be separated apart and reusable
        - keep codes organized and coherent
    - Decomposition can be achieved through **functions** and/or **classes**
- **Abstraction**: suppress details of method to compute something from use of that computation 
    - Hide a piece of code for a more effective structure when for examle:
        - we don't need or don't want to see details
        - we want to hide tedious coding details
    - Abstraction can be achieved through **function specifications** or **docstrings**.

### Introducing Functions
- Characteristics of a function:
    - **name**
    - **parameters** (0 or more, a parameter can have a default value)
    - **docstring** (optional but recommended: documentation that shows what a function does)
    - **body** (the sequence of commands or expressions that the function executes)

### Calling functions and scope
- scope is mapping of names to objects
- new scope created when enter a function
- If a function has no `return` statement, Python will return the value `None`

### Iteration vs Recursion
- Recursion is a programming technique where a **function calls itself**.
    - It must have **1 or more base cases** that are easy to solve
    - The problem needs to be able to be reduced into **simpler/smaller version** of same problem

### Inductive Reasoning
- Mathematical induction: To prove a statement indexed on integers is true for all values of n:
    - Prove it is true when n is the smallest value (e.g., n = 0 or n = 1)
    - Then prove that if it is true for an arbitrary value of n, it must be true for (n + 1)
- We can apply the concept of mathematical induction to recursive codes:
    - Does our base case do the right thing?
    - Then assume that our code works correctly for the smaller problem, does it work correctly for the whole problem?

### Towers of Hanoi
- It's perfectly fine to have multiple recursive calls inside of a function body.
- Some problems can be very hard to solve iteratively but elegantly easy to solve recursively.