# Given a string, return true if it is a nesting of zero or more pairs of 
# parenthesis, like "(())" or "((()))". Suggestion: check the first and last 
# chars, and then recur on what's inside them.

# nestParen("(())") -> true
# nestParen("((()))") -> true
# nestParen("(((x))") -> false

def nestParen(inp):
    if (inp == ''):
        return True

    if inp[0] == '(' and inp[-1] == ')':
        new_str = inp[1:-1]
        return nestParen(new_str)
    else:
        return False

def test_nestParen():
    inp = '(())'
    print 'nestParen(', inp, ') = ', nestParen(inp)

    inp = '((()))'
    print 'nestParen(', inp, ') = ', nestParen(inp)

    inp = '(((x))'
    print 'nestParen(', inp, ') = ', nestParen(inp)


if __name__ == '__main__':
    test_nestParen()
