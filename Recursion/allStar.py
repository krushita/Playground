# Given a string, compute recursively a new string where all the adjacent chars
# are now separated by a "*".

# allStar("hello") -> "h*e*l*l*o"
# allStar("abc") -> "a*b*c"
# allStar("ab") -> "a*b"
def allStar(inp_list, index):
    if (len(inp_list) == 0 or index >= len(inp_list)-1):
        return inp_list

    inp_list.insert(index+1, '*')
    return allStar(inp_list, index + 2)


def test_allStar():
    inp = list('hello')
    print 'allStar(', inp, ') = ', ''.join(allStar(inp, 0))

    inp = list('abc')
    print 'allStar(', inp, ') = ', ''.join(allStar(inp, 0))

    inp = list('ab')
    print 'allStar(', inp, ') = ', ''.join(allStar(inp, 0))

if __name__ == "__main__":
    test_allStar()
