import numpy as np
import matplotlib.pyplot as plt

f_x = input("Enter the function for Integration Methods: ")

def f(x):
    return eval(f_x)

def trapezoidal(a, b, n):
    h = (b - a) / n
    L = f(a) + f(b)
    for i in range(1, n):
        L += 2 * f(a + i * h)
    return h / 2 * L

def simpson(a, b, n):
    h = (b - a) / n
    L = f(a) + f(b)
    for i in range(1, n):
        L += 4 * f(a + i * h) if i % 2 == 1 else 2 * f(a + i * h)
    return L * (h / 3)

def simpson3(a, b, n):
    h = (b - a) / n
    L = f(a) + f(b)
    for i in range(1, n):
        L += 3 * f(a + i * h) if i % 3 != 0 else 2 * f(a + i * h)
    return (3 * h / 8) * L

F = np.linspace(1, 100, 100)
Et, Es, E38 = [], [], []
true_value = 0.25  # Known integral value for f(x) = x^3 from 0 to 1

for n in F:
    Et.append(abs(true_value - trapezoidal(0, 1, int(n))))
    Es.append(abs(true_value - simpson(0, 1, int(n))))
    E38.append(abs(true_value - simpson3(0, 1, int(n))))

plt.plot(F, Et, label="Trapezoidal")
plt.plot(F, Es, label="Simpson 1/3")
plt.plot(F, E38, label="Simpson 3/8")
plt.xlabel("Number of Slices")
plt.ylabel("Error")
plt.title("Error Comparison of Integration Methods")
plt.legend()
plt.show()

print(f"Trapezoidal result: {trapezoidal(-1, 1, 10000)}")
print(f"Simpson 1/3 result: {simpson(0, 1, 100)}")
print(f"Simpson 3/8 result: {simpson3(0, 1, 100000)}")