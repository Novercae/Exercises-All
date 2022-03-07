# look for words that can be rearranged and be palindromes.
# procure por palavras que podem ser rearranjado e ser palindromas.

text = ['ciicv', 'baba', 'xyz', 'casa', 'anilina', 'bbbbaabbbbaa']


def pali_hashtable(palavra):
    letras = {}
    impares = 0
    for l in palavra:
        if l in letras:
            letras[l] += 1
        else:
            letras[l] = 1

    for i in letras.values():
        if i%2 == 1:
            impares += 1
        if impares >= 2:
            return False
    return True


for palavra in text:
    print(pali_hashtable(palavra))
