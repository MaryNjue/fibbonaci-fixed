# Fibonacci Function Fix

## Problem
The original recursive Fibonacci function was:
- Not handling negative inputs.
- Very slow for large numbers due to repeated calculations.

## Solution
1. Added input validation for negative numbers.
2. Replaced recursion with an **iterative approach** (faster & more efficient).

## Usage
```python
print(fibonacci(10))  # Output: 55