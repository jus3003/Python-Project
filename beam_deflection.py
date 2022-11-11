# -*- coding: utf-8 -*-
"""
Created on Sat Nov  5 22:46:21 2022
@author: Rachel
"""
import numpy as np

#first creating functions for the area and the moment of inertia
#Area and moment of inertia for circle and rectangle 
#R is the radius
#B is the base and H is the height
#L is the length
#A is from left support to load (or the distributive load)
#these are not necessary, but if you needed them separately here they are
def Circle(R):
    Area = np.pi*R**2
    Dia = 2*R
    MoI = (1/64)*np.pi*Dia**4
    print('The area is:',Area)
    print('MoI is:', MoI)
def Rectangle(B,H): 
    Area = B*H
    MoI = (1/12)*B*H**4
    print('The area is:',Area)
    print('MoI is:', MoI)   

#if not there it is a 0
#supports: fix, none, tri, roll 
#loads can be 'A' on left,'B' on right,'L' across the whole thing
#these calculations are for one type of load only
def BD(R,B,H,L,A,C,End_L,End_R,q,P,Mo,load_location,E):
    #first calculating the area and moment of inertia
    if R == 0:
        #Shape is a rectangle haha
        Area = H*B
        MoI = (1/12)*B*H**4
        print('The area is:',Area)
        print('MoI is:', MoI)
    elif B == 0:
        #shape is a circle 
        Area = np.pi*R**2
        Dia = 2*R
        MoI = (1/64)*np.pi*Dia**4
        print('The area is:',Area)
        print('MoI is:', MoI)
    else:
        print('Error, no shape given')
    
    #now these will be the fix and none - deflections  and angle 
    if End_L == 'fix':
        #even distributive load first (triangular loads will be q0)
        if q != 0:
            if load_location == 'L': #means that the distributive load is across the whole bar
                deflection = (q*L**4)/(8*E*MoI)
                angle = (q*L**3)/(6*E*MoI)
                print('Deflection:',deflection)
                print('Angle:',angle)
            elif load_location == 'A': #meaning the load is on the left side
                deflection = (4*L-A)*(q*A**3) /(24*E*MoI)
                angle = (q*A**3)/(6*E*MoI)
                print('Deflection:',deflection)
                print('Angle:',angle)
            elif load_location == 'B': #meaning load is on the right side
                deflection = ((3*L**4)-(4*L*A**3)+A**4)*q/(24*E*MoI)
                angle = ((L**3)-(A**3))*q/(6*E*MoI)
                print('Deflection:',deflection)
                print('Angle:',angle)
            else: #something is wrong because someone put the wrong input into the code
                print('Error-did not write location of load')
        #point loads
        if P != 0:
            if load_location == 'L': #meaning the load is at the end
                deflection = (P*L**3)/(3*E*MoI)
                angle = (P*L**2)/(2*E*MoI)
                print('Deflection:',deflection)
                print('Angle:',angle)
            elif load_location == 'A': #meaning the load is on the left side
                deflection = (3*L-A)*(P*A**2)/(6*E*MoI)
                angle = (P*A**2)/(2*E*MoI)
                print('Deflection:',deflection)
                print('Angle:',angle)
            else: #something is wrong because someone put the wrong input into the code
                print('Error-did not write location of load')
        #moments
        if Mo != 0:
            if load_location == 'L': #the moment is at the right end of beam
                deflection = (Mo*L**2)/(2*E*MoI)
                angle = (Mo*L)/(E*MoI)
                print('Deflection:',deflection)
                print('Angle:',angle)
            elif load_location == 'A':
                deflection = (2*L-A)*(Mo*A)/(2*E*MoI)
                angle = (Mo*A)/(E*MoI)
                print('Deflection:',deflection)
                print('Angle:',angle)
            else: #something is wrong because someone put the wrong input into the code
                print('Error-did not write location of load')                
        #can add triangular loads here if you think we need more this is already a lot of cases

            
    #now these will be the tri and roll - deflection and angle
    #due to the nature of the tri and roll ones the options I am putting are L,L/2
    elif End_L == 'tri':
        if q != 0:
            if load_location == 'L': #load throughout the whole thing
                deflection = (5*q*L**4)/(384*E*MoI)
                angle = (q*L**3)/(24*E*MoI)
                print('Deflection:',deflection)
                print('Angle:',angle)
            elif load_location == 'l/2': #is if the load is on L/2 of the beam (left side)
                deflection = (5*q*L**4)/(768*E*MoI)
                angle_left = ((3*q*L**3))/(128*E*MoI)
                angle_right = (7*q*L**3)/(384*E*MoI)
                print('Deflection:',deflection)
                print('Angle (left):',angle_left)
                print('Angle (right):',angle_right)
            else:
                print('Error-did not write location of load')
        if P != 0:
            if load_location == 'L/2': #one load in the middle
                deflection = (P*L**3)/(48*E*MoI)
                angle = (P*L**2)/(16*E*MoI)
                print('Deflection:',deflection)
                print('Angle:',angle)
            else:
                print('Error-did not write location of load')
        if Mo != 0:
            if load_location == 'L/2': #located in the middle
                deflection = 0
                angle_left = (Mo*L)/(24*E*MoI)
                angle_right = -1*angle_left
                print('Deflection:',deflection)
                print('Angle (left):',angle_left)
                print('Angle (right):',angle_right)
            else:
                print('Error-did not write location of load')