def is_prime(n):
    result = True
    index = 2
    while (index <= (n / 2)):
        if (n % index == 0):
            result = False
            break
        index += 1
    return result


def run():
    number = 100
    while (number < 121):
        print(number, is_prime(number))
        number += 1


run()
