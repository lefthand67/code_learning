def longest_word_in_file():
    from string import punctuation
    file_name = input()
    fhand = open(file_name, 'r', encoding='utf-8')
    lst = list()
    longest_word = None
    for line in fhand:
        words = line.split()
        for word in words:
            for symbol in punctuation:
                if symbol in word:
                    word = word.rstrip(symbol)
            if longest_word is None or len(word)>len(longest_word):
                longest_word = word
    fhand.close()
    return longest_word