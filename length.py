def length_check(word):
    length_word = {}
    for letter in word:
        if letter in length_word:
            length_word[letter] += 1
        else:
            length_word[letter] = 1
    return length_word
print(length_check('abrakadabra'))