# We'll say that a "pair" in a string is two instances of a char separated by a
# char. So "AxA" the A's make a pair. Pair's can overlap, so "AxAxA" contains
# 3 pairs -- 2 for A and 1 for x. Recursively compute the number of pairs in 
# the given string.

# countPairs("axa") -> 1
# countPairs("axax") -> 2
# countPairs("axbx") -> 1
def countPairs(inp):
    if (len(inp) == 3 and inp[0] == inp[2]):
        return 1

    if (len(inp) < 3):
        return 0

    new_str = inp[1:]
    if (inp[0] == inp[2]):
        return 1 + countPairs(new_str)
    
    return countPairs(new_str)


def test_countPairs():
    inp = 'axa'
    print 'countPairs(', inp, ') = ', countPairs(inp)

    inp = 'axax'
    print 'countPairs(', inp, ') = ', countPairs(inp)

    inp = 'axbx'
    print 'countPairs(', inp, ') = ', countPairs(inp)

    inp = 'axaxa'
    print 'countPairs(', inp, ') = ', countPairs(inp)

if __name__ == '__main__':
    test_countPairs()
