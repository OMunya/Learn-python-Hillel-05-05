# Task 1

from math import pi, radians  # импортируем модуль math(число Пи и функцию тригонометрии radians)

digit = float(input("Вы вводите значение в градусах: "))  # значение введенное с клавиатуры пользователем в градусах
temperature = digit * pi / 180  # присваиваем имя для новой переменной

# 2 способ решения задачи через функцию radians

temperature1 = radians(digit)

# используем функцию округления round(х, n), где х - это temperature, а n - число округления после запятой

print(round(temperature, 5))  # округлям число до пяти знаков после запятой
print(round(temperature1, 5))

# Task 2

last_digit = float(input("Введите показатели предыдущего месяца: "))  # предыдущие показатели
present_digit = float(input("Введите показатели текущего месяца: "))  # нынешние показатели
tarif_digit = float(input("Введите показатель тарифа: "))  # тариф

how_need_to_pay = (present_digit - last_digit) * tarif_digit  # присваиваем имя для новой переменной

print(round(how_need_to_pay, 2))  # округлям число до двух знаков после запятой

# Task 3

size_get = float(input("Ввиде размер дохода: "))  # доход
size_percent = float(input("Введите размер налога: "))  # налог

how_much_need_to_pay_podatok = size_get / 100 * size_percent  # сколько нужно заплатить налога

clear_we_get = size_get - (size_get / 100 * size_percent)  # чистый налог

print(round(how_much_need_to_pay_podatok, 2))  # округлям число до двух знаков после запятой
print(round(clear_we_get, 2))  # округлям число до двух знаков после запятой

# Task 4
fuel_consumption = float(input("Введите показатель расхода топлива на 100км вашего автомобиля: "))
present_price = float(input("Введите цену за 1л топлива: "))  # цена за 1 л на сегодня
fuel_distance = float(input("Введите растояние: "))  # Сколько килломентров нужно проехать

fuel_for_some_distance = fuel_consumption / 100 * fuel_distance  # сколько машина потратит литров
how_we_must_spend = fuel_consumption / 100 * fuel_distance * present_price  # расходы

print(round(how_we_must_spend, 2))  # округлям число до двух знаков после запятой

