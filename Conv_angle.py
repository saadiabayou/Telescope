# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 15:25:37 2021

@author: Saadia Bayou
"""

# import biblio math
import math

# valeur numérique - varaible pi 
pi=math.pi



# UNITE ANGLE de DEPART -> DEGRE   
def deg_rad(angle):
    """ Convertie un angle en DEGRE vers -> RADIAN"""
    return (angle*(pi/180))
    
def deg_arcmin(angle):
    return (angle*60)

def deg_arcsec(angle):
    return (angle*3600)

def deg_milliarcsec(angle):
    return (angle *3600000)



# UNITE ANGLE de DEPART -> RADIAN  
def rad_deg(angle):  
    return (angle*(180/pi))
            
def rad_arcmin(angle):
    return (angle*((60*180)/pi))

def rad_arcsec(angle):
    return (angle*((3600*180)/pi))

def rad_milliarcsec(angle):   
    return (angle*((3600000*180)/pi))
    
    

# UNITE ANGLE de DEPART -> ARCSECONDE    
def arcsec_rad(angle):
    return ((angle*pi)/(180*3600))
    
def arcsed_milliarcsec(angle):      
        return (angle*1000)
# return angle /2,063e+8
        
def arcsec_deg (angle):
    return (angle/3600)    
    
def arcsec_arcmin(angle):
    return (angle/60)


         
## UNITE ANGLE de DEPART -> MILI ARCSECONDE  
#def milliarcsec_rad(angle):
#    
#    
#def miliarcsed_arcsec(angle): 
#         
#def milliarcsec_deg (angle):    
#    
#def miliarcsec_arcmin(angle):    
#    
#


    
## UNITE ANGLE de DEPART -> ARCMIN       
#def arcmin_deg(angle):
#    
#def arcmin_rad(angle):      
#
#def arcmin_arcsec(angle):    
#
#def arcmin_arcsec(angle):      

