# Object Oriented Programming

## Classes and Inheritance

### Objects
- Every **object** has 3 pieces:
    - a **type**, e.g., int, str, list, dict, etc.
    - an internal **data representation** 
        - It is a way of gluing together the pieces that compose the object. 
        - It can be from very simple as a scalar for a number to a more complex structure such as a linked list for a list.
    - a set of procedures for **interaction** with the object

### Object-Oriented Programming
- Everything in Python is an **object** and has a **type**
- An object is a **data abstraction** that capture:
    - an internal **representation** (**structure**) of the data attributes
    - an **interface** for interacting with object through methods, defines **behaviors** that an object may have but hides implementation
- We can **create new instances** of objects or **destroy objects** explicitly using `del` or just "forget" and leave the "garbage collection" for Python system

### Class
- A **class** is a blueprint/template for creating objects.
    - It is not an object itself.
    - It defines the structure and behavior that objects created from the class will have.
    - An object is an **instance** of a class

- Let's consider an example `x = 1`, `y = 2`, `a = 0.1` and `b = 0.2`:
    - `x`, `y`, `a`, and `b` are all objects
    - `x` and `y` are instances (objects) of class `int`
    - `a` and `b` are instances (objects) of class `float`

### Advantages of OOP?
- **bundle data into packages** together with procedures that work on them through well-defined interfaces
- **divide-and-conquer** development
    - implement and test behavior of each class separately
    - increases modularity and reduces complexity
- easy to **reuse** code

### Creating and using your own classes
- **Creating** a class involves:
    - defining the class name
    - defining the class attributes
- **Using** the class involves
    - creating new instances 
    - performing operations on the instances
- Attributes refer to data and procedures that **belong** to the class
- **Data** attributes are other objects that make up the class
- **Methods** are procedural attributes which are like functions that only work with this class.

### Data attributes and class instances
- When creating a class, we will first have to define **how to create an instance** of that class
- In Python, we use a **special method called __init__** to initialize some data attributes. 
- An object's attributes are variables that can be used throughout the entire object, regardless of the method in which it is first defined. Hence, it is not true that all attributes must be defined in the `__init__` method.
- However. as the `__init__` method is called whenever an object is created, it is considered a good practice to create attributes in the `__init__` method to ensure all attributes are properly initialized.
- An object's attributes are bound to the scope of that object only.

### Methods
- A method is a procedural attribute, like a **function that works only with this class**. It's designed for that class.
- Python always passes the actual object as the first argument, convention is to use `self` as the name of the first argument of all methods.
- The `.` operator is used to asscess any attribute, both data attributes and methods.
- Other than `self` and `.`, methods behave just like functions: take params, do operations, return something.
- Using methods
    - Methods can be called either from an instance or from the class itself. 
    - Note that when calling a method from an instance, we don't need to pass the first argument `self` but when calling it from the class, we need to pass all arguments.
- The `__str__` method
    - An object has **uninformative** print representation by default.
    - Hence, for our class, we may want to define a `__str__` method to provide more useful representation when we use `print` on our class object.
    - The `__str__` method must return a string.
- Other special operators
    - `__add__(self, other)` --> `self + other`
    - `__sub__(self, other)` --> `self - other`
    - `__eq__(self, other)` --> `self == other`
    - `__lt__(self, other)` --> `self < other`
    - `__len__(self)` --> `len(self)`
    - ...
- Key note is that we can have our method return simple values and can also have it return new instances of classes we created!

### Aliasing
- If `a` refers to an object and we assign `b = a`, then both variables refer to the same object.
- For mutable objects like lists, any changes made to one alias will mutate the object itself and hence, affect all other aliases.
- Aliasing is typically error-prone so in general, it is safer to avoid aliasing.
- Aliasing is not as much of a problem for immutable objects like strings.

### Getters and Setters
- Typically, we will define some get methods and some set methods to access and adjust the data attributes of a class.
- It is considered a good practice to always use get() and set() rather than directly interacting with the data attributes of a class via the dot notation.
- This is due to the practice of **hiding information** as we or more generally, the author of class definition, may later **change data attribute variable names** but it is less likely that the name of the get and set methods will be changed.
- More generally, use getters and setters instead of the direct dot notation for:
    - good style
    - easy code maintenance
    - reduction of bugs
- For Python, it is actually more Pythonic to just directly access the data attributes as Python is not great at information hiding, and not enforce the use of getters and setters. Python allows for accessing, writing or even creating data attributes for an instance from outside of class definition. It's **not a good style** to do any of those!

### Hierarchies
- **parent class** (superclass)
- **child class** (subclass)
    - **inherits** all data and behaviors of parent class
    - **add** more **data**
    - **add** more **behavior**
    - **override** behavior

