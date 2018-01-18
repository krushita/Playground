# Given a string and a non-empty substring sub, compute recursively if at least
# n copies of sub appear in the string somewhere, possibly with overlapping.
# N will be non-negative.

# strCopies("catcowcat", "cat", 2) -> true
# strCopies("catcowcat", "cow", 2) -> false
# strCopies("catcowcat", "cow", 1) -> true
def strCopies(inp, sub, n):

    if (n == 0):
        return True

    if (len(inp) < len(sub)):
        return False

    new_str = inp[1:]
    if (inp.startswith(sub)):
        return strCopies(new_str, sub, n-1)
    else:
        return strCopies(new_str, sub, n)

def test_strCopies():
    inp = "catcowcat"
    sub = "cat"
    n = 2
    print 'strCopies(', inp, sub, n, ') = ', strCopies(inp, sub, n)

    inp = "catcowcat"
    sub = "cow"
    n = 2
    print 'strCopies(', inp, sub, n, ') = ', strCopies(inp, sub, n)


    inp = "catcowcat"
    sub = "cow"
    n = 1
    print 'strCopies(', inp, sub, n, ') = ', strCopies(inp, sub, n)


    inp = ""
    sub = "cat"
    n = 2
    print 'strCopies(', inp, sub, n, ') = ', strCopies(inp, sub, n)

if __name__ == "__main__":
    test_strCopies()

