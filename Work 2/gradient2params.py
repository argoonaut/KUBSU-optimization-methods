import math
import numpy as np
from sympy import symbols, diff, lambdify, solve


def func():
    # return x**2 + 8 * y**2 - x*y + x
    return 2*x**2 + x*y + y**2


x_0, y_0 = 0.5, 1
# x_0, y_0 = 1.5, 0.1
e_1 = 0.1
e_2 = 0.15
M = 10
flag = True

x, y = symbols('x, y')
f = lambdify([x, y], func())
param = [x, y]
diffs = []
for i in param:
    diff_one = diff(func(), i)
    print("Derivative by", i , ":", diff_one)
    diffs.append(lambdify(param, diff_one))  # пишем в массив как лямбду (чтобы передать параметры)

x_k, y_k = x_0, y_0
k = 0
while flag:
    print()
    print("k =", k)
    # шаг 3
    diff_fx_k = []
    module_diff_fx_k = 0
    for i in diffs:
        diff_fx_k.append(i(x_k, y_k))
        module_diff_fx_k += diff_fx_k[-1] ** 2  # сразу считаем модуль для 4 шага
    print("3) f(x_k)'=", diff_fx_k)
    print("4) Norm f(x_k)'=", math.sqrt((module_diff_fx_k)), "and e_1 =", e_1)
    if math.sqrt(module_diff_fx_k) < e_1 or k >= M:
        flag = False
        print("Complete!")
        continue
    print("5) k =", k, ", M =", M)
    fi_x_k = diff(f(-x * diff_fx_k[0] + x_k, y_k - diff_fx_k[1] * x), x)
    print("6) fi(x_k) = ", fi_x_k)
    t_k = solve(fi_x_k, x)
    print("6) t_k = ", t_k[0])
    x_next = np.array([x_k, y_k] - t_k[0] * np.array(diff_fx_k))
    print("7) x_k+1 =", x_next)
    x_diff = np.array(x_next) - np.array([x_k, y_k])
    print("8) x_k+1 - x_k =", x_diff)
    module_x = 0
    for i in x_diff:
        module_x += i ** 2
    print("8) |x_k+1 - x_k| =", math.sqrt(module_x), "and e_2 =", e_2)
    if math.sqrt(module_x) < e_2:
        fx_k0 = f(x_next[0], x_next[1]) - f(x_k,y_k)
        # print(math.abs(fx_k0))
        if math.fabs(fx_k0) <e_2: print("!! Next step is the last !!")
    x_k = x_next[0]
    y_k = x_next[1]
    k += 1

print("Answer is:", x_k, y_k)
print("Function", f(x_k, y_k))