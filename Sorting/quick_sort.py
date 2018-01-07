# nlogn
# Select a pivot, usually 1st element
# For the remaining array, left = pivot + 1, right = end; all elements < pivot
# are to left and all element < pivot are moved to right.
# Finally pivot is swapped with right, it's final position
# quicksort left array and right array of pivot.
def quick_sort(input, start, end):
    #print "quick_sort array = {}, start = {}, end = {}".format(input, start, end)
    if start >= end:
        return
    pivot = input[start]
    left = start+1
    right = end

    while (left <= right):
        #print "left = {}, right = {}".format(left, right)
        while ((left <= right) and (input[left] <= pivot)):
            left += 1

        while((left <= right)) and (input[right] > pivot):
            right -= 1

        if (left < right):
            # Swap values at left and right
            temp = input[left]
            input[left] = input[right]
            input[right] = temp

    # Swap the pivot with right
    temp = input[start]
    input[start] = input[right]
    input[right] = temp

    quick_sort(input, start, right-1)
    quick_sort(input, right+1, end)

if __name__ == "__main__":
    input1 = [6,3,9,2,10,1,8,7,4,5]
    quick_sort(input1, 0, len(input1)-1)
    print "Input1 Sorted array = ", input1

    input2 = [2,2,2,2,2,2]
    quick_sort(input1, 0, len(input2)-1)
    print "Input2 Sorted array = ", input2

    input3 = [1,2, 3]
    quick_sort(input3, 0, len(input3)-1)
    print "Input3 Sorted array = ", input3

