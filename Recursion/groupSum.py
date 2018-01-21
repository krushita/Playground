# Given an array of ints, is it possible to choose a group of some of the ints,
# such that the group sums to the given target? This is a classic backtracking 
# recursion problem. Once you understand the recursive backtracking strategy in
# this problem, you can use the same pattern for many problems to search a 
# space of choices. Rather than looking at the whole array, our convention is 
# to consider the part of the array starting at index start and continuing to 
# the end of the array. The caller can specify the whole array simply by 
# passing start as 0. No loops are needed -- the recursive calls progress down 
# the array.

# groupSum(0, [2, 4, 8], 10) -> true
# groupSum(0, [2, 4, 8], 14) -> true
# groupSum(0, [2, 4, 8], 9) -> false
def groupSum(index, inp, sum):
    if (len(inp) == 0) or (index > len(inp)-1):
        if sum == 0:
            return True
        else:
            return False
 
    return groupSum(index+1, inp, sum - inp[index]) or groupSum(index+1, inp, sum)

# Given an array of ints, is it possible to choose a group of some of the ints,
# such that the group sums to the given target with these additional 
# constraints: all multiples of 5 in the array must be included in the group. 
# If the value immediately following a multiple of 5 is 1, it must not be 
# chosen. (No loops needed.)

# groupSum5(0, [2, 5, 10, 4], 19) -> true
# groupSum5(0, [2, 5, 10, 4], 17) -> true
# groupSum5(0, [2, 5, 10, 4], 12) -> false
def groupSum5(index, inp, sum):
    if (len(inp) == 0) or (index > len(inp)-1):
        if sum == 0:
            return True
        else:
            return False

    if (inp[index] % 5 == 0):
        if (index < len(inp)-1) and inp[index+1] == 1:
            return groupSum5(index+2, inp, sum - inp[index])
        else:
            return groupSum5(index+1, inp, sum - inp[index])

    return groupSum5(index+1, inp, sum - inp[index]) or groupSum5(index+1, inp, sum)


# Given an array of ints, is it possible to choose a group of some of the ints,
# beginning at the start index, such that the group sums to the given target?
# However, with the additional constraint that all 6's must be chosen. (No loops needed.)

# groupSum6(0, [5, 6, 2], 8) -> true
# groupSum6(0, [5, 6, 2], 9) -> false
# groupSum6(0, [5, 6, 2], 7) -> false
def groupSum6(index, inp, sum):
    if (len(inp) == 0) or (index > len(inp)-1):
        if sum == 0:
            return True
        else:
            return False

    if (inp[index] % 6 == 0):
        return groupSum6(index+1, inp, sum - inp[index])

    return groupSum6(index+1, inp, sum - inp[index]) or groupSum6(index+1, inp, sum)  

# Given an array of ints, is it possible to choose a group of some of the ints,
# such that the group sums to the given target with this additional
# constraint: If a value in the array is chosen to be in the group, the value 
# immediately following it in the array must not be chosen. (No loops needed.)
# groupNoAdj(0, [2, 5, 10, 4], 12) -> true
# groupNoAdj(0, [2, 5, 10, 4], 14) -> false
# groupNoAdj(0, [2, 5, 10, 4], 7) -> false
def groupAdj(index, inp, sum):
    if (len(inp) == 0) or (index > len(inp)-1):
        return sum == 0

    return groupAdj(index+2, inp, sum - inp[index]) or \
        groupAdj(index+1, inp, sum)


def test_groupSum():
    inp = [2, 4, 8]
    sum = 10
    print 'groupSum(', inp, sum, ') = ', groupSum(0, inp, sum)

    inp = [2, 4, 8]
    sum = 14
    print 'groupSum(', inp, sum, ') = ', groupSum(0, inp, sum)

    inp = [2, 4, 8]
    sum = 9
    print 'groupSum(', inp, sum, ') = ', groupSum(0, inp, sum)

def test_groupSum5():
    inp = [2, 5, 10, 4]
    sum = 19
    print 'groupSum5(', inp, sum, ') = ', groupSum5(0, inp, sum)

    inp = [2, 5, 10, 4]
    sum = 17
    print 'groupSum(', inp, sum, ') = ', groupSum5(0, inp, sum)

    inp = [2, 5, 10, 4]
    sum = 12
    print 'groupSum(', inp, sum, ') = ', groupSum5(0, inp, sum)

def test_groupSum6():
    inp = [5, 6, 2]
    sum = 8
    print 'groupSum5(', inp, sum, ') = ', groupSum6(0, inp, sum)

    inp = [5, 6, 2]
    sum = 9
    print 'groupSum(', inp, sum, ') = ', groupSum6(0, inp, sum)

    inp = [5, 6, 2]
    sum = 7
    print 'groupSum(', inp, sum, ') = ', groupSum6(0, inp, sum)

def test_groupAdj():
    inp = [2, 5, 10, 4]
    sum = 12
    print 'groupSum5(', inp, sum, ') = ', groupAdj(0, inp, sum)

    inp = [2, 5, 10, 4]
    sum = 14
    print 'groupSum(', inp, sum, ') = ', groupAdj(0, inp, sum)

    inp = [2, 5, 10, 4]
    sum = 7
    print 'groupSum(', inp, sum, ') = ', groupAdj(0, inp, sum)


if __name__ == "__main__":
    #test_groupSum()
    #test_groupSum5()
    #test_groupSum6()
    test_groupAdj()

