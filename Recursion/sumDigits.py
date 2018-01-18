# Given a non-negative int n, return the sum of its digits recursively (no loops).
# Note that mod (%) by 10 yields the rightmost digit (126 % 10 is 6), while 
# divide (/) by 10 removes the rightmost digit (126 / 10 is 12).

# sumDigits(126) -> 9
# sumDigits(49) -> 13
# sumDigits(12) -> 3
def sumDigits(n):
    if (n < 0):
        raise ValueError("Invalid input: negative number")

    if (n == 0):
        return 0

    return n % 10 + sumDigits(n/10)

def test_sumDigits():
    n = 126
    print 'test_sumDigits(', n, ') =', sumDigits(n)

    n = 49
    print 'test_sumDigits(', n, ') =', sumDigits(n)

    n = 3
    print 'test_sumDigits(', n, ') =', sumDigits(n)

    try:
        n = -1
        print 'test_sumDigits(', n, ') =', sumDigits(n)
    except Exception, e:
        print "Error: ", str(e)

if __name__ == '__main__':
    
        test_sumDigits()
