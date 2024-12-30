# Good Programming Practices

## Testing and Debugging

### Programming Challenges
Principles to avoid bugs:
1. **Defensive Programming**
    - Write **specifications** for functions
    - **Modularize** programs - don't write one long huge function, break it up to small pieces.
    - Check **conditions** on inputs/outputs (assertions)

2. **Testing/Validation** and **Debugging**

    **Testing/Validation** - *to detect bugs*
    - **Compare** input/output pairs to specification
    - Discover the scenario **when it's not working**.
    - Another question is **"how can I break my program?"**. Think about when the program may behave unexpectedly.
    
    **Debugging** - *what to do once there is a bug*
    - **Study events** leading up to an error
    - Find out the reasons **why is it not working?**
    - Think about **how to fix the program?**
    - Backup codes before changing it!

### General guidelines to set up for easy testing and debugging.
1. From the **start**, design code to ease the testing and debugging. 
    - E.g., breaking the program up into simple **modules**, self-contained modules that can be easily tested and debugged individually.
2. **Document constraints** on modules. 
    - E.g., what are expected inputs/outputs?
    - This can indicate what to look at in terms of test cases.
3. **Document assumptions** behind code design. 
    - "What was your *thinking process* when you created this code?"
    - "What were the *assumptions* that you were making that let this code be built in this particular way?"
    - This guides the creation of particular test cases to validate your assumptions.

### When are you ready to test?
- ensure **code runs**
    - This helps remove all syntax errors
    - and remove most static semantic errors
    - Interpreter can usually detect these errors
- Once the code runs, we should have a **set of expected results**
    - a set of inputs
    - the expected output for each input

### Classes of Tests
1. **Unit testing**
    - validate each piece of program
    - **testing each function/module** separately to ensure it's working properly
2. **Regression testing**, i.e., go back and retest
    - add test for bugs as you find them in a function
    - **catch reintroduced** errors that were previously fixed
3. **Integration testing**
    - Test the **entire overall program**.
    - Be careful don't rush to do the integration testing without the previous 2 tests!

### Testing approaches
- **intuition** about natural boundaries to the problem
- In addition to intuition or in case of no intuition, do **random testing**. 
    - Accuracy increases with more tests.
    - Not an efficient approach.
- **black box testing**: explore paths through specification
- **glass box testing**: explore paths through code

### Black Box Testing
- tests the **functionality** of an application.
- designed **without looking** at the code
- can be done by someone other than the implementer to avoid **biases**
- can be **reused** if implementation changes

Design black box testing by considering:
- **paths** through specification, i.e., What are test cases for all different ways to go through the specification? 
- possible **boundary conditions**, i.e., what are boundary cases for inputs and/or expected outputs?

### Glass Box Testing
- tests the **internal structures and workings** of a piece of code.
- **use code** directly to guide design of test cases
- Ideally, a **path-complete** glass box test suite tests every potential path through the code at least once.
- **drawbacks**
    - we can't always guarantee path-complete. E.g., a recursive function with arbitrary arguments.
    - we may miss some paths
- We must be willing to settle for testing **most but not all** of the paths
- guidelines
    - branches: exercise all parts of a conditional
    - for loops: loop not entered, body of loop executed once, body of loop executed more than once
    - while loops: same as for loops, cases that catch all ways to exit loop

### Bugs
- Once we know that our code does not run properly, we should:
    - isolate the bug(s)
    - eradicate the bug(s)
    - retest until code runs correctly
- Possible attributes of bugs:
    - **Overt** vs **Covert**:
        - **Overt** has an obvious manifestation - code crashses or runs forever
        - **Covert** has no obvious manifestation - code returns a value, which may be incorrect but hard to determine.
    - **Persistent** vs **Intermittent**:
        - **Persistent** occurs every time code is run
        - **Intermittent** only occurs some times, even if run on same inputs (e.g., when dealing with webs or when time is an important factor)
- Dealing with different categories of bugs
    - Overt and persistent
        - Obvious to detect
        - Good programmers use **defensive programming** to try to force any potential bugs to fall into this category.
    - Overt and intermittent
        - More frustrating and can be harder to debug
        - However, if conditions that prompt bug can be reproduced, then it can be handled.
    - Covert
        - Highly dangerous, as users may not realize answers are incorrect until code has been run for long period.

### Debugging
- Be patient as debugging has a steep learning curve! It often takes a lot of experience to become skilled at debugging.
- A very practiced programmer knows the kinds of things to look for and the kinds of tools to use.
- Tools:
    - **built in** to IDEs
    - `print` statement
    - use your brain, be **systematic** in your hunt
- `print` statement
    - good way to **test hypothesis**
    - print when and what?
        - enter a function
        - parameters
        - function results
    - **bisection method**
        - print halfway through the code
        - find the location where the bug may present depending on values
- error messages are easy to deal with, e.g., `IndexError`, `TypeError`, etc.
- logic errors are hard:
    - **think** before writing codes
    - **draw** pictures, take a break
    - **explain** the code to a rubber duck!

### Debugging steps
- **Study** the program code
    - Don't ask what's wrong, instead ask how did I get the unexpected result?
    - Is it part of a family of problems?
- **scientific method**: debugging is a search problem looking for explanation for incorrect behavior.
    - study available data: both correct test cases and incorrect ones
    - form hypothesis, based on the data
    - repeatable experiments to validate the hypothesis
    - keep record of experiments performed: use narrow range of hypotheses
- Bisection search is very useful searching algorithm for this.

### Pragmatic hints for debugging
- look for usual suspects, e.g., aliasing problems
- ask why the code is doing what it is, not why it is not doing what you want.
- the bug is probably not where you think it is - eliminate locations
- explain the problem to a rubber duck!
- don't always believe the documentation
- take a break and come back to the bug later

## Exceptions and Assertions


