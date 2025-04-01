def fibonacci(n):
    """Compute the nth Fibonacci number efficiently.
    
    Args:
        n: A non-negative integer
        
    Returns:
        The nth Fibonacci number
        
    Raises:
        ValueError: If n is negative
    """
    if n < 0:
        raise ValueError("Fibonacci sequence is only defined for n >= 0")
    if n == 0:
        return 0
    a, b = 0, 1  # F(0) = 0, F(1) = 1
    for _ in range(2, n + 1):
        a, b = b, a + b  # Update values iteratively
    return b


# Test the function
if __name__ == "__main__":
    print(fibonacci(5))   # Should output 5
    print(fibonacci(10))  # Should output 55
    try:
        print(fibonacci(-1))  # Should raise an error
    except ValueError as e:
        print(f"Error: {e}")  # Expected: "Fibonacci sequence is only defined for n >= 0"