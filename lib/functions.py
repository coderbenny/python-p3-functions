#!/usr/bin/env python3

# def my_function(param):
#     print("Running my_function")
#     return param + 1

# my_function_return_value = my_function(1)
# print(my_function_return_value)

def greet_programmer():
    print("Hello, programmer!")

greet_programmer()

def greet(name):
    print(f"Hello, {name}!")

greet("Naureen")

def greet_with_default(name="programmer"):
    print(f"Hello, {name}!")

greet_with_default("Sunny")

def add(num1, num2):
    sum = num1 + num2
    print(sum)
    return sum

add(1,2)

def halve(number):
    if isinstance(number, (int,float)):
        result = number / 2
        print(result)
        return result
    else:
        return None

halve(12)