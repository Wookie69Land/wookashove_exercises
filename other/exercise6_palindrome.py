def check_palindrome(string):
    word = string.lower()
    for char in " ?.,!/;:'":
        word = word.replace(char, "")
    rev_word = word[::-1]
    message = f'{string} is palindrome: '
    if word == rev_word:
        palindrome = True
    else:
        palindrome = False
    return f'{message}{palindrome}'


if __name__ == '__main__':
    word_1 = "baba"
    print(check_palindrome(word_1))

    word_2 = "Manam"
    print(check_palindrome(word_2))

    sentence_1 = "Jeż leje lwa, paw leje lżej."
    print(check_palindrome(sentence_1))
