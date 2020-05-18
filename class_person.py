# class Person:
#     def __init__(self, initialAge):
#         # Add some more code to run some checks on initialAge
#         if initialAge < 0:
#             print("Age is not valid, setting age to 0.")
#             self._age = 0
#         else:
#             self._age = initialAge

#     def amIOld(self):
#         # Do some computations in here and print out the correct statement to the console
#         if self._age < 13:
#             print("You are young.")
#         elif (13 <= self._age) and (self._age < 18):
#             print("You are a teenager.")
#         else:
#             print("You are old.")

#     def yearPasses(self):
#         # Increment the age of the person in here
#         self._age += 1


# t = int(input())
# for i in range(0, t):
#     age = int(input())
#     p = Person(age)
#     p.amIOld()
#     for j in range(0, 3):
#         p.yearPasses()
#     p.amIOld()
#     print("")
# import random
# t = random.randint(1, 10)
# n = 2
# for i in range(1, 11):
#     result1 = n*i
#     print(n, 'x', i, '=', result1)


# for i in range(1, 11):
#     result2 = i*t
#     print(t, 'x', i, '=', result2)

# N = range(1, 10)

# if (N % 2) != 0:
#     print("Weird")
# else:
#     if (2 <= N) and (N <= 5):
#         print("Not Weird")
#     elif (6 <= N) and (N <= 20):
#         print("Weird")
#     else:
#         print("Not Weird")

# javascripts Solution
# function main() {
#     const N = parseInt(readLine(), 10);
#     if(N % 2 == 0) {
#         if(N >= 2 && N < 6) {
#             console.log('Not Weird');
#         } else if(N >= 6 && N <= 20) {
#             console.log('Weird');
#         } else if(N > 20) {
#             console.log('Not Weird');
#         }
#     } else {
#         console.log('Weird');
#     }
# }


# n = int(input())
# r = []
# if(n >= 1 and n <= 10):
#     for i in range(n):
#         r.append(input())
# for s in r:
#     print("{} {}".format(s[::2], s[1::2]))

# n = 2
# for i in range(1, 11):
#     result1 = n*i

#     print(f"{n} x {i} = {n*i}")


# #!/bin/python3

# import math
# import os
# import random
# import re
# import sys

# # Complete the factorial function below.


# def factorial(n):
#     if n == 0:
#         return 1
#     elif n < 1:
#         return -1
#     else:
#         return n * factorial(n-1)


# print(factorial(9))