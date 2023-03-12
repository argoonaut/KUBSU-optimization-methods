import math
import numpy as np
from sympy import symbols, diff, lambdify, solve


def func():
    return x**2 + 8 * y**2 - x*y + x
    # return 2*x**2 + x*y + y**2


def main_minor(arr, i):
    return arr[np.array(list(range(i+1)))[:,np.newaxis],
               np.array(list(range(i+1)))]


# x_0, y_0 = 0.5, 1
x_0, y_0 = 1.5, 0.1
e_1 = 0.1
e_2 = 0.15
M = 10
flag = True

x, y = symbols('x, y')
f = lambdify([x, y], func())
param = [x, y]
diffs = []
first_deriv = []
for i in param:
    diff_one = diff(func(), i)
    first_deriv.append(diff_one)
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
    hesse = []
    for der in first_deriv:
        one_hesse = []
        for p in param:
             temp = lambdify([x, y], diff(der, p))
             one_hesse.append(temp(x_k, y_k))
        hesse.append(one_hesse)
    print("6) H(x_k) = ")
    print(hesse)
    inv_hesse = np.linalg.inv(hesse)
    print("7) H^-1(x_k) =")
    print(np.linalg.inv(hesse))
    d_k, x_next, y_next = 0, 0, 0
    print("8) main minor_1 = ", main_minor(inv_hesse, 0), ", main minor_2 = ", np.linalg.det(main_minor(inv_hesse, 1)))
    if main_minor(inv_hesse, 0) > 0 and np.linalg.det(main_minor(inv_hesse, 1)) > 0:
        print("9) d_k = ")
        print(-inv_hesse, "*", diff_fx_k, "^(T)")
        d_k = -inv_hesse.dot(diff_fx_k)
        print(" = ", d_k)
        x_next = round(x_k + d_k[0], 7)
        y_next = round(y_k + d_k[1], 7)
    else:
        d_k = -diff_fx_k
        # ????
        x_next = round(x_k + d_k[0], 7)
        y_next = round(y_k + d_k[1], 7)
    print("10) x_k+1 =", x_next, ", y_k+1 =", y_next)

    x_diff = np.array(x_next) - np.array([x_k, y_k])
    module_x = 0
    for i in x_diff:
        module_x += i ** 2
    print("11) |x_k+1 - x_k| =", math.sqrt(module_x), "and e_2 =", e_2)
    if math.sqrt(module_x) < e_2:
        fx_k0 = f(x_next[0], x_next[1]) - f(x_k, y_k)
        print(math.abs(fx_k0), " and e_2 =", e_2)
        if math.fabs(fx_k0) < e_2:
            print("!! Next step is the last !!")
    x_k = x_next
    y_k = y_next
    k += 1
print()
print("Answer is:", x_k, y_k)
print("Function", f(x_k, y_k))
print("main minor_1 = ", main_minor(inv_hesse, 0), ", main minor_2 = ", np.linalg.det(main_minor(inv_hesse, 1)))
if main_minor(inv_hesse, 0) > 0 and np.linalg.det(main_minor(inv_hesse, 1)) > 0:
    print("This is local min (>0)")
else:
    print("This is local min")
print("k =", k)
print("Hesse: ")
print(hesse)
print("Inv hesse: ")
print(inv_hesse)
