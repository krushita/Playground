# Given a string, compute recursively (no loops) a new string where all the lowercase 'x' chars have been changed to 'y' chars.

# changeXY("codex") -> "codey"
# changeXY("xxhixx") -> "yyhiyy"
# changeXY("xhixhix") -> "yhiyhiy"
def changeXY(inp, index):
    if (inp == "" or index > len(inp)-1):
        return inp

    if inp[index] == 'x':
        inp = inp.replace('x', 'y', 1)

    return changeXY(inp, index+1)

def test_changeXY():
    inp = "codex"
    print 'changeXY(', inp, ') = ', changeXY(inp, 0)

    inp = "xxhixx"
    print 'changeXY(', inp, ') = ', changeXY(inp, 0)

    inp = "xhixhix"
    print 'changeXY(', inp, ') = ', changeXY(inp, 0)


if __name__ == "__main__":
    test_changeXY()
