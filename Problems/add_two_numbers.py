# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverse_list(self, l):
        prev = None
        curr = l
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev

    def getInt(self, l):
        ptr = l
        power = 0
        num = 0
        while (ptr):
            num += (ptr.val * pow(10, power))
            power += 1
            ptr = ptr.next
        return num

    def createListFromInt(self, num):
        digits = []
        # Create list of digits starting with last digit first
        while num != 0:
            digits.append(num % 10)
            num = num/10
        head = None

        if not digits:
            digits.append(0)
        # Add digits to list
        for k in range(len(digits)):
            node = ListNode(digits[k])
            node.next = head
            head = node
        return head


    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        num1 = 0
        num2 = 0
        sum = self.getInt(l1) + self.getInt(l2)
        l3 = self.createListFromInt(sum)
        out = []

        rev_l3 = self.reverse_list(l3)
        ptr = rev_l3
        while ptr:
            out.append(ptr.val)
            ptr = ptr.next
        return out


if __name__ == "__main__":
    sol = Solution()

    l1 = sol.createListFromInt(1603367201)
    l2 = sol.createListFromInt(6308966961)
    print "l1 = {}, l2 = {}".format(l1,l2)
    out = sol.addTwoNumbers(l1, l2)
    print "Sum l3 = {}".format(out)

