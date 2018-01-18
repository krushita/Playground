# Given a string that contains a single pair of parenthesis, compute 
# recursively a new string made of only of the parenthesis and their contents,
# so "xyz(abc)123" yields "(abc)".

# parenBit("xyz(abc)123") -> "(abc)"
# parenBit("x(hello)") -> "(hello)"
# parenBit("(xy)1") -> "(xy)"
def parentBit(inp):

    if (inp == ""):
        return inp

    if (inp[0] == '('):
        if (inp.endswith(')')):
            return inp
        else:
            newStr = inp[:-1]
            return parentBit(newStr)
    else:
        newStr = inp[1:]
        return parentBit(newStr)


def test_parentBit():
    inp = "xyz(abc)123"
    print 'parentBit(', inp, ') = ', parentBit(inp)

    inp = "x(hello)"
    print 'parentBit(', inp, ') = ', parentBit(inp)

    inp = "(xy)1"
    print 'parentBit(', inp, ') = ', parentBit(inp)

    inp = "(("
    print 'parentBit(', inp, ') = ', parentBit(inp)



if __name__ == "__main__":
    test_parentBit()

