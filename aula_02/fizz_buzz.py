# Alunas: Jéssica Celestino, Laura Schiavon e Mariana Fernandes.

def fizz_buzz(n):
    if isinstance(n, str):
        return f'{n} não é fizzbuzz é buzlaitir 🚀'
    else:
        if n % 3 == 0 and n % 5 == 0:
            return 'fizzbuzz'
        if n % 3 == 0:
            return 'fizz'
        elif n % 5 == 0:
            return 'buzz'
        return n
