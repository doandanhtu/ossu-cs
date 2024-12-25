# Structured Types

## Tuples and Lists

### Tuples
- A tuple is an **ordered** sequence of elements, i.e, elements are accessible by index.
- can contain elements of **mixed types**.
- are **immutable**.
- conveniently used to **swap** variable values.
- used to **return more than one value** from a function
- are **iterable**.
- represented by parens ()

### Lists
- **ordered sequence** of information, accessible by index.
- contain elements that:
    - are **usually homogeneous**, i.e., of the same type.
    - can be of mixed types.
- are **mutable** (different from strings and tuples)
- are **iterable**
- denoted by square brackets, []

### List operations
- Add: `.append()`
- Concatenate: `+` operator, `.extend()`
- Remove: `del()`, `.pop()`, `.remove()`
- string to list: `list(s)` - convert a string to a list of all characters
- `.split()`: split a string on a character, default of space character.
- `''.join()`: turn a list of chars into a string with the char in '' between every element.
- Others: 
    - `.sort()` and `sorted()`
    - `.reverse()`
    - `.insert()`
- `.pop()` returns the element. 
- Operating methods like `.sort()`, `.remove()`, `.append()`, `.reverse()`, `.insert()`, `.extend()` returns nothing (`None`).

### Mutation, Aliasing, Cloning
- Be careful with **side effects** when working with lists.
- Assign a list to a variable or put a list in any data structure will create an **alias** of the list.
- As a list is a actually just a pointer to an object stored in the memory, any changes to a list will apply to all aliases.
- **Cloning** a list will make a copy of the original list, effectively creates a pointer to another object in the memory.
- Clones will not be affected by changes to the original.
- **Avoid** mutating a list when iterating over it.
- `==` and `is` can be used to compare lists but they work differently:
    - `==` tests whether 2 lists are identical, i.e., whether elements in 2 lists are identical
    - `is` tests whether 2 variables point to the same object in the memory.

### Functions as Objects
- functions are **first class objects**, which means they:
    - have types
    - can be elements of data structures like lists
    - can appear in expressions
        - as part of an assignment statement
        - as an argument to a function
- Particularly useful to **use functions as arguments when coupled with lists** aka **higher order programming**

### Quick review of strings, tuples and lists
- They are all ordered sequence of data
- Common operations of strings, tuples and lists:
    - **index** via square bracket, []
    - get the **length** using len()
    - **concatenate** using `+`
    - **repeat** using `*`
    - **slice** using [start:end:step]
    - Test if an element is in the sequence using `in`
    - Test if an element is not in the sequence using `not in`
    - **iterable**
- Only lists are **mutable**, others are immutable

### Dictionaries
- A Python dictionary stores pairs of data:
    - key: this can be considered a custom index
    - value: this is analogous to an element
- Similarly to indexing into a list,
    - we can look up the key and get the value associated with it
    - if key isn't found, we will get an error
- Dictionary operations:
    - **add** an entry
    - **test** if key in dictionary
    - **delete** an entry
    - get **an iterable collection of keys** via `.keys()` (no guaranteed order)
    - get **an iterable collection of values** via `.values()` (no guaranteed order)
- Dictionary keys and values:
    - Values:
        - any type (immutable / mutable, can be lists, can be other dictionaries, ...)
        - can be **duplicates**
    - Keys:
        - must be **unique**
        - must be of **immutable** type (actually **hashable**)
    - **No order** to keys or values
- Dictionaries offer a lot more capability in terms of what can be stored inside of them.


    
