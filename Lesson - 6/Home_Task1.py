text = input()  # вводи любое слово, в нашем случае "Аби ріці риба"
punctuation = '.,!\n\t"'
flg = False  #
raw_words = text.split()  # делаю со строки список

proces_word = list()  # список в который будет добавлено новые отредактированные слова

for word in raw_words:
    word = word.lower()
    word = word.strip(punctuation)
    proces_word.append(word)

    polindrom = "".join(proces_word)  # обьеденяю слова и чтобы проверить его на полиндром

    if polindrom == polindrom[:: -1]:
        flg = True  #

if flg == True:
    print(f"\"{text}\" which you write is 'polindrom'")
else:
    if flg == False:
        print(f"\"{text}\" is not 'polindrom'")