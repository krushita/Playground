# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def createListFromArr(self, arr):
        head = ListNode(0)
        p = head
        for k in range(len(arr)):
            p.next = ListNode(arr[k])
            p = p.next
        return head.next

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        p1 = l1
        p2 = l2
        head = ListNode(0)
        p = head

        carry = 0
        while p1 or p2 or carry:
            sum = carry
            if p1:
                sum += p1.val
                p1 = p1.next
            if p2:
                sum += p2.val
                p2 = p2.next
            carry = sum/10
            sum = sum%10
            p.next = ListNode(sum)
            p = p.next

        return head.next

if __name__ == "__main__":
    sol = Solution()

    l1 = sol.createListFromArr([1,6,0,3,3,6,7,2,0,1])
    l2 = sol.createListFromArr([6,3,0,8,9,6,6,9,6,1])
    l3 = sol.addTwoNumbers(l1, l2)
    out = []

    p = l3
    while p:
        out.append(p.val)
        p = p.next
    print "Sum l3 = {}".format(out)

