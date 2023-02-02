# Notes: Variables, Values & Type
---
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

## Short Declaration Operator

The short declaration operator `:=` allows to declare a variable and assign a value to that variable.

`x := 32`, Declares variabble `x` of type `int` and assigns value `32`.

When reassigning the variable the `=` operator is enough since the variable was previously declared.