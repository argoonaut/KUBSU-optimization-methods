def f(x):
    return 2*x * x + 2 * x + 7/2  # put your function here


a = -3  # start (a_0)
b = 7  # end (b_0)
l = 0.2  # можно сказать что это шаг на заданом отрезке локализации в заданой точке. те +-0.2 от этой точки
eps = 0.5  # точность
n = 100  # limit


def dichotomy(a, b, eps, l, n):
    a_n = a
    b_n = b
    k = -1
    while b_n - a_n > eps or n < 100:
        k += 1
        x_n = (a_n + b_n - l) / 2.0
        y_n = (a_n + b_n + l) / 2.0
        print("Step", k)
        print("y =", x_n, ",z =", y_n)
        if f(x_n) < f(y_n):
            b_n = y_n
            print(f(x_n), "<", f(y_n))
        else:
            a_n = x_n
            print(f(x_n), ">=", f(y_n))
        print("L =[", a_n, ";", b_n, "] and", "|L| = ", abs(a_n-b_n))
    print("\nAnswer:", (a_n + b_n) / 2)
    print("k =", k, ", N =", 2 * (k + 1))


dichotomy(a, b, eps, l, n)
