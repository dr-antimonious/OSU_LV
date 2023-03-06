# Zad 1.4.4

words = dict()
file = open('song.txt')

for line in file:
    line = line.rstrip().lower().split()
    for word in line:
        word = word.strip().strip(',')
        if words.keys().__contains__(word):
            words[word] += 1
        else:
            words[word] = 1
file.close()

unique = list(filter(lambda x: words[x] == 1, words))
print('Kolicina jedinstvenih rijeci: ', len(unique))
print(unique)
