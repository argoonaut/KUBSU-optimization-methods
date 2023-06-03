# Метод множителей (Лагранжа)
import math

rk = 0.1
u = 0.001
l = 0.001

def penalty_function(x1, x2):
    return (x1 + x2 - 1)

def function_helper(x1, x2):
    global u, rk
    answer = max(u + rk * penalty_function(x1, x2), 0)
    answer = (answer ** 2) - (u ** 2)
    answer *= (1 / (2 * rk))
    return answer

def p_function(x1, x2):
    global rk
    return (rk / 2) * (penalty_function(x1, x2) ** 2) + function_helper(x1, x2)

def function(x1, x2):
    global l, rk
    return (5 * x1 * x1 + x2 * x2 - x1 * x2 + x1 + l * penalty_function(x1, x2)
            + (rk / 2) * (penalty_function(x1, x2) ** 2) +
            function_helper(x1, x2))

def partial_derivative_function1(x1, x2):
    global u, rk, l
    if ((u + rk * penalty_function(x1, x2)) > 0):
        return (10 * x1 - x2 + 1 + l + rk * penalty_function(x1, x2) +
                penalty_function(x1, x2))
    else:
        return (10 * x1 - x2 + 1 + l + rk * penalty_function(x1, x2))

def partial_derivative_function2(x1, x2):
    global u, rk, l
    if ((u + rk * penalty_function(x1, x2)) > 0):
        return (2 * x2 - x1 + l + rk * penalty_function(x1, x2) +
                penalty_function(x1, x2))
    else:
        return (2 * x2 - x1 + l + rk * penalty_function(x1, x2))

def fi_function(tk, xk, grad):
    return function(xk[0] - (tk * grad[0]), xk[1] - (tk * grad[1]))

def dihotomy_func(xk, grad):
    Epsilon = 0.0002
    L = 0.0005
    a0 = -100
    b0 = 100
    check = float('inf')
    while (check >= L):
        y = ((a0 + b0) - Epsilon) / 2
        z = ((a0 + b0) + Epsilon) / 2
        if (fi_function(y, xk, grad) <= fi_function(z, xk, grad)):
            b0 = z
        else:
            a0 = y
        check = abs(b0 - a0)
    return((b0 + a0) / 2)

def gradient_descent(current_point):
    global u, rk
    Epsilon1 = 0.1
    Epsilon2 = 0.15
    m = 100
    i = 0
    previous_point = current_point

    while True:
        grad = (partial_derivative_function1(current_point[0], current_point[1]),
                partial_derivative_function2(current_point[0], current_point[1]))
        if math.sqrt((grad[0] ** 2) + (grad[1] ** 2)) < Epsilon1:
            print("Промежуточная точка вспомогательного метода:({}, {})!".format(current_point[0], current_point[1]))
            return current_point
        if i >= m:
            print("Промежуточная точка вспомогательного метода:({}, {})!".format(current_point[0], current_point[1]))
            break
        tk = dihotomy_func(current_point, grad)
        xk = (current_point[0] - (tk * grad[0]), current_point[1] - (tk * grad[1]))
        if (math.sqrt((xk[0] - current_point[0]) ** 2 + (xk[1] - current_point[1]) ** 2) < Epsilon2
                and
                math.sqrt((current_point[0] - previous_point[0]) ** 2 + (current_point[1] - previous_point[1]) ** 2) < Epsilon2
                and
                function(xk[0], xk[1]) - function(current_point[0], current_point[1]) < Epsilon1
                and
                function(current_point[0], current_point[1]) - function(previous_point[0], previous_point[1]) < Epsilon1):
            print("Промежуточная точка вспомогательного метода:({}, {})!".format(xk[0], xk[1]))
            return xk
        else:
            previous_point = current_point
            current_point = xk
            i += 1

def lagranj_method():
    global rk, l, u
    xk = (1.0, 2.0)
    C = 1.5
    Epsilon = 0.1
    while True:
        xk = gradient_descent(xk)
        if p_function(xk[0], xk[1]) <= Epsilon:
            print("Искомая точка:({}, {})!".format(xk[0], xk[1]))
            break
        else:
            rk *= C
            l = l + rk * penalty_function(xk[0], xk[1])
            u = max(u + rk * penalty_function(xk[0], xk[1]), 0)

if __name__ == "__main__":
    lagranj_method()
