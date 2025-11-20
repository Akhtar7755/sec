from typing import Union
import sys

Number = Union[int, float]

def add(a: Number, b: Number) -> Number:
    """Return the sum of two numbers (int or float)."""
    return a + b

if __name__ == "__main__":
    try:
        a = float(sys.argv[1]) if len(sys.argv) > 1 else 1.0
        b = float(sys.argv[2]) if len(sys.argv) > 2 else 2.0
        result = add(a, b)
        if isinstance(result, float) and result.is_integer():
            result = int(result)
        print(result)
    except Exception:
        print("Usage: python main.py [a] [b]")