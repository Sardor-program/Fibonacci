

from functools import lru_cache

@lru_cache
def fibonacci(number):
    print(number)
    if number < 2:
        return 1
    return fibonacci(number-1) + fibonacci(number-2)









