#!/usr/bin/env python3
# coding=utf8

import sys, re

expressions = [
# REGEX                                        # SUBEX
( r'^\w',                                      '    \\g<0>'                ),
( r'^\s{0,3}(\w)|^\s{5,9}(\w)',                '    \\g<1>'                ),
( r'(^\s{0,}\w{3})(\s{0,})(=)(\s{0,})(\{)',    '\\g<1>       \\g<3> \\g<5>'),
( r'(^\s{0,}\w{4})(\s{0,})(=)(\s{0,})(\{)',    '\\g<1>      \\g<3> \\g<5>' ),
( r'(^\s{0,}\w{5})(\s{0,})(=)(\s{0,})(\{)',    '\\g<1>     \\g<3> \\g<5>'  ),
( r'(^\s{0,}\w{6})(\s{0,})(=)(\s{0,})(\{)',    '\\g<1>    \\g<3> \\g<5>'   ),
( r'(^\s{0,}\w{7})(\s{0,})(=)(\s{0,})(\{)',    '\\g<1>   \\g<3> \\g<5>'    ),
( r'(^\s{0,}\w{8})(\s{0,})(=)(\s{0,})(\{)',    '\\g<1>  \\g<3> \\g<5>'     ),
( r'(^\s{0,}\w{9})(\s{0,})(=)(\s{0,})(\{)',    '\\g<1> \\g<3> \\g<5>'      ),
]

print('Input BibTeX:')

lines = []
while True:
    try:
        line = input()
    except EOFError:
        break
    lines.append(line)
lines = '\n'.join(lines)

for regex, subex in expressions:
    lines = re.sub(regex, subex, lines, 0, re.MULTILINE)
result = lines

if result:
    print (result)

sys.exit(0)

##################################################################################################

# EXAMPLE BibTeX TEST-STRING
'''
testr = (
    "@article{Vogel,\n"
    "doi = {10.1016/0025-5564(79)90080-4},\n"
    "title = {A Better Way to Construct the Sunflower Head},\n"
    "author = {Helmut Vogel},\n"
    "publisher = {Elsevier Science},\n"
    "journal = {Mathematical Biosciences},\n"
    "issn = {0025-5564},\n"
    "year = {1979},\n"
    "volume = {44},\n"
    "issue = {3-4},\n"
    "pages = {119–189},\n"
    "url = {http://doi.org/10.1016/0025-5564%2879%2990080-4}\n"
    "}\n"
    "@book{Vaudenay,\n"
    " title =     {A Classical Introduction to Cryptography - Exercise Book},\n"
    " author =    {Serge Vaudenay, Thomas Baigneres, Pascal Junod, Yi Lu, Jean Monnerat},\n"
    " publisher = {Springer},\n"
    " isbn =      {0-387-27934-2,978-0-387-27934-3,9780387258805,0387258809},\n"
    " year =      {2006},\n"
    " series =    {},\n"
    " edition =   {},\n"
    " volume =    {},\n"
    "}\n")
'''

##################################################################################################
