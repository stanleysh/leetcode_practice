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

# -------------------------------------------------------
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

# Testing:
answer = add_two_numbers(l1_n1, l2_n1)
answer.listprint()

# -------------------------------------------------------
# Longest substring without repeating characters

def length_of_longest_substring(s):
    letter_dict = {}
    j = 0
    max_length = 0
    for i in range(len(s)):
        if s[i] in letter_dict and j < letter_dict[s[i]] + 1:
            j = letter_dict[s[i]] + 1
        letter_dict[s[i]] = i
        max_length = max(max_length, i - j + 1)

    return max_length

# Testing:
assert(length_of_longest_substring("abcabcbb")) == 3
assert(length_of_longest_substring("bbbbb")) == 1
assert(length_of_longest_substring("pwwkew")) == 3

# -------------------------------------------------------
# Reverse Integer:
def reverse(x):
    pop = 0
    rev = 0
    neg = x < 0
    if neg:
        x = -x
    while x != 0:
        pop = x % 10
        x = x // 10
        rev = rev * 10 + pop
    if neg:
        return -rev
    return rev

assert(reverse(-123)) == -321
assert(reverse(5142)) == 2415

# -------------------------------------------------------
# Interview camp questions:
# Sort subarray to sort whole array:

def sortSub(nums):
    start = 0
    end = 0
    for i in range(len(nums) - 1):
        if nums[i] == nums[i + 1] - 1:
            continue
        else:
            start = i + 1
            break

    for j in range(len(nums) - 1, 1, -1):
        if nums[j] == nums[j - 1] + 1:
            continue
        else:
            end = j - 1
            break
    
    return nums[start: end + 1]
        
assert(sortSub([1,2,4,5,3,5,6,7])) == [4,5,3]
assert(sortSub([1,3,5,2,6,4,7,8,9])) == [3,5,2,6,4]

# -------------------------------------------------------
# Dutch natinal flag problem
def dutchNationalFlag(nums, pivot):
    boundary = 0
    end_boundary = len(nums) -1
    i = 0
    while i <= end_boundary:
        if nums[i] < pivot:
            nums[boundary], nums[i] = nums[i], nums[boundary]
            boundary += 1
            i += 1
        elif nums[i] > pivot:
            nums[end_boundary], nums[i] = nums[i], nums[end_boundary]
            end_boundary -= 1
        else:
            i += 1
    
    return nums

assert(dutchNationalFlag([5,2,4,4,6,4,4,3], 4)) == [3, 2, 4, 4, 4, 4, 6, 5]

# -------------------------------------------------------
# Red white blue marbles: sort array so that red -> white -> blue
def redWhiteBlue(marbles):
    red_boundary = 0
    blue_boundary = len(marbles) - 1
    i = 0
    while i <= blue_boundary:
        if marbles[i] < 1:
            marbles[red_boundary], marbles[i] = marbles[i], marbles[red_boundary]
            red_boundary += 1
            i += 1
        elif marbles[i] > 1:
            marbles[blue_boundary], marbles[i] = marbles[i], marbles[blue_boundary]
            blue_boundary -= 1
        else:
            i += 1
    return marbles

assert(redWhiteBlue([0,2,1,2,0,1,2,0,1,2,1,2,1,0])) == [0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2]

# -------------------------------------------------------
# Kadane's algorithm, find max sum of subarray of an array
def kadanes(nums):
    result = nums[0]
    max_end_result = nums[0]
    for i in range(1, len(nums)):
        max_end_result = max(nums[i], max_end_result + nums[i])
        result = max(result, max_end_result)
    return result

assert(kadanes([-2,-3,4,-1,-2,1,5,-1])) == 7

# -------------------------------------------------------
# kadane's but return the indicies and not the result number
def kadanesIndicies(nums):
    result = nums[0]
    max_end_result = nums[0]
    start = 0
    end = 0
    for i in range(1, len(nums)):
        max_end_result = max(nums[i], max_end_result + nums[i])
        if max_end_result == nums[i]:
            start = i
        if max_end_result > result:
            result = max_end_result
            end = i
        
    return (start, end)

assert(kadanesIndicies([-2,-3,4,-1,-2,1,5,-1])) == (2,6)
assert(kadanesIndicies([1,2,-1,2,-3,2,-5])) == (0,3) 

# -------------------------------------------------------
# Sliding window, find subarray that sums ot target with sliding window
def slidingWindow(nums, target):
    start = 0
    end = 1
    while end < len(nums) + 1:
        if sum(nums[start:end]) < target:
            end += 1
        elif sum(nums[start:end]) > target:
            start += 1
        elif sum(nums[start:end]) == target:
            return nums[start:end]

assert(slidingWindow([5,3,1,7,6,4,2,3], 15)) == [6,4,2,3]
assert(slidingWindow([1,2,3,5,2], 8)) == [3,5]

# -------------------------------------------------------
# Given a string, find the longest substring with unique characters
def uniqueSubstring(s):
    i = 0
    j = 1
    start = 0
    end = 0
    while j < len(s):
        if s[j] not in s[i:j]:
            j += 1
        elif s[j] in s[i:j]:
            i += 1
        if j - i + 1 > end - start + 1:
            start = i
            end = j - 1
    return s[start:end + 1]
        
assert(uniqueSubstring('whatwhywher')) == 'ywher'


# Solved with dictionary, only looking for length not the actual string
def uniqueSubstringDict(s):
    letters_dict = {}
    j = 0
    max_length = 0
    for i in range(len(s)):
        if s[i] in letters_dict and j < letters_dict[s[i]] + 1:
            j = letters_dict[s[i]] + 1
        letters_dict[s[i]] = i
        max_length = max(max_length, i - j + 1)
    return max_length

assert(uniqueSubstringDict('whatwhywhere')) == 5