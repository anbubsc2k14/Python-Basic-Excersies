# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 22:34:26 2019

@author: Dell
"""
Type = 'outer'

class SuperHeroGT():
    
    Type = 'Hero'    
    def __init__(self):
        Type = 'Villan'
        print(Type)
        
    def prn_gob(self):
        global Type
        print(Type)
                
    def prn_clss_v(self):
        print(self.Type)
        
    def __del__(self):
       print( 'SuperHeroGT Destroyed')
        
Vegeta = SuperHeroGT() 
Vegeta.prn_gob()
print(Vegeta.Type)
Vegeta.prn_clss_v()
del Vegeta