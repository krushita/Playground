# Given a string, return recursively a "cleaned" string where adjacent chars 
# that are the same have been reduced to a single char. So "yyzzza" yields "yza".

# stringClean("yyzzza") -> "yza"
# stringClean("abbbcdd") -> "abcd"
# stringClean("Hello") -> "Helo"
def stringClean(inp_list, index):
    if (index >= len(inp_list)-1 or len(inp_list) == 0):
        return inp_list

    if (inp_list[index] == inp_list[index+1]):
        del(inp_list[index+1])
        return stringClean(inp_list,index)

    return stringClean(inp_list, index+1)

def test_stringClean():

    inp = list("yyzzza")
    print 'stringClean(', inp, ') =', ''.join(stringClean(inp, 0))

    inp = list("abbbcdd")
    print 'stringClean(', inp, ') =', ''.join(stringClean(inp, 0))


    inp = list("Hello")
    print 'stringClean(', inp, ') =', ''.join(stringClean(inp, 0))


if __name__ == '__main__':
    test_stringClean()
