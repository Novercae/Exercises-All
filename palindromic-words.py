"""
look for words that can be rearranged and be palindromes.
procure por palavras que podem ser rearranjado e ser palindromas.
"""

text = ['ciicv', 'baba', 'xyz', 'casa', 'anilina', 'bbbbaabbbbaa']


def pali_hashtable(word):
    letters = {}
    odd = 0
    for l in word:
        if l in letters:
            letters[l] += 1
        else:
            letters[l] = 1

    for i in letters.values():
        if i%2 == 1:
            odd += 1
        if odd >= 2:
            return False
    return True


for word in text:
    print(pali_hashtable(word))
