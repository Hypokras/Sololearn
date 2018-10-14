"""
Insult Generator
Coded by Marc Maurer (c) 2018
Generates randomly combined insults based on three lists 
Original code: https://code.sololearn.com/cFtZwA7OwnFk/#py
"""

# -*- coding: utf-8 -*-

# May this little code example help someone to overcome the
# hurdle of importing files to dictionairies.

# Now it has only one function to create the opener-, middle- and closer-part of the insult.
# The textfiles with the insult parts and the indexes look like this:
# 1;backward
# 2;babbling
# 3;barbed
# 4;beardless
# ...
# 100;yellow-bellied

# If you have any improvements regarding efficiency or clarity, please let me know in the comments.

from random import randint

insult_part = {}
insult_index = 0
pattern_index = 0
insult_file = ""
buffer = ""

""" begin of function definition """

def open_insultfile(insult_txt):

    with open(insult_txt, "r", encoding="utf-8-sig") as fobj:
    # Every line of the given file will be read and loaded into the dictionary
    # 'insult_part'

        for line in fobj:
            line = line.strip()
            name = line.split(";")
            insult_part[int(name[0])] = name[1]

    return insult_part


def insult(omc):
    partial_insult = ""

    if omc == "opener":
        insult_file = "Insult_Dwarf_01.txt"
    elif omc == "middle":
        insult_file = "Insult_Dwarf_02.txt"
    else:
        insult_file = "Insult_Dwarf_03.txt"

    open_insultfile(insult_file)
    insult_index = randint(1,100)
    buffer = (insult_part[insult_index])
    partial_insult = '%s' % (buffer)

    return partial_insult
    
""" end of function definition """

pattern_index = randint(1,20)

if pattern_index < 7:
    print(insult("opener"), insult("middle"), insult("closer"))
elif pattern_index < 9:
    print(insult("opener"), insult("opener"), insult("middle"), insult("closer"))
elif pattern_index < 11:
    print(insult("opener"), insult("middle"), insult("middle"), insult("closer"))
elif pattern_index < 13:
    print(insult("opener"), insult("opener"), insult("middle"), insult("middle"), insult("closer"))
elif pattern_index < 15:
    print(insult("opener"), insult("middle"), insult("opener"), insult("closer"))
elif pattern_index < 17:
    print(insult("opener"), insult("middle"), insult("opener"), insult("middle"), insult("closer"))
elif pattern_index < 19:
    print(insult("opener"), insult("middle"), insult("middle"), insult("opener"), insult("closer"))
else:
    print(insult("opener"), insult("closer"))
