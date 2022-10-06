
# problem 1
Eng2Ita = {}
while True:
    word = input('insert English word: ')
    if word != 'done!':
        parola = input(f'insert Italian translation of {word}: ')
        Eng2Ita[word] = parola
    else:
        break

# problem 2
Eng2Ita = {}
Ita2Eng = {}
while True:
    word = input('insert English word: ')
    if word != 'done!':
        parola = input(f'insert Italian translation of {word}: ')
        Eng2Ita[word] = parola
        Ita2Eng[parola] = word
    else:
        break
while True:
    word = input('insert a word to be translated: ')
    if word in Eng2Ita:
        print(f'the Italian translation of {word} is {Eng2Ita[word]}')
    elif word in Ita2Eng:
        print(f'the English translation of {word} is {Ita2Eng[word]}')
    else:
        print(f'error: the word {word} is not in the dictionary')
        break
        
# problem 3
s = input('insert a string: ')
s = s.lower()
d = {}
for c in s:
    if c in d:
        d[c] = d[c]+1
    else:
        d[c] = 1
for c in 'abcdefghijklmnopqrstuvwxyz':
    if c in d:
        print(c, d[c])

