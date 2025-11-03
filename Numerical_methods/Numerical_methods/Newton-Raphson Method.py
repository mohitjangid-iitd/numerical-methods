'''Newton-Raphson Method'''

import sympy as sp

'''Symbolizing x as a Variables'''
x_sym = sp.symbols('x')

'''Taking Function as User Input'''
f_x_I=input('f(x)=')

'''Creating Funs. f(x) & f'(x)'''
f_x = sp.sympify(f_x_I)
f_p_x = sp.diff(f_x ,x_sym)

'''Taking Initial Guess as User Input'''
x=float(input('Initial guess x0 = '))

'''f(x0)'''
fx = f_x.subs(x_sym, x)

I_C = 0                                         #Itration Count

while abs(fx)>1e-6:
    fx = f_x.subs(x_sym, x)
    fpx = f_p_x.subs(x_sym, x)
    x = x - fx / fpx
    I_C += 1
print (f'The Root of Function {f_x} is {round(x,6)}\nNumber of Iterations: {I_C}')