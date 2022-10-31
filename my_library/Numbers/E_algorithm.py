def E_algorithm(m, n):
    """
    Euclid algorithm
    """
    if type(m) is int and type(n) is int and m > 0 and n > 0:
        initial = m, n
        counts = 1
        if m < n: m, n = n, m
        r = m%n
        while r != 0:
            m, n = n, r
            r = m%n
            counts+=1
        return f'gcd is {n} for {initial} in {counts} step(s)'
    else:
        return 'Choose natural numbers with type of integer'
