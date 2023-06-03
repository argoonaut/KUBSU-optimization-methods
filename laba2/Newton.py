import numpy as np

# Определение функции, градиента и гессиана
def function(x):
    return 5 * x[0] ** 2 + x[1] ** 2 + x[0] * x[1] + x[0]

def gradientFunction(x):
    return np.array([10 * x[0] + x[1] + 1, 2 * x[1] + x[0]])

def hessianFunction(x):
    return np.array([[10, 1], [1, 2]])

# Начальная точка
x0 = np.array([1.5, 1.0])

# Параметры алгоритма
M = 10
epsilonOne = 0.1
epsilonTwo = 0.15

# Метод Ньютона
def newton_method(x0, gradientFunction, hessianFunction, M, epsilonOne, epsilonTwo):
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

        if k >= M:
            print(f"Шаг 5[{k}]: Количество итераций превышенно {k} > {M}")
            return x
        print(f"Шаг 5[{k}]: {k} < {M}")

        # Вычисление гессиана
        hessian = hessianFunction(x)
        print(f"Шаг 6[{k}]: Вычисляем матрицу H(x[{k}]) = {hessian}")

        # Вычисление обратного гессиана
        hessian_inv = np.linalg.inv(hessian)
        print(f"Шаг 7[{k}]: Вычисляем обратную матрицу H(x[{k}]), H^-1(x[{k}]) = {hessian_inv}")


        # Проверка положительной определенности обратного гессиана и определение направления поиска
        if np.all(hessian_inv > 0):
            d_k = -np.dot(hessian_inv, gradient)
            print(f"Шаг 8[{k}]: H^-1(x[{k}]) > 0, d_k = {d_k}")
        else:
            d_k = -gradient
            print(f"Шаг 8[{k}]: H^-1(x[{k}]) <= 0, d_k = {d_k}")

        # Шаг поиска
        t_k = 1 # в методичке t_k можно было взять за 1
        x_next = x + t_k * d_k
        print(f"Шаг 9[{k}]: Вычисляем x[k+1] = x[k] + d_k, x[{k+1}] = {x_next}")

        total = 0
        # Критерии остановки
        if np.linalg.norm(x_next - x) < epsilonTwo and np.abs(function(x_next) - function(x)) < epsilonTwo and total == 2:
            total += 1
            print(f"Шаг 10[{k}]: Критерий остановки по разности аргументов и значений функции выполнен, x = {x_next}")
            return x_next
        print(f"Шаг 10[{k}]: Условия ||x[k+1] - x[k]|| = {np.linalg.norm(x_next - x)} > {epsilonTwo} or |f(x[k+1]) - f(x[k])| = {np.abs(function(x_next) - function(x))} > {epsilonTwo}  не выполненны")
        print("----------------------------------------------------------------")
        x = x_next
    return x

x_star = newton_method(x0, gradientFunction, hessianFunction, M, epsilonOne, epsilonTwo)
print(x_star)
