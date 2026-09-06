import matplotlib.pyplot as plt

# defining function to accept the equation, 
#then open two lists to hold the values, ans also add spacing between the 
#points
def plot_function(fun_str,domain,ns) :
    
    xmin, xmax = domain
    xs=[]
    ys=[]
   
    for i in range(ns) :
       x=xmin+i
       xs.append(x)
       
    for x in xs :
        y=eval(fun_str)
        ys.append(y)
    
    return xs,ys

#calling the functions and storing the data
fun_str=input('Enter a function with x: ')
ns=int(input('Enter a number of saamples: '))
xmin=float(input('Enter xmin: '))
xmax=float(input('Enter xmax: '))
domain=xmin,xmax

print("X's" "                  " "Y's")
print("-" *40)
xs,ys=plot_function(fun_str,domain,ns)
print(xs,                       ys)

#graphing function

plt.plot(xs, 0, marker='o', color='red')
plt.plot(ys, 0, marker='o', color='red')
plt.axhline(0, color='black')
plt.grid()
plt.show()