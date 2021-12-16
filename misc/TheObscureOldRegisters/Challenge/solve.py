# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 23:10:12 2021

@author: franc
"""

code = {
    'A' : '1' ,
    'B' : '2' , 
    'C' : '3' ,
    'D' : '4-1' ,
    'E' : '4-2' ,
    'F' : '5-1' ,
    'G' : '5-2' ,
    'H' : '6' ,
    'I' : '7-1' ,
    'J' : '7-2' ,
    'K' : '8-1',
    'L' : '8-2' ,
    'M' : '9' ,
    'N' : '10' ,
    'O' : '11' ,
    'P' : '12-1' ,
    'Q' : '12-2' ,
    'R' : '13' ,
    'S' : '14' ,
    'T' : '15' ,
    'U' : '16-1' ,
    'V' : '16-2' ,
    'W' : '17-1' ,
    'X' : '17-2' ,
    'Y' : '18-1' ,
    'Z' : '18-2' ,
}

string = '7-1 4-1 4-2 8-1 1 1 1 9 1 8-1 7-1 10 5-2 1 1 1 2 7-1 5-2 1 1 1 5-1 8-2 1 5-2 14 1 1 1 7-2 16-1 14 15 1 1 1 15 11 1 1 1 9 1 8-1 4-2 1 1 1 18-1 11 16-1 1 1 1 16-1 14 4-2 1 1 1 1 1 1 1 14 3 13 7-1 12-1 15 1 1 1 11 13 1 1 1 2 4-2 1 1 1 1 10 10 11 18-1 4-2 4-1 1 1 1 1 15 1 1 1 9 4-2 1 1 1 4-2 6 4-2 6 4-2 6 1 1 1 17-1 11 17-1 1 1 1 9 1 8-1 7-1 10 5-2 1 1 1 2 7-1 5-2 1 1 1 14 15 13 7-1 10 5-2 14 1 1 1 13 4-2 1 8-2 8-2 18-1 1 1 1 7-1 14 1 1 1 1 1 1 1 2 16-1 9 9 4-2 13 1 1 1 2 16-1 15 1 1 1 11 6 1 1 1 17-1 4-2 8-2 8-2 1 1 1 7-1 1 1 1 5-2 16-1 4-2 14 14 1 1 1'

values = string.split(' ')
print(values)
flag = ""
for j in values:
    for l in code:
        if code[l] == j:
            flag += l
print(flag)
'''
    Output:
    IDEKAAAMAKINGAAABIGAAAFLAGSAAAJUSTAAATOAAAMAKEAAAYOUAAAUSEAAAAAAASCRIPTAAAORAAABEAAAANNOYEDAAAATAAAMEAAAEHEHEHAAAWOWAAAMAKINGAAABIGAAASTRINGSAAAREALLYAAAISAAAAAAABUMMERAAABUTAAAOHAAAWELLAAAIAAAGUESSAAA
'''