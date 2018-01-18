# Given base and n that are both 1 or more, compute recursively (no loops) the
# value of base to the n power, so powerN(3, 2) is 9 (3 squared).

# powerN(3, 1) -> 3
# powerN(3, 2) -> 9
# powerN(3, 3) -> 27
def powerN(base, n):
    if (n == 1):
        return base

    return base * powerN(base, n-1)


def test_powerN():

    base = 3
    n = 1
    print 'powerN(', base, n, ') = ', powerN(base, n)

    base = 3
    n = 2
    print 'powerN(', base, n, ') = ', powerN(base, n)

    base = 3
    n = 3
    print 'powerN(', base, n, ') = ', powerN(base, n)

if __name__ == '__main__':
    test_powerN()
