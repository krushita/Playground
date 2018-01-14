def isArray(arr):
    if not isinstance(arr, list):
        return ValueError("Input not an array")

    if len(arr) == 0:
        return 0
    else:
        return 1 + isArray(arr[1:]) if (arr[0] == 11) else isArray(arr[1:])

if __name__ == "__main__":

    inp = [1,5,11]
    print "# of 11s in array",inp, " = " , isArray(inp)

    inp = [1,11,11]
    print "# of 11s in array",inp, " = " , isArray(inp)

    inp = [11,11,11,11]
    print "# of 11s in array",inp, " = " , isArray(inp)

    inp = []
    print "# of 11s in array",inp, " = " , isArray(inp)

    inp = [11]
    print "# of 11s in array",inp, " = " , isArray(inp)

    inp = [13]
    print "# of 11s in array",inp, " = " , isArray(inp)

    inp = [1,5,7]
    print "# of 11s in array",inp, " = " , isArray(inp)

    try:
        inp = 5
    except Exception, e:
        print "Error: ", str(e)
