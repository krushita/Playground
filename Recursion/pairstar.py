#Given a string, compute recursively a new string where identical chars that 
# are adjacent in the original string are separated from each other by a "*".

# pairStar("hello") -> "hel*lo"
# pairStar("xxyy") -> "x*xy*y"
# pairStar("aaaa") -> "a*a*a*a"

def pairStar(inp_list, index):
    if (index < 0):
        raise ValueError("Invalid index")

    if (index >= len(inp_list)-1):
        return inp_list

    if (inp_list[index] == inp_list[index+1]):
        inp_list.insert(index+1, '*')
        return pairStar(inp_list, index+2)
    else:
        return pairStar(inp_list, index+1)

def test_pairStar():
    inp_list = list("hello")
    print 'pairStar(', ''.join(inp_list), ") = ", ''.join(pairStar(inp_list, 0))

    inp_list = list("xxyy")
    print 'pairStar(', ''.join(inp_list), ") = ", ''.join(pairStar(inp_list, 0))

    inp_list = list("aaaa")
    print 'pairStar(', ''.join(inp_list), ") = ", ''.join(pairStar(inp_list, 0))

    inp_list = list("xyz")
    print 'pairStar(', ''.join(inp_list), ") = ", ''.join(pairStar(inp_list, 0))

    inp_list = list("")
    print 'pairStar(', ''.join(inp_list), ") = ", ''.join(pairStar(inp_list, 0))


if __name__ == "__main__":
    test_pairStar()



