# problem 1
with open("words.txt") as fin:
    for word in fin:
        if len(word)>20:
            print(word)
            
# problem 2
with open("words.txt") as fin:
    with open('long_words.txt', 'w') as fout:
        for word in fin:
            if len(word)>20:
                print(word, file=fout)

# problem 3
d = {}
with open("words.txt") as fin:
    for word in fin:
        l = len(word)
        if l in d:
            d[l] += 1
        else:
            d[l] = 1

# problem 4
import pickle
d = {}
with open("words.txt") as fin:
    for word in fin:
        l = len(word)
        if l in d:
            d[l] += 1
        else:
            d[l] = 1
with open('counts.pickle', 'wb') as fout:
    pickle.dump(d,fout)

