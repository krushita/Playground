# Heap Sort
# https://d18ky98rnyall9.cloudfront.net/_b85511f4ea522da4caf6b02d10fc0bad_24PriorityQueues.pdf?Expires=1490486400&Signature=CgBbsRh0x3ERrV~t5wRfvA~8PVVvFbUM9fMY33Cbn89hofBWKX-TdQh9-gbiL4H9Q1QN9CDOtSyCoQHTvqbW401DWqTOOYWExNq~eW5nv4N1Raaerse0Igm~wkgK83dRQEgScbDWJWiZanU9bgSL2XBPlrlSRiX2t~qTrtJxOe4_&Key-Pair-Id=APKAJLTNE6QMUY6HBC5A


def sink(input, k, n):
  while (2*k < n):
    idx = 2*k
    if (idx+1 < n) and (input[idx+1] > input[idx]): # If child at idx+1 is greater use that
      idx = idx + 1
    if input[k] < input[idx]:
      # Exchange parent with max_child
      temp = input[k]
      input[k] = input[idx]
      input[idx] = temp
      k = idx
    else:
      break

def heap_sort(input):
    # Create heap out of the input
    # Go through first half of array and sink each element to its correct
    # position in the heap
    n = len(input)
    # Construct heap/heapify
    for k in range(n/2, 0, -1):
      sink(input, k, n)
    # Also take care of element at index 0
    sink(input, 0, n)

    # Sort: Exchange root with last element, sink new root to right position
    len = n
    while (len > 1):
      # Exchange root with last
      max = input[0]
      input[0] = input[len-1]
      input[len-1] = max
      len -= 1
      # Sink new root to right position
      sink(input, 1, len)

if __name__ == "__main__":
    input1 = [6,3,9,2,10,1,8,7,4,5]
    heap_sort(input1)
    print "Input1 Sorted array = ", input1

