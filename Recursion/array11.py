# Given an array of ints, compute recursively the number of times that the
# value 11 appears in the array. We'll use the convention of considering only
# the part of the array that begins at the given index. In this way, a 
# recursive call can pass index+1 to move down the array. 
# The initial call will pass in index as 0.

# array11([1, 2, 11], 0) -> 1
# array11([11, 11], 0) -> 2
# array11([1, 2, 3, 4], 0) -> 0
def isArray11(arr):
    if not isinstance(arr, list):
        return ValueError("Input not an array")

    if len(arr) == 0:
        return 0
    else:
        return 1 + isArray(arr[1:]) if (arr[0] == 11) else isArray(arr[1:])


# Given an array of ints, compute recursively if the array contains somewhere
# a value followed in the array by that value times 10. We'll use the 
# convention of considering only the part of the array that begins at the 
# given index. In this way, a recursive call can pass index+1 to move down 
# the array. The initial call will pass in index as 0.

# array220([1, 2, 20], 0) → true
# array220([3, 30], 0) → true
# array220([3], 0) → false
def isArray220(arr, index):
    if not isinstance(arr, list):
        return ValueError("Input not an array")
    elif (index < 0) or (index > len(arr)-1):
        return ValueError("Invalid input index")

    if index == len(arr)-1:
        return 0
    else:
        return 1 if (arr[index+1] == arr[index]*10) else isArray220(arr, index+1)


def testIsArray11():
    inp = [1,5,11]
    print "# of 11s in array",inp, " = " , isArray11(inp)

    inp = [1,11,11]
    print "# of 11s in array",inp, " = " , isArray11(inp)

    inp = [11,11,11,11]
    print "# of 11s in array",inp, " = " , isArray11(inp)

    inp = []
    print "# of 11s in array",inp, " = " , isArray11(inp)

    inp = [11]
    print "# of 11s in array",inp, " = " , isArray11(inp)

    inp = [13]
    print "# of 11s in array",inp, " = " , isArray11(inp)

    inp = [1,5,7]
    print "# of 11s in array",inp, " = " , isArray11(inp)

    try:
        inp = 5
    except Exception, e:
        print "Error: ", str(e)

def testIsArray220():

    inp = [1, 2, 20]
    print "Found times 10 for ",inp, " = " , isArray220(inp, 0)

    inp = [3, 30]
    print "Found times 10 for ",inp, " = " , isArray220(inp, 0)

    inp = [3]
    print "Found times 10 for ",inp, " = " , isArray220(inp, 0)

    inp = [2, 3, 4, 5, 6]
    print "Found times 10 for ",inp, " = " , isArray220(inp, 0)

    try:
        inp = 5
    except Exception, e:
        print "Error: ", str(e)

if __name__ == "__main__":
    #testIsArray11()
    testIsArray220()


