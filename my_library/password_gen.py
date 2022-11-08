# Strong password generator
def password_gen(number_of_symbols):
    """
    The program generates strong passwords of any size starting from 12 symbols.
    If the number is less than four (the number of required symbol types) the program will not
    be able to generate a password.
    """
    
    # required symbols
    numbers = '1234567890'
    lletters = 'abcdefghijklmnopqrstuvwxyz'
    uletters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    signs = '!@#$%^&*()-+~'
    
    # generating the password
    import random
    password = ''
    
    if number_of_symbols < 12:
        print('Choose number starting from 12.')
    
    else: 
        while len(password) < number_of_symbols:
            password = password + random.choice(numbers + lletters + uletters + signs)
#         return password
        
        # check group for every type of required symbols
        numbers_check = 0
        lletters_check = 0
        uletters_check = 0
        signs_check = 0

        # check test of the password
        for symbol in password:        
            if symbol in numbers: numbers_check = 1      
            elif symbol in lletters: lletters_check = 1        
            elif symbol in uletters: uletters_check = 1        
            elif symbol in signs: signs_check = 1

        # results of check test
        # if the password lacks at least one of symbol types' elements it repeats the loop until the password gets the check
        while ((numbers_check == 0) or 
               (lletters_check == 0) or 
               (uletters_check == 0) or 
               (signs_check == 0)):
#             print('weak')
            return password_gen(number_of_symbols)
        else:
            print('Your password:')
            print(password)

