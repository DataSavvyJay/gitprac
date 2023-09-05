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
# Done using recursion

def division(a,b):
    try:
<<<<<<< HEAD
        return a/b*10
=======
        return a/b*2
>>>>>>> 22c5f88ecc97d72b7802550aba92a2d9996476cf
    except:
        print("sorry cant be processed")
        ###yeah
