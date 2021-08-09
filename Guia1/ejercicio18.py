word = input("Ingresa la palabra :")
i = -1

while i >= (len(word)*-1):
    print (f"{word[i]}")
    i -= 1


for letra in word [::-1]:
    print (letra)


for letra in reversed(word):
    print (letra)