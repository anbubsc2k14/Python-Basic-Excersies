# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 16:39:47 2019

@author: Dell
"""

inp_list = [2,1,4]
srtd_lst = []
cntr = 0
bof = 1

for i in inp_list:
    if bof == 1:
        srtd_lst.append(i)
        #print(srtd_lst)
        bof = 0
    else:
        if i < srtd_lst[cntr]:
            srtd_lst.insert(cntr -1,i)
            #print('@if',srtd_lst)
        elif i > srtd_lst[cntr]:
            srtd_lst.insert(cntr +1,i)
           # print('@els',srtd_lst)
        cntr += 1
print('Sorted List',srtd_lst)