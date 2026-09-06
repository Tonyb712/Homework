
import math
import matplotlib.pyplot as plt

#while value has been added, continue with program
while True :
    a = float(input('Enter a value for A'))
    
    if a == '' :
        break
    
    b = float(input('Enter a value for B'))
    c = float(input('Enter a value for C'))
    
    #performing the mathematical operation to find out whats under the square
    #root
    
    radicand = b**2-4*a*c
    
    #the if statements for the possibility of certain answers
    
    #if  less than 0, close program and print message
    if radicand<0 :
        print('No real solutions')
        break 
#if zero, print one solution and graph
    if radicand == 0 :
        x1 =-b+ math.sqrt(radicand)/(2*a)
        print('One solution:', x1)
        plt.plot(x1, 0, marker='o', color='red')
        plt.axhline(0, color='black')
        plt.grid()
        plt.show()
   #if greater than 0, print two solutions with graph
    if radicand > 0 :
        x1 = -b+ math.sqrt(radicand)/(2*a)
        x2 = -b- math.sqrt(radicand)/(2*a)
        print('Two solutions:',x1,x2)
        plt.plot(x1,0,color='red', marker='o')
        plt.plot(x2,0,color='red', marker='o')
        plt.axhline(0, color='black')
        plt.grid()
        plt.show()
