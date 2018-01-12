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


if __name__ == "__main__":

    #test_count7()
    test_countX()
