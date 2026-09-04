import math
import matplotlib.pyplot as plt

while True :
    a = float(input('Enter a value for A'))
    
    if a == '' :
        break
    
    b = float(input('Enter a value for B'))
    c = float(input('Enter a value for C'))
    
    radicand = b**2-4*a*c
    
    if radicand<0 :
        print('No real solutions')
        break 

    if radicand == 0 :
        x1 =-b+ math.sqrt(radicand)/(2*a)
        print('One solution:', x1)
        plt.plot(x1, 0, marker='o', marker='red')
        plt.axhline(0, color='black')
        plt.grid()
        plt.show()
   
    if radicand > 0 :
        x1 = -b+ math.sqrt(radicand)/(2*a)
        x2 = -b- math.sqrt(radicand)/(2*a)
        print('Two solutions:',x1,x2)
        plt.plot(x1,0,color='red', marker='o')
        plt.plot(x2,0,color='red', marker='o')
        plt.axhline(0, color='black')
        plt.grid()
        plt.show()