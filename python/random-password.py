import random, string

def password(length,num=False,strength=True):
    """length of password, num if you want a number,
    and strength (weak,strong,very)"""
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    letter = lower + upper
    dig = string.digits
    punct = string.punctuation
    pwd = ''
    if strength == 'weak':
        if num:
            length -= 2
            for i in range(2):
                pwd += random.choice(dig)
        for i in range(length):
            pwd += random.choice(lower)

    elif strength == 'strong':
        if num:
            length -= 2
            for i in range(2):
                pwd += random.choice(dig)
        for i in range(length):
            pwd += random.choice(letter)

    elif strength == 'very':
        ran = random.randint(2,4)
        if num:
            length -= ran
            for i in range(ran):
                pwd += random.choice(dig)
        length -= ran
        for i in range (ran):
            pwd += random.choice(punct)
        for i in range(length):
            pwd += random.choice(letter)
    pwd = list(pwd)
    random.shuffle(pwd)
    return ''.join(pwd)
    
print("Weak password example: " + password(6,num=True,strength='weak'))
print("Strong password example: " + password(12,num=True,strength='strong'))
print("Very Strong password example: " + password(18,num=True,strength='very'))