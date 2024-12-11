import math

x = float(input("Введите длину первого катета: "))
y = float(input("Введите длину второго катета: "))
print("Гипотенуза: ", math.sqrt(x**2 + y**2))
print("Площадь треугольника", (x*y) / 2)
