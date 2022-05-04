# def factorial(n):
#     if n == 0 or n == 1:
#         return 1

#     else:
#         return n * factorial(n-1)

# factorial(5)

# a = factorial(5)
# print(a)

factorial = int(input("Enter a number you want to factorial:"))
fact = 1
i = 0

while i<=factorial:
    factorial = factorial * factorial-1
    i = i+1
print(factorial)