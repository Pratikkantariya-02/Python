def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))

# in this code line was repeated in infinite time

# def factorial(n):
#     return n * factorial(n-1)

# print(factorial(5))