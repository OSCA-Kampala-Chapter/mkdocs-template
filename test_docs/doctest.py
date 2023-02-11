def add(a, b):
    """Compute and return the sum of two numbers.

    Args:
        a (float): A number representing the first addend in the addition.
        b (float): A number representing the second addend in the addition.

    Returns:
        float: A number representing the arithmetic sum of `a` and `b`.
    """
    return float(a + b)

def subtract(a, b):
    """Calculate the difference of two numbers.

    Args:
        a (float): A number representing the minuend in the subtraction.
        b (float): A number representing the subtrahend in the subtraction.

    Returns:
        float: A number representing the difference between `a` and `b`.
    """
    return float(a - b)

def multiply(a, b):
    """Compute and return the product of two numbers.

    Args:
        a (float): A number representing the multiplicand in the multiplication.
        b (float): A number representing the multiplier in the multiplication.

    Returns:
        float: A number representing the product of `a` and `b`.
    """
    return float(a * b)

def divide(a, b):
    """Compute and return the quotient of two numbers.

    Args:
        a (float): A number representing the dividend in the division.
        b (float): A number representing the divisor in the division.

    Returns:
        float: A number representing the quotient of `a` and `b`.

    Raises:
        ZeroDivisionError: An error occurs when the divisor is `0`.
    """
    if b == 0:
        raise ZeroDivisionError("division by zero")
    return float(a / b)