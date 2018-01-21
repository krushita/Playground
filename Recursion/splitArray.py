# Given an array of ints, is it possible to divide the ints into two groups,
# so that the sums of the two groups are the same. Every int must be in one 
# group or the other. Write a recursive helper method that takes whatever 
# arguments you like, and make the initial call to your recursive helper 
# from splitArray(). (No loops needed.)

# splitArray([2, 2]) -> true
# splitArray([2, 3]) -> false
# splitArray([5, 2, 3]) -> true
def splitArray(inp):
    return splitArray_helper(inp, 0, 0 , 0)
    

def splitArray_helper(inp, index, sum1, sum2):
    if (index > len(inp)-1):
        return sum1 == sum2

    return splitArray_helper(inp, index+1, sum1 + inp[index], sum2) \
        or splitArray_helper(inp, index+1, sum1, sum2 + inp[index])


# Given an array of ints, is it possible to divide the ints into two groups,
# so that the sum of the two groups is the same, with these constraints: all 
# the values that are multiple of 5 must be in one group, and all the values 
# that are a multiple of 3 (and not a multiple of 5) must be in the other.
# (No loops needed.)

# split53([1, 1]) -> true
# split53([1, 1, 1]) -> false
# split53([2, 4, 2]) -> true
def split53():
    return split53_helper(inp, 0, 0 , 0)


def split53_helper(inp, index, sum1, sum2):
    if (index > len(inp)-1):
        return sum1 == sum2

    if (inp[index] % 5) == 0:
        return split53_helper(inp, index+1, sum1 + inp[index], sum2)
    elif (inp[index] % 3) == 0:
        return split53_helper(inp, index+1, sum1, sum2 + inp[index])
    else:
        return split53_helper(inp, index+1, sum1 + inp[index], sum2) or \
            split53_helper(inp, index+1, sum1, sum2 + inp[index])


def test_splitArray():
    inp = [2, 2]
    print 'splitArray(', inp, ') = ', splitArray(inp)

    inp = [2, 3]
    print 'splitArray(', inp, ') = ', splitArray(inp)

    inp = [5, 2, 3]
    print 'splitArray(', inp, ') = ', splitArray(inp)

    inp = [0, 0]
    print 'splitArray(', inp, ') = ', splitArray(inp)

    inp = [3,9,3,3]
    print 'splitArray(', inp, ') = ', splitArray(inp)

    inp = [15,6,5,9,3,2]
    print 'splitArray(', inp, ') = ', splitArray(inp)


def test_split53():
    inp = [1, 1]
    print 'splitArray(', inp, ') = ', splitArray(inp)

    inp = [1, 1, 1]
    print 'splitArray(', inp, ') = ', splitArray(inp)

    inp = [2, 4, 2]
    print 'splitArray(', inp, ') = ', splitArray(inp)

    inp = [0, 0]
    print 'splitArray(', inp, ') = ', splitArray(inp)

    inp = [5, 10, 3, 6, 6]
    print 'splitArray(', inp, ') = ', splitArray(inp)


if __name__ == "__main__":
    # test_splitArray()
    test_split53()
