# Python Data Types: From Integers Onward

This lesson introduces Python's basic, non-collection data types, starting with integers. It covers integers, floating-point numbers, complex numbers, booleans, strings, and `None`. Lists, arrays, dictionaries, and other collection or object-like types are outside the scope of this lesson.

No variables are declared in this lesson. Every example works directly with literal values or expressions.

## 1. Values, types, and literals

A **value** is a piece of data that a program can work with. A **data type** describes what kind of value it is and which operations make sense for it. A **literal** is a value written directly in Python code, such as `42`, `3.5`, or `"hello"`.

Python can report the type of a value with the built-in `type()` function:

```python
type(42)
```

Result:

```text
<class 'int'>
```

The examples in this lesson use literals directly; they do not assign values to names.

## 2. Integers (`int`)

An **integer** is a whole number with no fractional or decimal part. Integers can be positive, negative, or zero.

```python
25
-8
0
```

Python represents these values with the `int` type:

```python
type(25)
```

Result:

```text
<class 'int'>
```

### Integer arithmetic

Python supports the usual arithmetic operations on integers:

| Operation | Symbol | Example | Result |
|---|---:|---:|---:|
| Addition | `+` | `7 + 3` | `10` |
| Subtraction | `-` | `7 - 3` | `4` |
| Multiplication | `*` | `7 * 3` | `21` |
| Division | `/` | `7 / 2` | `3.5` |
| Floor division | `//` | `7 // 2` | `3` |
| Remainder (modulo) | `%` | `7 % 2` | `1` |
| Exponentiation | `**` | `2 ** 3` | `8` |

Regular division (`/`) produces a floating-point result, even when the division is exact:

```python
8 / 2
```

Result:

```text
4.0
```

Floor division (`//`) rounds the result down to the next whole number. For negative results, “down” means toward negative infinity:

```python
-7 // 2
```

Result:

```text
-4
```

The remainder operator (`%`) gives the remainder after floor division:

```python
7 % 2
```

Result:

```text
1
```

Integers have arbitrary precision in Python: their size is limited by available memory rather than a fixed maximum integer size.

## 3. Floating-point numbers (`float`)

A **floating-point number** represents a number with a fractional part or a decimal point. Python uses the `float` type for these values.

```python
3.14
-0.5
2.0
```

Even when the decimal part is zero, a number written with a decimal point is a `float`:

```python
type(2.0)
```

Result:

```text
<class 'float'>
```

### Floating-point arithmetic

Floating-point numbers support arithmetic:

```python
1.5 + 2.25
```

Result:

```text
3.75
```

Computers store most floating-point numbers in binary. Some decimal fractions therefore cannot be represented exactly, which can produce a small rounding difference:

```python
0.1 + 0.2
```

A typical result is:

```text
0.30000000000000004
```

This is normal for binary floating-point arithmetic. For exact decimal calculations, such as financial amounts, Python also provides the `decimal` module.

### Scientific notation

Large or small floating-point values can be written with scientific notation. The letter `e` means “times ten to the power of”:

```python
1.2e3
```

Result:

```text
1200.0
```

```python
4e-3
```

Result:

```text
0.004
```

## 4. Complex numbers (`complex`)

A **complex number** has a real part and an imaginary part. Python uses `j` to mark the imaginary part:

```python
3 + 4j
```

The value above has a real part of `3` and an imaginary part of `4`. Its type is `complex`:

```python
type(3 + 4j)
```

Result:

```text
<class 'complex'>
```

Python supports arithmetic with complex numbers:

```python
(1 + 2j) + (3 + 4j)
```

Result:

```text
(4+6j)
```

Complex numbers are used in fields such as engineering, physics, and signal processing. They are usually not needed for everyday beginner programs.

## 5. Booleans (`bool`)

A **boolean** represents one of two truth values:

```python
True
False
```

The type name is `bool`:

```python
type(True)
```

Result:

```text
<class 'bool'>
```

The capitalization matters: Python uses `True` and `False`, not `true` and `false`.

Booleans are commonly produced by comparisons:

```python
5 > 2
```

Result:

```text
True
```

```python
5 == 2
```

Result:

```text
False
```

Comparison operators include:

| Meaning | Operator | Example |
|---|---:|---:|
| Equal to | `==` | `4 == 4` |
| Not equal to | `!=` | `4 != 5` |
| Less than | `<` | `2 < 5` |
| Greater than | `>` | `5 > 2` |
| Less than or equal to | `<=` | `3 <= 3` |
| Greater than or equal to | `>=` | `5 >= 3` |

Boolean logic combines or reverses truth values:

```python
True and False
```

Result:

