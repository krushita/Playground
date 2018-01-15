# Given a string and a non-empty substring sub, compute recursively the number
# of times that sub appears in the string, without the sub strings overlapping.

# strCount("catcowcat", "cat") -> 2
# strCount("catcowcat", "cow") -> 1
# strCount("catcowcat", "dog") -> 0
def strCount(inp, sub, index):
    if (index < 0):
        raise ValueError('Invalid index')

    if (index > len(inp)-1):
        return 0

    if inp.startswith(sub, index):
        return 1 + strCount(inp, sub, index+len(sub))
    else:
        return strCount(inp, sub, index+1)


def test_strCount():
    inp = "catcowcat"
    sub = 'cat'
    print 'strCount(', inp, sub, ') = ', strCount(inp, sub, 0)

    inp = "catcowcat"
    sub = 'cow'
    print 'strCount(', inp, sub, ') = ', strCount(inp, sub, 0)

    inp = "catcowcat"
    sub = 'dog'
    print 'strCount(', inp, sub, ') = ', strCount(inp, sub, 0)

    inp = "cccccc"
    sub = 'cc'
    print 'strCount(', inp, sub, ') = ', strCount(inp, sub, 0)

    inp = ""
    sub = 'cat'
    print 'strCount(', inp, sub, ') = ', strCount(inp, sub, 0)


if __name__ == "__main__":
    test_strCount()
