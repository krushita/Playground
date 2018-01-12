def factorial(inp):
    if (inp < 0):
        raise ValueError("Cannot find factorial for negative numbers!")

    if (inp == 0 or inp == 1):
        return 1
    else:
        return inp * factorial(inp-1)


if __name__ == "__main__":

    inp = 15
    print "Factorial (" , inp , ") = ", factorial(inp)

    inp = 0
    print "Factorial (" , inp , ") = ", factorial(inp)

    inp = 1
    print "Factorial (" , inp , ") = ", factorial(inp)

    try:
        inp = -1
        print "Factorial (" , inp , ") = ", factorial(inp)
    except Exception, e:
        print str(e)
      
