import re  # Импортирую библиотеку "re"

# 1 Користувач вводить строку
text = input("Write you text please: ")
# HelLo, mY nAmE iS KyRyLo! I aM PrograMMing on C++) WhAt abOuT yoU? :) пример для прослеживания действий

# 2 Програма переводить строку в нижній регістр
text = text.lower()

# 3 Програма видаляє зі строки такі символи пунктуації: .,-:;?! при помощи sub заменяем найденные символы на новые
reg = r"([.,!?:)]+)"  # формула по которой будет производиться замена
replacement = ""  # переменная, на которую будет происходить замена
new_text = re.sub(reg, replacement, text)

# 4 Програма видаляє зайві пробіли\табуляції з правого кінця строки
new_text = new_text.rstrip()

# 5 Програма питає користувача яке слово (або словосполучення) він бажає замінити
quetion = input("What do you want to replace? ")
# C++
quetion = quetion.lower()
answer = new_text.find(quetion)

# 6 Програма повідомляє на якому індексі строки словосполучення присутнє
print(answer)

# 7 Програма питає на яке слово треба замінити
quetion2 = input("With what do you want to replace? ")
# Python
quetion2 = quetion2.lower()

print(new_text.replace(quetion, quetion2))

