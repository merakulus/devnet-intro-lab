"""Intro to Python - Part 1 - Hands-On Exercise."""

import math
import random

# TODO: Write a print statement that displays both the type and value of `pi`
pi = math.pi
print(pi)

# TODO: Write a conditional to print out if `i` is less than or greater than 50
i = random.randint(0, 100)
print(i)
if i < 50:
    print("Lower than 50")
else:
    print("highet than 50")

# TODO: Write a conditional that prints the color of the picked fruit
picked_fruit = random.choice(['orange', 'strawberry', 'banana'])
print(f"Picked Fruit: {picked_fruit}")
if picked_fruit == 'orange':
    print("orange")
elif picked_fruit == 'strawberry':
    print("red")
else:
    print("yellow")


# TODO: Write a function that multiplies two numbers and returns the result
# Define the function here.
def multitwo(num1, num2):
    result = num1 * num2
    return result


# TODO: Now call the function a few times to calculate the following answers

print("12 x 96 =", )
print(multitwo(12, 96))
print("48 x 17 =", )
print(multitwo(48, 17))
print("196523 x 87323 =", )
print(multitwo(196523, 87323))