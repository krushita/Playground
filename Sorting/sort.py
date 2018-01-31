class Sort(object):
    def __init__(self, sort_fn):
        self.sort_fn = sort_fn

    def __call__(self, inp):
        if self.sort_fn == 'insertion':
            return self.__insertion_sort(inp)
        elif self.sort_fn == 'selection':
            return self.__selection_sort(inp)
        elif self.sort_fn == 'shell':
            return self.__shell_sort(inp)
        elif self.sort_fn == 'merge':
            return self.__merge_sort_caller(inp)
        elif self.sort_fn == 'quick':
            return self.__quick_sort(inp, 0, len(inp)-1)
        elif self.sort_fn == 'quick_3':
            return self.__quick_3_sort(inp, 0, len(inp)-1)



    # For each element in the array, insert in the leftmost sorted array in
    # its right position. Sorted array starts with size 1 (leftmost element).
    # Move each element to temp position , closer to its final position and
    # to the left.
    # Time complexity : 
    # Best: Sorted array: n-1 comparisons, 0 exchanges  O(n)
    # Worst: Reverse sorted array: ~n^2 comparision, n^2 exchanges O(n^2)
    def __insertion_sort(self, inp):
        if (len(inp) == 0):
            return inp

        size = len(inp)
        for i in range(1, size):
            comp = inp[i]
            for j in range(i, -1, 0):
                if (inp[j] < inp[j-1]):
                    # Exchange elements at j and j-1
                    temp = inp[j-1]
                    inp[j-1] = inp[j]
                    inp[j] = temp
                else:
                    break
        return inp

    # In each iteration i, find the index of min entry in remaining array
    # and exchange it with a[i]. Move each element to its final position on left.
    # Time complexity: Best/Worst O(n^2)
    def __selection_sort(self, inp):
        if (len(inp) == 0):
            return inp

        size = len(inp)
        for i in range(0, size):
            min = inp[i]
            min_index = i
            for j in range(i+1, size):
                if inp[j] < min:
                    min = inp[j]
                    min_index = j
            # Exchange min with inp[i]
            temp = inp[i]
            inp[i] = inp[min_index]
            inp[min_index] = temp
        return inp


    def __merge_sort_caller(self, inp):
        self.__merge_sort(inp, 0, len(inp)-1)
        return inp

    # Divide array into 2 halves till we have 1-element array.
    # Then merge the 2 arrays in sorted order.
    # Complexity O n(log n)
    def __merge_sort(self, inp, start, end):
        if (start >= end):
            return

        mid = start + (end-start)/2
        self.__merge_sort(inp, start, mid)
        self.__merge_sort(inp, mid+1, end)

        # Merge sorted arrays into merged
        merged = [0 for i in range(0, end+1)]

        i = start
        j = mid+1
        k = 0

        while i <= mid and j <= end:
            if inp[i] <= inp[j]:
                merged[k] = inp[i]
                i += 1
                k += 1
            else:
                merged[k] = inp[j]
                j += 1
                k += 1

        while i <= mid:
            merged[k] = inp[i]
            i += 1
            k += 1

        while j <= end:
            merged[k] = inp[j]
            j += 1
            k += 1

        # Copy merged back to inp
        j = 0
        for i in range(start, end+1):
            inp[i] = merged[j]
            j += 1
        return


    # Similar to insertion sort, but every time compare with hth element
    # and construct h-sorted array. Do for different values of h till h >= 1
    # Time complexity : 
    # Best: Sorted array: n-1 comparisons, 0 exchanges  O(n)
    # Worst: Reverse sorted array: ~n^2 comparision, n^2 exchanges O(n^2)
    def __shell_sort(self, inp):
        if (len(inp) == 0):
            return inp

        h = 1
        size = len(inp)
        while h < size/3:
            h = 3*h + 1

        while h >= 1:
            for i in range(h, size):
                comp = inp[i]
                for j in range(i, -h, h+1):
                    if (inp[j-h] > inp[j]):
                        # Exchange elements at j and j-h
                        temp = inp[j-h]
                        inp[j-h] = inp[j]
                        inp[j] = temp
                    else:
                        break
            h = h/3
        return inp

    # In-place, nlog(n)
    # Pick a pivot - assume inp[0].
    # Partition the array:
    #  Make left and right point to pivot+1 and end positions of array.
    #  Keep incrementing left until inp[left] <= pivot.
    #  Keep decrementing right until inp[right] >= pivot.
    #  Exchange inp[left] and inp[right].
    #  Repeat till left and right cross each other. Pivot positon is finalized.
    # Repeat quicksort on left half and right half of array.
    def __quick_sort(self, inp, start, end):
        if start >= end:
            return

        # Parition array
        pivot_pos = self.__partition_quick_sort(inp, start, end)

        self.__quick_sort(inp, start, pivot_pos-1)
        self.__quick_sort(inp, pivot_pos+1, end)
        return inp

    def __partition_quick_sort(self, inp, start, end):
        pivot = inp[start]
        left = start+1
        right = end

        while left <= right:
            while left <= right and inp[left] <= pivot:
                left += 1

            while left <= right and inp[right] >= pivot:
                right -= 1

            if left < right:
                temp = inp[left]
                inp[left] = inp[right]
                inp[right] = temp

        # Swap pivot and right
        temp = inp[right]
        inp[right] = pivot
        inp[start] = temp
        return right

    # Similar to quick sort, but more efficient for repeated values.
    # Use lt, gt and i
    # Invariant : Values left of lt is less than pivot, right of gt is 
    # greater than pivot and in between them is equal to pivot
    # Partition the array: 
    #  Pivot = inp[start]
    #  Make lt/i and gt point to inp[start] and end positions of array.
    #  Keep incrementing i and compare value at i to vaues at lt and gt
    #    If inp[i] < pivot, exchange with inp[lt], i++, lt++
    #    If inp[i] > pivot, exchange with inp[gt], gt--  (do NOT incr i, as next value at gt needs to be checked)
    #    If inp[i] == pivot, NO exchange, i++
    #  Repeat till i and gt cross each other. Pivot positon is finalized.
    # Repeat quick3sort on left half and right half of array.
    def __quick_3_sort(self, inp, start, end):
        if start >= end:
            return

        # Parition array
        lt, gt = self.__partition_quick_3_sort(inp, start, end)

        self.__quick_3_sort(inp, start, lt-1)
        self.__quick_3_sort(inp, gt+1, end)
        return inp

    def __partition_quick_3_sort(self, inp, start, end):
        pivot = inp[start]
        lt = i = start
        gt = end

        while i <= gt:
            if inp[i] < pivot:
                temp = inp[lt]
                inp[lt] = inp[i]
                inp[i] = temp
                i += 1
                lt += 1
            elif inp[i] > pivot:
                temp = inp[gt]
                inp[gt] = inp[i]
                inp[i] = temp
                gt -= 1
            elif inp[i] == pivot:
                i += 1

        return lt, gt
              




if __name__ == "__main__":
    #sort = Sort('insertion')
    #sort = Sort('selection')
    #sort = Sort('shell')
    #sort = Sort('merge')
    #sort = Sort('quick')
    sort = Sort('quick_3')


    inp_list = [[2,1],
           [1,2],
           [3, 2,1],
           [1,2,3,4,5,6,7,8],
           [8,7,6,5,4,3,2,1],
           [1,2,2,3,4],
           [5,2,2,1,3],
           [10,5,2,7,2,1,3,5,6,2,4,8,9],
          ]

    for inp in inp_list:
        print 'Input = ', inp, sort.sort_fn, ':', sort(inp)

