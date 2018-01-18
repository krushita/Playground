# Given a string and a non-empty substring sub, compute recursively the largest
# substring which starts and ends with sub and return its length.

# strDist("catcowcat", "cat") -> 9
# strDist("catcowcat", "cow") -> 3
# strDist("cccatcowcatxx", "cat") -> 9
def strDist(inp, sub):
    if (inp == "" or len(inp) < len(sub)):
        return 0

    if inp.startswith(sub):
        if inp.endswith(sub):
            return len(inp)
        else:
            return strDist(inp[:-1], sub)
    return strDist(inp[1:], sub)

def test_strDist():
    inp = "catcowcat"
    sub = "cat"
    print 'strDist(', inp, sub, ') = ', strDist(inp, sub)

    inp = "catcowcat"
    sub = "cow"
    print 'strDist(', inp, sub, ') = ', strDist(inp, sub)

    inp = "cccatcowcatxx"
    sub = "cat"
    print 'strDist(', inp, sub, ') = ', strDist(inp, sub)


if __name__ == '__main__':
    test_strDist()
