# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 22:06:15 2019

@author: Dell
"""

class SuperHero():
    
    Type = 'Villan'
    
    def __init__(self):
        Type = 'Hero'
        print(Type)
        
class SuperHeroGT():
    
    #Type = 'Villan' #
    
    def __init__(self):
        Type = 'Hero'
        print(Type)
    def __del__(self):
       print( 'SuperHeroGT Destroyed')
        
Vegeta = SuperHeroGT() 
del Vegeta

# Try the commented print Statement
#Here It throws Error because we dont have Class Variable 'Type'. Variable declared inside Constructor canoot be explictly called using Object

#print(Vegeta.Type) 

SuperMan = SuperHero()
print('SuperMan',SuperMan.Type)

