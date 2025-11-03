'''Bisection Method'''

'''Taking Function as User Input'''
f_x=input('f(x)=')

''' Defining the function f(x)'''
def f(x):
    return eval(f_x)

'''Taking Guesses for x1 and x2 as User Input'''
x1,x2 = map(float,input("Enter Your Guess as x1,x2: ").split(','))

'''Applying Bisection Method Loop'''
if f(x1)*f(x2)>0:
    print(f'The Function {f_x} has No Roots B/W {x1} & {x2}')
else:
    x=(x1+x2)/2                                         #Initial midpoint
    I_C=0                                               #Itration Count
    while abs(f(x))>1e-6:                               #Tolerance of 1e-6
        I_C+=1
        if f(x)*f(x1)>0:
            x1=x
        elif f(x)*f(x1)<0:
            x2=x
        else:
            break
        x=(x1+x2)/2
    
    '''Print Result with Round Off to 6 decimal places'''
    print (f'The Root of Function {f_x} is {round(x,6)}\nNumber of Iterations: {I_C}') 