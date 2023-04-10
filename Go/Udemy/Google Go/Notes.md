# 1. Variables, Values & Type
---
- Go is a static language which means that type is important when declaring variables and assigning values to them. 
- One can not have unused variables in code.
    - The compiler complains.
    - use `_` to throw away returns.
- Go uses the dot notation
    - `package.identifier`, the identifier is the name of the variable, constant or func from the package.
- Variadic parameters
    - The `...<some type>` is how we signify a variadic parameter
    - `...interface{}`, means give me as many arguments of any type as you'd like.
- The type `interface{}` is the empty value of type interface.

## Identifiers

Identifiers name program entities such as variables and types.</br>
They are sequences of one or more letters and digits that must begin with a letter.

Some identifiers are pre-declared.
- Types:
    - bool, byte, complex64, complex128, error, float32, float64, int, int8, int16, int32, int64, rune, string, uint, uint8, uint16, uint32, uint64, uintptr
- Constants:
    - true, false, iota
- Zero Value:
    - nil
- Functions:
    - append, cap, close, complex, copy, delete, imag, len, make, new, panic, print, println, real, recover

Some are reserved as keywords and may not be used as identifiers.
- keywords
    - break, case, chan, const, continue, default, defer, else, fallthrough, for, func, go, goto, if, import, interface, map, package, range, return, select, struct, switch, type, var.

## Declaring Variables

In Go a variable is DECLARED to hold values of a certain TYPE, meaning that:

`var x int` -> will only hold values for type INTEGER. </br>
`x := "hello"` -> will only hold values for type STRING

### Short Declaration Operator

The short declaration operator `:=` allows to declare a variable and assign a value to that variable.

`x := 32`, Declares variabble `x` of type `int` and assigns value `32`.

When reassigning the variable the `=` operator is enough since the variable was previously declared.

### Var Keyword

the `var` keyword is used to declare a variable, one can specify the type of the value or assign one immediatly

Declare variable with type int and assign the **zero** value to it.</br>
`var x int` </br>

Declare variable and assign a value to it.</br>
`var x = 32`

The var keyword can be used to declare variables in the global scope (the short declaration operator is limited in this regard)

- The **ZERO VALUE** depends on each type
    - `0` for integers
    - `0.0` for floats
    - `""` for strings
    - `nil` for pointers, functions, interfaces, slices, channels and maps.

### Constant Keyword

The `const` keyword is used to declare constants.

- to declare a constant simply call: 
    - `const a = 3`, the compiler will figure the type and assign it.
    - `const a int = 3`, typed constants are also a possibility though the compiler loses the flexibility to assign the value.
- the const keyword can be used with parenthesis to declare multiple constants at a time

    ```
    const (
        a = 3
        b = "4"
        c = 5.0
    )
    ```
## Types

- To check the type of a variable in go.
    - `fmt.Printf("%T", x)`

In most programming languages all basic data-types are built-in, however, they usually also provide a set of composite data types already built-in. (there are mixed opinions on wether this should be considered primitive.)

### a. Primitive data types

In CS, primitive data type can be one of:
- A `basic type`, which is a data type provided by a programming language as a basic building block.
- A `built-in type`, which is a data type for which the programming language provides a built-in support

Most programming languages, all basic types are built-in, in addition, many languages also provide a set of composite data types.

### b. Composite data types

In CS, a composite data type or compound data type is ANY data type which can be constructed in a program using the programming language's primitive data types and other composite types. </br>
It is sometimes called a structure or aggregate data types (arrays, lists, etc.)

- The act of constructing a composite type is known as COMPOSITION.

### Type Keyword

We can create our own types using the `type` keyword

`type my_var int` - meaning that we have a type `my_var` with the undelying type of `int`.

>NOTE: A variable declared of the underlying type CAN'T hold a value of type my_var. It would need to be CONVERTED to the desired type.

# 2. Types
---

## Bool Type

> A binary variable, having two possible values True and False.

- pre-declared boolean type in Go is `bool`
- Zero Value is `false`
- Comparison Expressions evaluate to a `bool`.

Examples:
- New bool variable: `var x bool` (gets `false` assigned as **zero value**.)
- New bool variable with assigned value `var x bool = true`

## Numeric Type

All numeric types are distinct except for.
- `byte` is an alias for `uint8`
- `rune` is an alias for `int32` (another word for characters which are 32bits in UTF-8)

### Integers

> An Int variable, stores whole numbers.

- Ints precision depends on size and sign, meaning that we can specify the number of bits to store and if they can store only positive or positive and negative numbers
    - `int8`, `int16`, `int32`, `int64`
    - `uint8`, `uint16`, `uint32`, `uint64` (unsigned, i.e only possitive)
- if a number is stored, which is greater than what the variable can hold it will **overflow** it.
- When declaring a variable with `int` or `uint` it will store either 32 or 64 depending on the system, thus making the optimal conversion on the architecture it is being used.
- Conversions are required when different numeric types are mixed in an expression or assignment. For instance `int` and `int32/int64` (depending on the system/architecture) are not the same type even though they are the same size


### Float

> A float variable, stores floating point numbers (real numbers).

- Floats can also have a precision defined.
    - `float32`, `float64`

## String Type

> A String value is a sequence of bytes.

- They can be created by using `""` or with `` (a string raw literal) 
- Strings are immutable, once created it is impossible to change the contents of a string.
- Strings are sequences of bytes (alias to uint8)
- Strings and slice of bytes are treaded equivalently with these verbs
    - `%s`, the uninterpreted bytes of the string or slice
    - `%q`, a double-quted string safely escaped with Go syntax
    - `%x`, base 16, lower-case(letters in base16), two characters per byte
    - `%X`, base 16, upper-case(letters in base16), two characters per byte
    - `%#U`, Utf-8 code point