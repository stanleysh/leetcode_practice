# linked list nodes and other classes that will be used for leetcode:
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def listprint(self):
        printval = self
        while printval != None:
            print(printval.val)
            printval = printval.next

# Two sum:
def two_sum(nums, target):
    for i in range(len(nums)):
        solution = target - nums[i]
        if solution in nums and nums.index(solution) != i:
            return [i, nums.index(solution)]

sum_array = [2,4,6,8,1,3,5]

# test cases:
assert(two_sum(sum_array, 14)) == [2,3]
assert(two_sum(sum_array, 17)) == None

# -------------------------------------------------------

# Adding Two Numbers:
def add_two_numbers(l1, l2):
    dummy = ListNode(None)
    p = l1
    q = l2
    current = dummy
    carry = 0
    while p != None or q != None:
        x = p.val if p != None else 0
        y = q.val if q != None else 0
        new_sum = carry + x + y
        carry = new_sum // 10
        current.next = ListNode(new_sum % 10)
        current = current.next
        if p != None:
            p = p.next
        if q != None:
            q = q.next
    if carry > 0:
        current.next = ListNode(carry)
    return dummy.next

l1_n1 = ListNode(2)
l1_n2 = ListNode(4)
l1_n3 = ListNode(3)
l1_n1.next = l1_n2
l1_n2.next = l1_n3

l2_n1 = ListNode(5)
l2_n2 = ListNode(6)
l2_n3 = ListNode(4)
l2_n1.next = l2_n2
l2_n2.next = l2_n3

answer = add_two_numbers(l1_n1, l2_n1)
answer.listprint()

# -------------------------------------------------------
