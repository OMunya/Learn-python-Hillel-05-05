sum = 0
total = 0

while True:
    text = input("Введіть число або sum будь-ласка!")
    if text == "sum":
        sum += total
        print(sum)
        break
    try:
        interger = float(text)
        total += interger

    except ValueError:
        print("Введіть число або sum будь-ласка!")