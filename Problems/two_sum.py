#Given an array of integers, return indices of the two numbers such that they add up to a specific target.
#You may assume that each input would have exactly one solution, and you may not use the same element twice.
#Given nums = [2, 7, 11, 15], target = 9,
#Because nums[0] + nums[1] = 2 + 7 = 9,
#return [0, 1].

# Go through input array, find current elemen't sum_partner, and add it to a dict with current index as value.
# If current element already exists in dict, then return current index and value for current element key in dict.
def two_sum(input, target):
    num = len(input)
    sum_pair = {}
    out = []
    for i in range(num):
        sum_partner = target - input[i]

        if input[i] in sum_pair:
            out.append(i)
            out.append(sum_pair[input[i]])
            break
        else:
            sum_pair[sum_partner] = i

    return out

if __name__ == "__main__":
    input = [1,2,3]
    out = two_sum(input, 5)
    print "two_sum = ", out

    input = [1,1,1]
    out = two_sum(input, 3)
    print "two_sum = ", out

