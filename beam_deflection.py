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
#now BD(radius,base,height,length,location of load,distributive,point,moment,E)
#if ou really wanted we can change q,P,Mo to a choice and make it load then do what i did for support-up to you
def BD(R,B,H,L,A,support,q,P,Mo,E):
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
    if support == 'fix':
        #even distributive load first (triangular loads will be q0)
        if q != 0:
            #since all are location a now I removed the conditional
            deflection = (4*L-A)*(q*A**3) /(24*E*MoI)
            angle = (q*A**3)/(6*E*MoI)
            #you can specify if you want the location (angle is at the left and deflection is at the right for all these cases)
            print('Deflection:',deflection)
            print('Angle:',angle)

        #point loads
        if P != 0:
            #a location
            deflection = (3*L-A)*(P*A**2)/(6*E*MoI)
            angle = (P*A**2)/(2*E*MoI)
            print('Deflection:', deflection)
            print('Angle:',angle)

        #moments
        if Mo != 0:
            #a location
            deflection = (2*L-A)*(Mo*A)/(2*E*MoI)
            angle = (Mo*A)/(E*MoI)
            print('Deflection:',deflection)
            print('Angle:',angle)
             
    #can add triangular loads here if you think we need more this is already a lot of cases
    #now these will be the tri and roll - deflection and angle

    elif support == 'tri':
        if q != 0:
            angle_left = ((2*L-A)**2)*(q*(A**2))/(24*L*E*MoI)
            angle_right = -1*(2*(L**2)-(A**2))*(q*(A**2))/(24*L*E*MoI)
            #deflection is in the middle
            deflection = (4*(L**2)-(7*A*L)+(3*(A**2)))*(q*(A**3))/(24*L*E*MoI)
            print('Deflection:',deflection)
            print('Angle (left):',angle_left)
            print('Angle (right):',angle_right)

        if P != 0:
            C = L - A #this is the other length (called this C instead of B since I used B for Cross-Section)
            angle_left = (L+C)*(P*A*C)/(6*L*E*MoI)
            angle_right = (L+A)*(P*A*C)/(6*L*E*MoI)
            print('Angle (left):',angle_left)
            print('Angle (right):',angle_right)
            if A >= C:
                deflection = (3*(L**2)-4*(C**2))*(P*C)/(48*E*MoI)
                print('Deflection:',deflection)
            else: #if A<C
                deflection = (3*(L**2)-4*(A**2))*(P*A)/(48*E*MoI)
                print('Deflection:',deflection)

        if Mo != 0:
            C = L - A
            angle_left = (6*A*L-(3*(A**2))-2*(L**2))*Mo/(6*L*E*MoI)
            angle_right = (3*(A**2)-(L**2))*Mo/(6*L*E*MoI)
            print('Angle (left):',angle_left)
            print('Angle (right):',angle_right)
            #I got this formula off of pinterest so...
            if A<=(L/2):
                deflection = -1*(np.sqrt(3))*Mo*(((L**2)-(A**2))**1.5)/(27*E*L*MoI)
                print('Deflection:',deflection)
            else:
                deflection = (np.sqrt(3))*Mo*(((L**2)-(C**2))**1.5)/(27*E*L*MoI)
                print('Deflection:',deflection)
                














    

