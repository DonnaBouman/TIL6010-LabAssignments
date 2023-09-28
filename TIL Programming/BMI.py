# This program calculates body mass index of users using their weight and height. 

import os    

os.system("clear")

# YOUR CODE HERE! 

def ask_height():
    height = input('What is your height? ')

    if height > 3:
        height = height / 100
    
    return height
    
def ask_weight():
    weight = input('What is your weight? ')
    return weight

def ask_age():
    age = input('What is your age? ')

    if 18 < age < 65:
        return age
    else:
        return 'Sorry, your age is not compatible'

def measuring():
    height = ask_height
    weight = ask_weight
    age = ask_age

    if isinstance(age, int) == False:
        return 'One of the fields was not filled in completely'

    return ask_height/ask_weight