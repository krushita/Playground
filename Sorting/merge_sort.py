#nlogn
#Divide array into halves till you reach arrays of size 1
#Then begin merging in to a new array.
#Needs extra space for merged array

def merge_sort(input, start, end):
    print "merge_sort input={}, start={}, end={}".format(input, start, end)
    if start >= end:
        return

    mid = start + (end - start)/2
    merge_sort(input, start, mid)
    merge_sort(input, mid+1, end)

    merged = [0 for i in range(end-start+1)]

    i = start
    j = mid+1
    k = 0

    while (i <= mid) and (j <= end):
        #print "i = {}, j = {}".format(i,j)
        if input[i] <= input[j]:
            merged[k] = input[i]
            i += 1
            k += 1
        else:
            merged[k] = input[j]
            j += 1
            k += 1

    while (i <= mid):
        merged[k] = input[i]
        i += 1
        k += 1

    while(j <= end):
        merged[k] = input[j]
        j += 1
        k += 1

    j = 0
    for k in range(start, end+1):
        print "k = {}".format(k)
        input[k] = merged[j]
        j += 1


if __name__ == "__main__":
    input1 = [6,3,9,2,10,1,8,7,4,5]
    merge_sort(input1, 0, len(input1)-1)
    print "Input1 Sorted array = ", input1

    input2 = [2,2,2,2,2,2]
    merge_sort(input1, 0, len(input2)-1)
    print "Input2 Sorted array = ", input2

    input3 = [1,2, 3]
    merge_sort(input3, 0, len(input3)-1)
    print "Input3 Sorted array = ", input3

