# Метод штрафов
import math

# Инициализация глобальной переменной
rk = 0.1

# Функция штрафа
def penalty_function(x1, x2):
    return (x1 + x2 - 1)

# Корректированная функция штрафа
def corrected_penalty_function(x1, x2):
    return (x1 + x2 - 1) if (x1 + x2 - 1) > 0 else 0

# Вспомогательная функция
def auxiliary_function(x1, x2):
    return (rk / 2.0) * (penalty_function(x1, x2)**2 + corrected_penalty_function(x1, x2)**2)

# Главная функция
def function(x1, x2):
    return (5 * pow(x1, 2) + pow(x2, 2) - x1 * x2 + x1 + auxiliary_function(x1, x2))

# Частная производная функции 1
def partial_derivative_function1(x1, x2):
    if auxiliary_function(x1, x2) > 0:
        return (10 * x1 - x2 + 2 * (x1 + x2 - 1))
    else:
        return (10 * x1 - x2 + 1 * (x1 + x2 - 1))

# Частная производная функции 2
def partial_derivative_function2(x1, x2):
    if auxiliary_function(x1, x2) > 0:
        return (x2 - x1 + 2 * (x1 + x2 - 1))
    else:
        return (x2 - x1 + 1 * (x1 + x2 - 1))

# Функция Fi
def fi_function(tk, xk, grad):
    return function(xk[0] - (tk * grad[0]), xk[1] - (tk * grad[1]))

# Функция дихотомии
def dihotomy_func(xk, grad):
    epsilon = 0.0002
    L = 0.0005
    a0 = -100
    b0 = 100
    check = float('inf')
    while check >= L:
        y = ((a0 + b0) - epsilon) / 2
        z = ((a0 + b0) + epsilon) / 2
        if fi_function(y, xk, grad) <= fi_function(z, xk, grad):
            b0 = z
        else:
            a0 = y
        check = abs(b0 - a0)
    return((b0 + a0) / 2)

# Функция градиентного спуска
def gradient_descent(current_point):
    epsilon1 = 0.1
    epsilon2 = 0.15
    previous_point = current_point
    m = 100
    i = 0
    while True:
        grad = (partial_derivative_function1(current_point[0], current_point[1]), partial_derivative_function2(current_point[0], current_point[1]))
        if math.sqrt(grad[0]**2 + grad[1]**2) < epsilon1:
            print(f"Промежуточная точка вспомогательного метода:({current_point[0]};{current_point[1]})!")
            return (current_point[0], current_point[1])
        if i >= m:
            print(f"Промежуточная точка вспомогательного метода:({current_point[0]};{current_point[1]})!")
            break
        tk = dihotomy_func(current_point, grad)
        xk = (current_point[0] - (tk * grad[0]), current_point[1] - (tk * grad[1]))
        if (math.sqrt((xk[0] - current_point[0])**2 + (xk[1] - current_point[1])**2) < epsilon2
            and
            math.sqrt((current_point[0] - previous_point[0])**2 + (current_point[1] - previous_point[1])**2) < epsilon2
            and
            function(xk[0], xk[1]) - function(current_point[0], current_point[1]) < epsilon1
            and
            function(current_point[0], current_point[1]) - function(previous_point[0], previous_point[1]) < epsilon1):
            print(f"Промежуточная точка вспомогательного метода:({xk[0]};{xk[1]})!")
            return (xk[0], xk[1])
        else:
            previous_point = current_point
            current_point = xk
            i += 1

def penalty_method():
    global rk
    xk = (1.0, 2.0)
    C = 1.5
    epsilon = 0.1
    while True:
        xk = gradient_descent(xk)
        if auxiliary_function(xk[0], xk[1]) <= epsilon:
            print(f"Искомая точка:({xk[0]};{xk[1]})!")
            break
        else:
            rk *= C

def main():
    penalty_method()

if __name__ == "__main__":
    main()
