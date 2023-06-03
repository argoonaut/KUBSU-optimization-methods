def f(x):
    return 2 * x * x + 2 * x + 7 / 2  # put your function here

def fib(n):
    if n in (0, 1):
        return 1
    return fib(n - 1) + fib(n - 2)


a = -3  # start (a_0)
b = 7  # end (b_0)
l = 0.5  # (l) - find +-
eps = 0.2

def fibonacci(a, b, l, eps):
    n = 1
    while fib(n) <= abs(b - a)/l:
        n += 1

    a_n = a
    b_n = b
    y_n = a_n + (fib(n - 2) / fib(n)) * (b_n - a_n)
    z_n = a_n + (fib(n - 1) / fib(n)) * (b_n - a_n)
    k = 0
    while k != n - 3:
        print("Step", k)
        print("y =", y_n,",z =", z_n)
        if f(y_n) > f(z_n):
            print(f(y_n), ">", f(z_n))
            a_n = y_n
            y_n = z_n
            z_n = a_n + (fib(n-k-2)/fib(n-k-1)) * (b_n - a_n)
        else:
            print(f(y_n), "<=", f(z_n))
            b_n = z_n
            z_n = y_n
            y_n = a_n + (fib(n-k-3)/fib(n-k-1)) * (b_n - a_n)
        print("L = [", a_n, ";", b_n, "] and", "|L| =", abs(a_n-b_n))
        k += 1
    y_n = z_n
    z_n = y_n + eps
    if f(y_n) <= f(z_n):
        b_n = z_n
    else:
        a_n = y_n
    print("\nAnswer:", (a_n + b_n) / 2)
    print("k =", k)
    string = ""
    for i in range(n):
        string += str(fib(i)) + ", "
    print(string)


fibonacci(a, b, l, eps)
