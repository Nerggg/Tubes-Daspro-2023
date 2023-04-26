import random

# fungsi ini menerima 'n' sebagai integer yang menjadi rentang bawah bilangan random
def rng(n):

    # mengembalikan nilai random yang berada pada rentang n <= nilai <= 5 dengan library 'random'
    return random.randint(n,5)
