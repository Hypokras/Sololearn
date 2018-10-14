"""
Dice Game
Coded by Marc Maurer (c) 2018
Let the computer play a dice game for you
The code rolls the dices for himself and for you based on randomly generated numbers 
Original code: https://code.sololearn.com/cXz4pBSAXE30/#py
"""
"""
I was inspired by Turjas code. It's a bit like reinventing the wheel, but for the purpose of practicing my skills
with functions. So I turned Turjas code into one with functions, which shortend the script.
Here you can see the original script: https://code.sololearn.com/cbQ73Vkj1mub/#py
"""
"""
Update 2018-09-17: The function "second_row_of_cube" looks now a little bit more like Python than before. The vars
are not changed to str anymore and the values are in lists, so an iteration is possible and they are still int.
"""

# -*- coding: utf-8 -*-

import random

"""begin datatype definition"""

i = "=","×","_","-",":","*","^","~","-"
top = " _______      _______"
bottom = "|_______|    |_______|"
space = "    "
null = "|       |"
eins = "|   #   |"
zwei = "|  # #  |"
cube_nr = []
d=[1,2],[1,3],[1,4],[1,5],[1,6],[2,3],[2,4],[2,5],[2,6],[3,4],[3,5],[3,6],[4,5],[4,6],[5,6],[1,1],[2,2],[3,3],[4,4],[5,5],[6,6]
first_row = ""
second_row = ""
third_row = ""

"""end datatype definition"""


"""begin function definition"""

def cube_sum(d):
# The specific pair of cubes will be "chosen" and the sum of both cubes calculated.

    buffer = 0
    cube_nr = ((random.choice(d)))
    buffer = cube_nr[0]+cube_nr[1]
    
    return (cube_nr, buffer)

def random_line():
# The delimiter-lines between the displayed cubes and the results etc. will be created
# and printed.

    print((random.choice(i)*38))

def first_row_of_cube(cube_nr):
# Since the top and bottom lines of every cube are the same, the three lines that contain
# the dots that represent the cube's value are chosen according to the cubes nr. Here
# the first of the three lines is chosen.

    if cube_nr[1] <= 4:
        first_row = (null + space + null)
    elif cube_nr[0] >= 5:
        first_row = (zwei + space + zwei)
    else:
        first_row = (null + space + zwei)
    
    return first_row

def second_row_of_cube(cube_nr):
# Same as for the first line, but for the second.
# This if was the toughest of the whole script

    one_two_five = [1, 2, 5]
    three_four_six = [3, 4, 6]

    if cube_nr == 55:
        second_row = (eins + space + zwei)
    elif cube_nr[0] in three_four_six:
        if cube_nr[1] == 5:
            second_row = (zwei + space + eins)
        elif cube_nr[1] in three_four_six:
            second_row = (zwei + space + zwei)
    elif cube_nr[1] in one_two_five:
        second_row = (eins + space + eins)
    else:
        second_row = (eins + space + zwei)

    return second_row
    
def third_row_of_cube(cube_nr):
# And for the third line with dots

    if cube_nr[0] >= 4:
        third_row = (zwei + space + zwei)
    elif cube_nr[0] >=2:
        if cube_nr[1] >= 4:
            third_row = (eins + space + zwei)
        else:
            third_row = (eins + space + eins)
    elif cube_nr[1] >= 4:
        third_row = (null + space + zwei)
    elif cube_nr[1] == 1:
        third_row = (null + space + null)
    else:
        third_row = (null + space + eins)

    return third_row

def print_dice():
# Here the cube is assembled and printed

    print(top)
    print(first_row_of_cube(cube_nr))
    print(second_row_of_cube(cube_nr))
    print(third_row_of_cube(cube_nr))
    print(bottom)

"""end of function definition"""

# Ask for the users name
print("Enter name please")
name = str(input())

# print random delimiter line
random_line()

# call cube_sum and print pair of dices before ...
cube_nr, sum_human = cube_sum(d)
print_dice()

# ... print the result for the human player
print(name,"rolled",cube_nr,"total point is",sum_human,".")

# call cube_sum and print pair of dices before ...
cube_nr, sum_comp = cube_sum(d)
print_dice()

# ... print the result for the computer player
print("Mr.computer rolled",cube_nr,"total point",sum_comp,".")

# print random delimiter line
random_line()

# check who's the winner and print the result
if sum_human > sum_comp :
    print(name,"is the winner.")
    print("plz leave an upvote.")
elif sum_human < sum_comp :
    print("Mr.Computer is the winner.")
    print("( × _ × )")
    print("Try again.")
else :
    print("It's a draw.")
    print("I hope you enjoyed.")

# print random delimiter line
random_line()

#________________________________________#
#           Inspired by Turja.           #
#           Condensed by Marc            #
#                   ;)                   #
