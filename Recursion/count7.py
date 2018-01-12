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

if __name__ == "__main__":

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

