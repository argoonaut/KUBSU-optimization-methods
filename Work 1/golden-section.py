def f(x):
    return 2*x * x + 2 * x + 7/2  # put your function here


a = -3  # start (a_0)
b = 7  # end (b_0)
l = 0.5  # (l) - find +-
n = 100  # limit


def golden_section(a, b, l, n):
    a_n = a
    b_n = b
    k = -1
    while b_n - a_n > l or n < 100:
        k += 1
        y_n = a_n + 0.381966 * (b_n - a_n)
        z_n = a_n + b_n - y_n
        print("Step", k)
        print("y =", y_n, ",z =", z_n)
        if f(y_n) > f(z_n):
            print(f(y_n), ">", f(z_n))
            a_n = y_n
            y_n = z_n
            z_n = a_n + b_n - z_n
        else:
            print(f(y_n), "<=", f(z_n))
            b_n = z_n
            z_n = y_n
            y_n = a_n + b_n - y_n
        print("L = [", a_n, ";", b_n, "] and", "|L| =", abs(a_n-b_n))
    print("\nAnswer:", (a_n + b_n) / 2)
    print("k =", k, ", N =", 2 * (k + 1))


golden_section(a, b, l, n)