#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Module docstring: One line description of what your program does.
"""

with open('input.txt', "r") as rf:
  with open('output.txt', 'w') as wf:
    for line in rf:
      wf.write(line)


def nested_brackets(string):
  opening_list = []
  if string == "":
    return 'YES'
  for char in string:
    if char == '(':
      opening_list.append(char)
    elif char == ')' and len(opening_list)>=1:
      opening_list.pop()
    elif char == ')' and len(opening_list)==0:
      return 'NO'
  if len(opening_list)==0:
    return 'YES'   
  return 'NO'
    
__etallman__ = "Your Github Username"

import sys

def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{} got: {} expected: {}'.format(prefix, repr(got), repr(expected)))
    
def main(args):
    """Add your code here"""
    print('nested_brackets')
    test(nested_brackets('(*a++(*)'), 'NO')# 6)
    test(nested_brackets('(*a{+}*)'), 'YES')
    test(nested_brackets('    <************)>'), 'NO')# 17)
    test(nested_brackets('    ()(***)(**)'), 'YES')
    test(nested_brackets('   ()(***)(*)'), 'NO')# 10)
    test(nested_brackets('({{}{}}[{(){}[]}'), 'NO')# 17)
    test(nested_brackets('   ([))'), 'NO')# 6)
    test(nested_brackets(' ()(**)'), 'YES')
    test(nested_brackets('    ()*'), 'YES')
    test(nested_brackets(' aaaaaaa'), 'YES')
    test(nested_brackets('    aaa(aaaa'), 'NO') #13)
    test(nested_brackets(' *******'), 'YES')

if __name__ == '__main__':
    main(sys.argv)