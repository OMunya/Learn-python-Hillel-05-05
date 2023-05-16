# Вариант исполнения кода через метод .replace()
text = input("Write you text please: ")

# 2 Програма переводить строку в нижній регістр
text = text.lower()

# 3 Заміняємо символи пунктуації: .,-:;?!
text = text.replace(".", "")
text = text.replace(",", "")
text = text.replace("-", "")
text = text.replace(":", "")
text = text.replace(";", "")
text = text.replace("?", "")
text = text.replace("!", "")

# 4 Програма видаляє зайві пробіли\табуляції з правого кінця строки
text = text.rstrip()

# 5 Програма питає користувача яке слово (або словосполучення) він бажає замінити
quetion = input("What do you want to replace? ")
# C++
quetion = quetion.lower()
answer = text.find(quetion)

# 6 Програма повідомляє на якому індексі строки словосполучення присутнє
print(answer)

# 7 Програма питає на яке слово треба замінити
quetion2 = input("With what do you want to replace? ")
# Python
quetion2 = quetion2.lower()

print(text.replace(quetion, quetion2))

