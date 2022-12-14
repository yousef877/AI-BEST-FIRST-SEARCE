# -*- coding: utf-8 -*-
"""BackTracking.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/github/JehadT/AI-Lab-III/blob/main/BackTracking.ipynb
"""

def permute(list, s):
    if list==1:
        return s
    else:
        return [
            x+y
            for y in permute(1, s) 
            for x in permute(list - 1, s)
        ]
print(permute(1, ["a", "b", "c"])) 
print(permute(2, ["a", "b", "c"])) 
print(permute(3, ["a", "b", "c"]))