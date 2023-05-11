import math

#Alunas: Jéssica Celestino, Laura Schiavon e Mariana Fernandes.
class MathSamples:

    @staticmethod
    def fibonacci(n):
        if n == 0:
            return 0
        if n <= 2:
            return 1
        return MathSamples.fibonacci(n-1) \
                + MathSamples.fibonacci(n-2)

    @staticmethod
    def double(n):
        if(n == 0):
            return 1
        return n ** 2

    @staticmethod
    def power(b, p):
        if(p == 0):
            return 1
        return math.pow(b, p)
