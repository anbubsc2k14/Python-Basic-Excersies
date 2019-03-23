# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 21:05:10 2019

@author: Anbu Ananda
"""

inv_str = ''
inp_str = 'abcdef'

indx = -1

for i in inp_str:
    inv_str += inp_str[indx]
    indx -= 1
print('In reverse order:',inv_str)