# Given a string, compute recursively a new string where all the lowercase
# 'x' chars have been moved to the end of the string.

# endX("xxre") -> "rexx"
# endX("xxhixx") -> "hixxxx"
# endX("xhixhix") -> "hihixxx"
def endX(inp):
    if (len(inp) == 0 or len(inp) == 1):
        return inp

    new_inp = inp[1:]
    if (inp[0] == 'x'):
        return endX(new_inp) + 'x'
    else:
        return inp[0] + endX(new_inp)

def test_endX():
    inp = 'xxre'
    print 'endX(', inp, ') = ', endX(inp)

    inp = 'xxhixx'
    print 'endX(', inp, ') = ', endX(inp)

    inp = 'xhixhix'
    print 'endX(', inp, ') = ', endX(inp)

if __name__ == "__main__":
    test_endX()
