# Nuts and bolts. A disorganized carpenter has a mixed pile of n nuts and n bolts.
# The goal is to find the corresponding pairs of nuts and bolts. Each nut fits 
# exactly one bolt and each bolt fits exactly one nut. By fitting a nut and a bolt 
# together, the carpenter can see which one is bigger (but the carpenter cannot 
# compare two nuts or two bolts directly). Design an algorithm for the problem 
# that uses nlogn compares (probabilistically).
def quick_sort_nuts_and_bolts(nuts, bolts, start, end):
    if (start >= end):
        return

    # Find position of nut by comparing nuts with bolt as pivot
    nut_pos = partition(nuts, start, end, bolts[start])
    # Now, for above nut, find correct position for corresponding bolt
    bolt_pos = partition(bolts, start, end, nuts[nut_pos])

    # Recursively quick sort smaller nuts and bolts subarrays
    quick_sort_nuts_and_bolts(nuts, bolts, start, nut_pos-1)
    quick_sort_nuts_and_bolts(nuts, bolts, nut_pos+1, end)

# Use partitioning for 3 way sort
def partition(inp, start, end, pivot):
    lt = i = start
    gt = end

    while i <= gt:
        if inp[i] < pivot:
            # Swap values at i and lt
            temp = inp[i]
            inp[i] = inp[lt]
            inp[lt] = temp
            i += 1
            lt += 1

        elif inp[i] > pivot:
            # Swap values ar i and gt
            temp = inp[i]
            inp[i] = inp[gt]
            inp[gt] = temp
            gt -= 1

        else:
            i += 1


    # i points to the element equal to pivot
    return lt


if __name__ == "__main__":
    nuts = [5, 3, 2, 6, 4, 9, 7, 8, 1]
    bolts = [1, 6, 2, 4, 9, 7, 8, 3, 5]

    quick_sort_nuts_and_bolts(nuts, bolts, 0, len(nuts)-1)
    print 'Sorted nuts and bolts are:'
    print 'nuts =', nuts
    print 'bolts =', bolts
