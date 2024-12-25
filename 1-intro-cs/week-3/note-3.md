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


