# dfile = input('Enter the default file name to make your life easier: ')  # activate for a script

def host_names():

    """
    Host names extraction function
    extracts the host names from the emails in a mailbox doc (VR).

    >>> Output example:

    Enter the file name (press Enter to open the default file):
    Opened by default: _mbox-short.txt
    @hostnames found in: 336 lines of 1909

    HOST LIST of 10 host(s):
    ['uct.ac.za', 'collab.sakaiproject.org', 'nakamura.uits.iupui.edu', 'localhost', 'media.berkeley.edu']

    FREQUENCY of the host names:
    {'uct.ac.za': 25, 'collab.sakaiproject.org': 162, 'nakamura.uits.iupui.edu': 27, 'localhost': 27}

    """

    dfile = '_mbox-short.txt'  # a file that be opened by default (Enter button), deactivate when using as script

    fname = input('Enter the file name (press Enter to open the default file): ')
    if len(fname) < 1:
        fname = dfile
        print('Opened by default:', dfile)
    fhand = open(fname, 'r', encoding='utf-8')

    # Definitions
    line_number = 0   # number of the line in the doc
    count = 0         # number of the line with '@'
    long_list = []    # list of all host names in the lines with '@'
    host_list = []    # list of the unique host names extracted from the long_list
    host_count = {}   # frequency of the host names in the long_list

    # First we need to find the '@' and ' ' positions to extract the host names between them.
    for line in fhand:
        line_number = line_number + 1
        if '@' not in line:                 # we skip lines without '@'
            continue
        elif '@' in line:
            atpos = line.find('@')          # finding the '@' position
            sppos = line.find(' ', atpos)   # finding the ' ' position
            host = line[atpos + 1: sppos]     # extracting the host name
            host = host.rstrip('>')         # cleaning the host name out of the additional symbols
            host = host.rstrip('>;')
            host = host.rstrip(';')
            host = host.rstrip(')')
            count = count + 1
            long_list.append(host)          # appending the found host names into the long_list
            if host not in host_list:       # appending the unique host names in the host_list
                host_list.append(host)
    #         print('Line {}: {}'.format(line_number, host))

    print('@hostnames found in: {} lines of {}'.format(count, line_number))
    print('\nHOST LIST of {} host(s):\n{}'.format(len(host_list), host_list))

    # Second, we count the frequency of the previously extracted host names.
    for name in long_list:
        host_count[name] = host_count.get(name, 0) + 1

    return '\nFREQUENCY of the host names:\n{}'.format(host_count)
    # print(long_list)
