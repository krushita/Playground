# We have a number of bunnies and each bunny has two big floppy ears. 
# We want to compute the total number of ears across all the bunnies 
# recursively (without loops or multiplication).

# bunnyEars(0) -> 0
# bunnyEars(1) -> 2
# bunnyEars(2) -> 4
def bunny_ears(inp):
    if (inp < 0):
        raise ValueError("Cannot find bunny ears for negative numbers!")

    if (inp == 0):
        return 0
    else:
        return  2 + bunny_ears(inp-1)

# We have bunnies standing in a line, numbered 1, 2, ... 
# The odd bunnies (1, 3, ..) have the normal 2 ears. 
# The even bunnies (2, 4, ..) we'll say have 3 ears, because they each have a 
# raised foot. Recursively return the number of "ears" in the bunny 
# line 1, 2, ... n (without loops or multiplication).

# bunnyEars2(0) -> 0
# bunnyEars2(1) -> 2
# bunnyEars2(2) -> 5
def bunny_ears_2(inp):
    if (inp < 0):
        raise ValueError("Cannot find bunny ears for negative numbers!")

    if (inp == 0):
        return 0
    else:
        if (inp % 2 ) == 0:
            # Even
            return 3 + bunny_ears_2(inp-1)
        else:
            # Odd
            return 2 + bunny_ears_2(inp-1)
 

if __name__ == "__main__":

    inp = 0
    #print "Bunny ears (" , inp , ") = ", bunny_ears(inp)
    print "Bunny ears (" , inp , ") = ", bunny_ears_2(inp)

    inp = 1
    #print "Bunny ears (" , inp , ") = ", bunny_ears(inp)
    print "Bunny ears (" , inp , ") = ", bunny_ears_2(inp)

    inp = 2
    #print "Bunny ears (" , inp , ") = ", bunny_ears(inp)
    print "Bunny ears (" , inp , ") = ", bunny_ears_2(inp)

    inp = 4
    #print "Bunny ears (" , inp , ") = ", bunny_ears(inp)
    print "Bunny ears (" , inp , ") = ", bunny_ears_2(inp)

    try:
        inp = -1
        print "Bunny ears (" , inp , ") = ", bunny_ears(inp)
    except Exception, e:
        print str(e)
      
