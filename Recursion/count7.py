# Given a non-negative int n, return the count of the occurrences of 7 as a digit,
# so for example 717 yields 2. (no loops). Note that mod (%) by 10 yields the
# rightmost digit (126 % 10 is 6), while divide (/) by 10 removes the rightmost digit (126 / 10 is 12).
# count7(717) -> 2
# count7(7) -> 1
# count7(123) -> 0
def count7(inp):
    if (inp < 0):
        raise ValueError("Invalid input (negative number)")

    if (inp == 0):
        return 0

    if (inp % 10) == 7:
        return 1 + count7(inp/10)
    else:
        return count7(inp/10)


# Given a string, compute recursively (no loops) the number of
# lowercase 'x' chars in the string.
# countX("xxhixx") -> 4
# countX("xhixhix") -> 3
# countX("hi") -> 0
def countX(inp):
    if (not isinstance(inp, str)):
        raise ValueError("Invalid input (not a string)")

    if (len(inp) == 0):
        return 0

    if (inp[-1] == 'x'):
        return 1 + countX(inp[:-1])
    else:
        return countX(inp[:-1])

#Count recursively the total number of "abc" and "aba" substrings that appear in the given string.

#countAbc("abc") -> 1
#countAbc("abcxxabc") -> 2
#countAbc("abaxxaba") -> 2
def countABC(inp, index):
    if (index < 0) or (index > len(inp)-1):
        raise ValueError('Invalid index')

    if (index >= len(inp)-2):
        return 0

    return 1 + countABC(inp, index+1) if (inp.startswith('abc', index)) or (inp.startswith('aba', index)) else countABC(inp, index+1)

# Given a string, compute recursively the number of times lowercase "hi" appears
# in the string, however do not count "hi" that have an 'x' immedately before them.

# countHi2("ahixhi") -> 1
# countHi2("ahibhi") -> 2
# countHi2("xhixhi") -> 0
def countHi2(inp, index):
    if (index < 0):
        raise ValueError('Invalid index')

    if (index > len(inp)-1):
        return 0

    if (inp.startswith('hi', index+1) and inp[index] == 'x'):
        return 1 + countHi2(inp, index+3)
    else:
        return countHi2(inp, index+1)

# Given a non-negative int n, compute recursively (no loops) the count of the 
# occurrences of 8 as a digit, except that an 8 with another 8 immediately to 
# its left counts double, so 8818 yields 4. Note that mod (%) by 10 yields the 
# rightmost digit (126 % 10 is 6), while divide (/) by 10 removes the 
# rightmost digit (126 / 10 is 12).

# count8(8) -> 1
# count8(818) -> 2
# count8(8818) -> 4
def count8(inp):
    if (inp < 0):
        raise ValueError('Invalid input number')

    if inp == 0:
        return 0

    if (inp % 10) == 8:
        next_inp = inp/10
        return 2 + (count8(inp/10)) if (next_inp %10 == 8) else 1 + (count8(inp/10))
    else:
        return 0 + count8(inp/10)


def test_count7():
    inp = 17
    print "Count(", inp, ") = ", count7(inp)

    inp = 1111
    print "Count(", inp, ") = ", count7(inp)

    inp = 0
    print "Count(", inp, ") = ", count7(inp)

    inp = 717
    print "Count(", inp, ") = ", count7(inp)

    inp = -1
    print "Count(", inp, ") = ", count7(inp)

def test_countX():
    inp = 'xxx'
    print "Count(", inp, ") = ", countX(inp)

    inp = 'xyyyd'
    print "Count(", inp, ") = ", countX(inp)

    inp = 'abc'
    print "Count(", inp, ") = ", countX(inp)

    inp = "a"
    print "Count(", inp, ") = ", countX(inp)

    inp = ""
    print "Count(", inp, ") = ", countX(inp)

    inp = "x"
    print "Count(", inp, ") = ", countX(inp)


def test_countABC():
    inp = 'abc'
    print '# of abc and aba in ', inp , '=', countABC(inp, 0)

    inp = 'abcxxabc'
    print '# of abc and aba in ', inp , '=', countABC(inp, 0)

    inp = 'abaxxaba'
    print '# of abc and aba in ', inp , '=', countABC(inp, 0)

    inp = ''
    print '# of abc and aba in ', inp , '=', countABC(inp, 0)

    try:
        inp = 5
    except Exception, e:
        print 'Error: ', str(e)

def test_countHi2():
    inp = 'ahixhi'
    print '# of xhi in ', inp , '=', countHi2(inp, 0)

    inp = 'ahibhi'
    print '# of xhi in ', inp , '=', countHi2(inp, 0)

    inp = 'xhixhi'
    print '# of xhi in ', inp , '=', countHi2(inp, 0)

    inp = ''
    print '# of xhi in ', inp , '=', countHi2(inp, 0)

def test_count8():
    inp = 8
    print 'count8(', inp, ') = ', count8(inp)

    inp = 818
    print 'count8(', inp, ') = ', count8(inp)

    inp = 8818
    print 'count8(', inp, ') = ', count8(inp)

if __name__ == "__main__":

    #test_count7()
    #test_countX()
    #test_countABC()
    #test_countHi2()
    test_count8()
