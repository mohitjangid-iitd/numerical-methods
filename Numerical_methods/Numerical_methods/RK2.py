import numpy as np

f_xy = input('Function dy/dx = f(x,y)=')
x0,y= map(float,input("Enter Your Guess as x0,y0: ").split(','))
h=float(input('Step size h='))

def f(x,y):
    return eval(f_xy)

x_r=1.1
x=np.arange(x0,x_r,h)

def RK2_step(x,y,h):
    '''2nd order Runge-Kutta numerical method'''
    k1=h*f(x,y)
    k2=h*f(x+h,y+k1)
    return (k1+k2)/2

Y=[y]
for i in x:
    y=y+RK2_step(i,y,h)
    Y.append(y)

print(' x       y')
for i in range(len(x)):
    print(round(x[i],3),'  ',round(Y[i],5))