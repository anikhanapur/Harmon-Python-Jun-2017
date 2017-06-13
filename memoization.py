
def get_prime_finder():
    cache = {}

    def is_prime(n):
        if (n in cache):
            return cache[n]

        print('processing ' + str(n))
        cache[n] = True
        index = 2
        while (index <= (n / 2)):
            if (n % index == 0):
                cache[n] = False
                break
            index += 1
        return cache[n]
    return is_prime


def get_even_odd_finder():
    cache = {}

    def is_even_odd(n):
        if (n in cache):
            return cache[n]

        print('processing ' + str(n))
        if (n % 2 == 0):
            cache[n] = 'even'
        else:
            cache[n] = 'odd'

        return cache[n]

    return is_even_odd


def memoize(algoFn):
    cache = {}

    def fn(n):
        if (n in cache):
            return cache[n]

        print('processing ' + str(n))
        cache[n] = algoFn(n)
        return cache[n]

    return fn




# def run():
#     number = 100
#     while (number < 121):
#         print(number, is_prime(number))
#         number += 1


# run()
