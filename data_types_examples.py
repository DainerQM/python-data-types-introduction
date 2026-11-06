"""Print beginner-friendly Python data type examples to the terminal.

Run this file with:
    python data_types_examples.py

The examples use literal values directly and do not declare variables.
"""

print("PYTHON DATA TYPES: TERMINAL EXAMPLES")
print("=" * 42)

print("\n1. INTEGERS (int)")
print("A whole number:", 25)
print("A negative integer:", -8)
print("The type of 25:", type(25))
print("Addition (7 + 3):", 7 + 3)
print("Subtraction (7 - 3):", 7 - 3)
print("Multiplication (7 * 3):", 7 * 3)
print("Division (7 / 2):", 7 / 2)
print("Floor division (7 // 2):", 7 // 2)
print("Floor division with a negative result (-7 // 2):", -7 // 2)
print("Remainder (7 % 2):", 7 % 2)
print("Exponentiation (2 ** 3):", 2**3)

print("\n2. FLOATING-POINT NUMBERS (float)")
print("A decimal value:", 3.14)
print("The type of 2.0:", type(2.0))
print("Floating-point addition (1.5 + 2.25):", 1.5 + 2.25)
print("A common binary floating-point result (0.1 + 0.2):", 0.1 + 0.2)
print("Scientific notation (1.2e3):", 1.2e3)
print("Small value in scientific notation (4e-3):", 4e-3)

print("\n3. COMPLEX NUMBERS (complex)")
print("A complex number:", 3 + 4j)
print("The type of 3 + 4j:", type(3 + 4j))
print("Complex addition:", (1 + 2j) + (3 + 4j))

print("\n4. BOOLEANS (bool)")
print("A true value:", True)
print("A false value:", False)
print("The type of True:", type(True))
print("Comparison (5 > 2):", 5 > 2)
print("Equality check (5 == 2):", 5 == 2)
print("Logical AND (True and False):", True and False)
print("Logical OR (True or False):", True or False)
print("Logical NOT (not True):", not True)

print("\n5. STRINGS (str)")
print("A string:", "Hello, Python!")
print("The type of 'hello':", type("hello"))
print("Joining strings:", "Hello" + " " + "there")
print("Repeating a string:", "ha" * 3)
print("Digits in quotes are text:", type("42"))

print("\n6. NONE (NoneType)")
print("The special value:", None)
print("The type of None:", type(None))
print("None is None:", None is None)

print("\n7. CHECKING AND CONVERTING TYPES")
print("The type of 10:", type(10))
print("The type of 10.0:", type(10.0))
print("The type of '10':", type("10"))
print("Is 10 an integer?:", isinstance(10, int))
print("Convert text to an integer:", int("25"))
print("Convert text to a float:", float("3.5"))
print("Convert a number to text:", str(42))
print("Convert 1 to a boolean:", bool(1))
print("Convert text to a complex number:", complex("2+3j"))
print("Convert 3.9 to an integer (fraction is removed):", int(3.9))

print("\n8. BOOLEAN CONVERSION")
print("bool(0):", bool(0))
print("bool(''):", bool(""))
print("bool(None):", bool(None))
print("bool(7):", bool(7))
print("bool('Python'):", bool("Python"))

print("\n9. PRACTICE EXPRESSIONS")
print("18 // 5:", 18 // 5)
print("18 / 5:", 18 / 5)
print("2 ** 4:", 2**4)
print("type(-12):", type(-12))
print("type(6.0):", type(6.0))
print("type(2 + 5j):", type(2 + 5j))
print("9 >= 9:", 9 >= 9)
print("'Py' + 'thon':", "Py" + "thon")
print("None is None:", None is None)
print("str(2026):", str(2026))

print("\nEnd of examples. No variables were declared.")
