
# Цикл while будет повторяться бесконесное колличество раз при помощи True:

while True:
    question = input("Write you text for boat, please: ")
    if "Привіт".lower() in question or "Хай".lower() in question or "Доброго дня".lower() in question:
        print("Доброго вечора, я бот з України!")
    elif "Як справи?".lower() in question or "Що робиш?".lower() in question or "Чим займаєшся?".lower() in question:
        print("Вчусь програмувати на Python!")
    elif "Фільм".lower() in question or "Серіал".lower() in question or "Кінотеатр".lower() in question:
        print("Соррі що втручуюсь, не знаю про що йдеться мова, але подивіться серіал 'Swagger', він просто бомба!")
    elif "Бувай".lower() in question or "Надобраніч".lower() in question or "Гудбай".lower() in question or "До зустрічі".lower() in question:
        print("Побачимось у мережі, I'll be back.")
        break  # выход из цикла

    else:
        print("Дуже цікаво, але, нажаль, нічого не зрозуміло :(")


