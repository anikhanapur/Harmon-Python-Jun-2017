

def echo():
    while True:
        line = input('> ')
        if (line == 'done'):
            break
        print line

    print 'Good Bye!'


if (__name__ == '__main__'):
    echo()


