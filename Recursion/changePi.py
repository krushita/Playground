# Given a string, compute recursively (no loops) a new string where
# all appearances of "pi" have been replaced by "3.14".

# changePi("xpix") -> "x3.14x"
# changePi("pipi") -> "3.143.14"
# changePi("pip") -> "3.14p"
def changePi(inp, index):
    if (index < 0):
        raise ValueError("Index not valid")

    if (index >= len(inp)-1):
        return inp

    if (inp.startswith('pi', index)):
        inp = inp.replace('pi', '3.14', 1)
        return changePi(inp, index+4)
    else:
        return changePi(inp, index+1)

def test_changePi():
    inp = 'xpix'
    print 'For input', inp, "output = ", changePi(inp, 0)

    inp = 'pipi'
    print 'For input', inp, "output = ", changePi(inp, 0)

    inp = 'pip'
    print 'For input', inp, "output = ", changePi(inp, 0)


if __name__ == "__main__":

    test_changePi()
