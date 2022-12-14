# dfile = input('Enter the default file name to make your life easier: ')  # activate for a script

def word_count():
    """
    The Word Count Function
    counts the words in the document with disregard to the case of the letters in words and
    puts them into a dictionary.
    
    The function ignores the strings that can be converted to floats and integers. 
    
    NOTE! You can reassign the default file in prompt by activating the line above the function code
    and deactivating the first line of the function.
    
    Output example:
    
    Enter the file name (press Enter to open the default file):
    Opened by default: _mbox-short.txt

    Length: 1063
    Counts: {'from': 326, 'stephen.marquard@uct.ac.za': 8, 'sat': 12, 'jan': 352, '09:14:16': 4, 'return-path': 27}
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
            try:  # the operation filters ints and floats
                word = float(word)
                continue
            except ValueError:  # we get only non-ints and non-floats in counts list
                if len(word) > 0:
                    counts[word] = counts.get(word, 0) + 1
    return '\nThe number of words: {}\nCounts:\n{}.\nDone'.format(len(counts), counts)
