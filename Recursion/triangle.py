# We have triangle made of blocks. The topmost row has 1 block, the next row
# down has 2 blocks, the next row has 3 blocks, and so on. Compute recursively 
# (no loops or multiplication) the total number of blocks in such a triangle 
# with the given number of rows.

# triangle(0) -> 0
# triangle(1) -> 1
# triangle(2) -> 3
def triangle(row):
    if (row < 0):
        raise ValueError('Invalid row')

    if (row == 0):
        return 0

    return row + triangle(row-1)

def test_triangle():
    row = 0
    print 'triange(', row, ') = ', triangle(row)

    row = 1
    print 'triange(', row, ') = ', triangle(row)

    row = 2
    print 'triange(', row, ') = ', triangle(row)



if __name__ == '__main__':
    test_triangle()
