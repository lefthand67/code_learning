# dfile = input('Enter the default file name to make your life easier: ')  # activate for a script

def most_freq_word():

    """
    The Most Frequent Word Function
    searches for the most frequent word(s) in the document with disregard to the case of 
    the letters in words. 
    It shows the "Largest count" number (i.e. value in dictionary) and lists all 
    the words (keys) that are complemented to the value.
    
    The function ignores the strings that can be converted to floats and integers. 
    
    NOTE! You can reassign the default file in prompt by activating the line above the function code
    and deactivating the first line of the function.
    
    Output example:
    
    Enter the file name (press Enter to open the default file): 
    Opened by default: _mbox-short.txt

    Largest count: 352
    jan

    Quantity of words: 1
    Most frequent words: ['jan'] <<<
    
    """

    dfile = '_mbox-short.txt'  # a file that be opened by default (Enter button), deactivate when using as script

    fname = input('Enter the file name (press Enter to open the default file): ')
    if len(fname) < 1:
        fname = dfile
        print('Opened by default:', dfile)
    fhand = open(fname, 'r', encoding='utf-8')

    counts = {}
    for line in fhand:
        line = line.rstrip() and line.lower()
        words = line.split()
    #     print('Words:', words)
        for word in words:
            word = word.strip(',')
            word = word.strip('.')
            word = word.strip(';')
            word = word.strip('?')
            word = word.strip('!')
            word = word.strip('?!')
            word = word.strip('"')
            word = word.strip(':')
            word = word.strip('(')
            word = word.strip(')')
            word = word.strip('[')
            word = word.strip(']')
            try:                        # the operation filters ints and floats
                word = float(word)
                continue
            except ValueError:           # we get only non-ints and non-floats in counts list
                if len(word) > 0:
                    counts[word] = counts.get(word, 0) + 1
    # print('\nLength: {}\nCounts: {}'.format(len(counts),counts))

    largest_count = None                # searching for the largest value (i.e. count of the words)
    # print('\nLargest count search:')  # got be activated only with print(count, word)
    for word, count in counts.items():
        if largest_count is None or count > largest_count:
            largest_count = count
    #         print(largest_count, word)
    #     print(count, word)
    print('\nLargest count: {}'.format(largest_count))

    freq_words = []                     # most frequent words' list
    for word, count in counts.items():
        if (count == largest_count) and (word not in freq_words):
            freq_words.append(word)
            # print(word)
    return '\nQuantity of words: {}\nMost frequent words: {}.\nDone'.format(len(freq_words), freq_words)
