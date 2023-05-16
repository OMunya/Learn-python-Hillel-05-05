word = input("Write your word: ")
word = word.lower()
print(word)
word2 = word[::-1]
if word == word2:
    print("Yes")
else:
    print("No")

