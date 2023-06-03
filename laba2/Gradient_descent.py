import numpy as np


# Определение функции и градиента
def function(x):
    return 5 * x[0] ** 2 + x[1] ** 2 + x[0] * x[1] + x[0]


def gradientFunction(x):
    return np.array([10 * x[0] + x[1] + 1, 2 * x[1] + x[0]])


# Начальная точка
x0 = np.array([1.5, 1.0])

# Параметры алгоритма
M = 10
epsilonOne = 0.1
epsilonTwo = 0.15

def golden_section_search(func, a, b, tol=1e-5):
    gr = (np.sqrt(5) + 1) / 2  # Золотое сечение
    c = b - (b - a) / gr
    d = a + (b - a) / gr
    while abs(c - d) > tol:
        if func(c) < func(d):
            b = d
        else:
            a = c
        c = b - (b - a) / gr
        d = a + (b - a) / gr
    return (b + a) / 2


# Градиентный спуск
def gradient_descent(x0, gradientFunction, M, epsilonOne, epsilonTwo):
    print(f"Шаг 1: x = {x0}; e1 = {epsilonOne}; e2 = {epsilonTwo}; M = {M}; ∇f(xk) = {gradientFunction(x0)}")
    x = x0
    print("Шаг 2: k = 0")
    for k in range(M):

        gradient = gradientFunction(x)
        print(f"Шаг 3[{k}]: ∇f(x[{k}]) = {gradient}")

        # Критерии остановки
        if np.linalg.norm(gradient) < epsilonOne:
            print(f"Шаг 4[{k}]: Критерий остановки по норме градиента выполнен, x = {x}")
            return x
        print(f"Шаг 4[{k}]: ||∇f(x[{k})|| = {np.linalg.norm(gradient)} > {epsilonOne}")

        if k > M:
            print(f"Шаг 5[{k}]: Количество итераций превышенно {k} > {M}")
            return x
        print(f"Шаг 5[{k}]: {k} < {M}")

        # Определение t_k с помощью метода золотого сечения
        func = lambda t: function(x - t * gradient)
        t_k = golden_section_search(func, 0, 1)
        print(f"Шаг 6[{k}]: Вычисляем величину шага tk∗ из условия методом золотого сечения, t_k = {t_k}")

        x_next = x - t_k * gradient
        print(f"Шаг 7[{k}]: Вычисляем xk+1 = {x_next}")
        total = 0
        if np.linalg.norm(x_next - x) < epsilonTwo and abs(function(x_next) - function(x)) < epsilonTwo and total == 2:
            total += 1
            print(f"Шаг 8[{k}]: Условие [{np.linalg.norm(x_next - x)} < {epsilonTwo} и {abs(function(x_next) - function(x))} < {epsilonTwo}] выполненно")
            return x_next

        print(
            f"Шаг 8[{k}]: Условие [{np.linalg.norm(x_next - x)} < {epsilonTwo} и {abs(function(x_next) - function(x))} < {epsilonTwo}]  не выполненно")
        print("----------------------------------------------------------------")
        x = x_next
    return x


x_star = gradient_descent(x0, gradientFunction, M, epsilonOne, epsilonTwo)
print(x_star)
