counter = 0  # сумма чисел будет записываться в переменную сума
total = 0  # в переменную будут записываться значения, которые мы преобразовуем в try

while True:
    text = input("Введіть число або sum будь-ласка!")
    if text == "sum":
        sum += total
        print(sum)
        break
    try:
        interger = float(text)  # пытаемся число преобразовать в вещественное
        total += interger

    except ValueError:
        print("Введіть число або sum будь-ласка!")