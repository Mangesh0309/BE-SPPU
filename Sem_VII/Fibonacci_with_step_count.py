# Program to compute fibonacci numbers with step count
def fibonacci(n):
    steps = 0
    
    if n == 0:
        steps += 1
        return 0,  steps
    elif n ==1:
        steps += 1
        return 1, steps
    

    #Recursive calls
    fib1, steps1 = fibonacci(n-1)
    fib2, steps2 = fibonacci(n-2)

    steps += steps1 + steps2 + 1  # +1 is to count the current addition step
    return fib1 + fib2, steps

# Taking input from user
n = int(input("Enter a positive integer to compute its Fibonacci number:"))
fib, step_count = fibonacci(n)

print(f"Fibonacci number for {n} is {fib}")
print(f"Total steps taken to compute Fibonacci({n}): {step_count}")


