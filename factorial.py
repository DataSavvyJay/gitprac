def fac(x):
    # Base case: Return 1 when x is 1
    if x == 1:
        return 1
    else:
        # Calculate the factorial recursively by multiplying x with fac(x-1)
        return x * fac(x - 1)

# Test the function
result = fac(5)
print(result)