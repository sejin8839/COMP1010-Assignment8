'''
# Assignment written by: Sejin Yoon
'''

# Assignment 8 Part A.
# Carefully read the comments and add code where specified.

# Question 1) Write a loop (not a function) that prints out every element in the values list all on one line
# with a space between each element and ending with a new line.

values = ["Eleni", "Peter", 100]
# Write your loop after this line
for value in values:
    print(value, end=' ')
print()


# Given values above, the loop should print
# Eleni  Peter  100
#

# Question 2) Write a function called multiply that has two parameters, x and y.
# The function should return the result of multiplying x times y. Then fill in code after
# where the number1 and number2 variables are defined below to call this function
# and print the result.

# Write your function below this line
def multiply(x, y):
    return x * y


# This code will test the multiply function
number1 = 5
number2 = 10
# Below this comment, write a call to multiply with number1 and number2
# as arguments and store the result in a variable called answer.
# Then print answer
answer = multiply(number1, number2)
print(answer)

# The above code should print
# 50

# Question 3) Finish the function that is started below. Make a new list
# that contains in order from left to right every element of input_list
# that has an even index number.
# Return that new list. This is an example of an accumulation loop
# with a list 

# Finish this function by replacing the return line with your own lines
# of code.
def even_elements(input_list):
    return input_list[::2]

# The function is called with this data
even_vals = even_elements([2,3,4,5,6,7,8,9])
print(even_vals)
# The test code above should produce
#[2, 4, 6, 8]
# once you implement the function

