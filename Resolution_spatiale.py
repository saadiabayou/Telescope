#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 17:25:01 2021

@author: saadia
"""


""" Ce programme calcul la résolution spatiale théta d'un télescope
    de diamètre D d'un rayon lumineux de longeur d'onde donnée"""


lambd=float(input("Entrez la longeur d'onde lambda ="))
D=float(input("Entrez le diamètre D = "))    

  
def res_spa(lambd, D):
    theta=lambd/D
    return theta

res_spa=res_spa (lambd,D)
print("La résolution spatiale théta = ", res_spa, "radian")