```text
False
```

```python
True or False
```

Result:

```text
True
```

```python
not True
```

Result:

```text
False
```

In Python, `bool` is a subtype of `int`: `True` behaves like `1` and `False` behaves like `0` in some numeric operations. Although Python allows this, beginners should generally use booleans for truth values and integers for counting or arithmetic.

## 6. Strings (`str`)

A **string** is text: a sequence of characters enclosed in quotes. Python calls this type `str`.

```python
"Hello, Python!"
'A string can use single quotes too.'
```

Both single and double quotes can create strings. Use the other kind of quote inside a string when convenient:

```python
"It's a sunny day."
'The word "Python" is in quotation marks.'
```

Triple quotes can represent text that spans multiple lines:

```python
"""This text
uses more than one line."""
```

The type of a string can be checked with `type()`:

```python
type("hello")
```

Result:

```text
<class 'str'>
```

### Common string operations

The `+` operator joins strings together. This is called **concatenation**:

```python
"Hello" + " " + "there"
```

Result:

```text
'Hello there'
```

The `*` operator repeats a string when multiplied by an integer:

```python
"ha" * 3
```

Result:

```text
'hahaha'
```

Strings are **immutable**: once a string value is created, its characters cannot be changed in place. Operations that appear to alter text produce a new string value.

### Text and numbers are different types

A number written inside quotes is text, not a numeric value:

```python
type("42")
```

Result:

```text
<class 'str'>
```

Python does not automatically add a string to an integer:

```python
"Age: " + 12
```

This raises a `TypeError`. Convert one value explicitly when combining text and a number; conversion is covered below.

## 7. The absence of a value: `None` (`NoneType`)

`None` is a special value that represents the absence of a value. Its type is called `NoneType`:

```python
type(None)
```

Result:

```text
<class 'NoneType'>
```

`None` is not the same as `0`, `False`, or an empty string. Those are values of other types:

```python
type(0)
type(False)
type("")
```

`None` is often used to indicate that a function has no meaningful result or that a value is intentionally absent. To check for it, use the identity comparison `is`:

```python
None is None
```

Result:

```text
True
```

## 8. Checking and converting types

Use `type()` to inspect the exact type of a value:

```python
type(10)
type(10.0)
type("10")
```

Use `isinstance()` to check whether a value belongs to a type:

```python
isinstance(10, int)
```

Result:

```text
True
```

Python provides built-in functions for common conversions:

| Function | Example | Result |
|---|---|---|
| `int()` | `int("25")` | `25` |
| `float()` | `float("3.5")` | `3.5` |
| `str()` | `str(42)` | `'42'` |
| `bool()` | `bool(1)` | `True` |
| `complex()` | `complex("2+3j")` | `(2+3j)` |

Conversion must be possible for the supplied value. For example, this is valid:

```python
int("25")
```

But converting text that is not a whole-number representation raises a `ValueError`:

```python
int("hello")
```

Converting a floating-point number to an integer removes the fractional part; it does not round to the nearest integer:

```python
int(3.9)
```

Result:

```text
3
```

`bool()` follows Python's truth-value rules. Zero, empty text, and `None` are false; nonzero numbers and non-empty text are true:

```python
bool(0)
bool("")
bool(None)
bool(7)
bool("Python")
```

Results, in order:

```text
False
False
False
True
True
```

## 9. Quick reference

| Type | Example literal | General meaning |
|---|---|---|
| `int` | `42` | Whole number |
| `float` | `3.14` | Floating-point number |
| `complex` | `3 + 4j` | Number with real and imaginary parts |
| `bool` | `True` | Truth value: `True` or `False` |
| `str` | `"Hello"` | Text |
| `NoneType` | `None` | Absence of a value |

## 10. Practice without declaring variables

Evaluate each expression and identify its type:

1. `18 // 5`
2. `18 / 5`
3. `2 ** 4`
4. `type(-12)`
5. `type(6.0)`
6. `type(2 + 5j)`
7. `9 >= 9`
8. `"Py" + "thon"`
9. `None is None`
10. `str(2026)`

You can check a result directly in Python by passing the expression to `print()` or `type()`, without assigning it to a variable:

```python
print(18 // 5)
type(18 / 5)
```

## Key points

- Every Python value has a type.
- `int`, `float`, and `complex` are Python's built-in numeric types.
- `bool` represents `True` or `False`.
- `str` represents text; quoted digits are still text.
- `None` represents the absence of a value and has type `NoneType`.
- Arithmetic and comparisons produce values; comparisons produce booleans.
- Conversions should be explicit when text and numbers need to work together.
- This lesson uses literal values directly and does not declare variables.
