# Given a string, compute recursively a new string where all the 'x' chars 
# have been removed.

# noX("xaxb") -> "ab"
# noX("abc") -> "abc"
# noX("xx") -> ""
def noX(inp, index):
    if (index < 0):
        raise ValueError('Invalid input index')

    if (index > len(inp)-1):
        return inp

    if (inp[index] == 'x'):
        inp = inp.replace('x', '')
    return noX(inp, index+1)

def test_noX():
    inp = "xaxb" 
    print 'noX(', inp, ') = ', noX(inp, 0)

    inp = "abc" 
    print 'noX(', inp, ') = ', noX(inp, 0)

    inp = "xx" 
    print 'noX(', inp, ') = ', noX(inp, 0)


if __name__ == "__main__":
    test_noX()
