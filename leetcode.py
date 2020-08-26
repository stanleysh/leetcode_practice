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

# -------------------------------------------------------
# Leetcode question, also appears in interview camp
# Solved with dictionary, only looking for length not the actual string
def uniqueSubstringDict(s):
    letters_dict = {}
    j = 0
    max_length = 0
    for i in range(len(s)):
        if s[i] in letters_dict and j < letters_dict[s[i]] + 1:
            j = letters_dict[s[i]] + 1
        letters_dict[s[i]] = i
        if max_length < i -j + 1:
            start = j
            end = i
            max_length = i - j + 1
    return s[start:end + 1]

print(uniqueSubstringDict('whatwhywhere'))

# -------------------------------------------------------
# Prefix sums, finds part of array that gives 0
def prefixSum(nums):
    sum_dict = {}
    start = 0
    end = 0
    current_sum = 0
    for i in range(len(nums)):
        current_sum += nums[i]
        if current_sum in sum_dict:
            start = sum_dict[current_sum] + 1
            end = i
            break
        sum_dict[current_sum] = i
    
    return nums[start:end + 1]

assert(prefixSum([2,4,-2,1,-3,5,-3])) == [4,-2,1,-3]

def prefixSumWithTarget(nums, target):
    sum_dict = {}
    start = 0
    end = 0
    current_sum = 0
    for i in range(len(nums)):
        current_sum += nums[i]
        if current_sum == target:
            return nums[0:i + 1]
        if (current_sum - target) in sum_dict:
            start = sum_dict[current_sum - target] + 1
            end = i
            break
        sum_dict[current_sum] = i
    
    return nums[start:end + 1]

assert(prefixSumWithTarget([2,4,-2,1,-3,5,-3], 5)) == [2,4,-2,1]
assert(prefixSumWithTarget([2,4,-2,1,-3,5,-3], 3)) == [4,-2,1]

# -------------------------------------------------------
# Binary search
def binarySearch(nums, target):
    low = 0
    high = len(nums) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if nums[mid] > target:
            high = mid - 1
        elif nums[mid] < target:
            low = mid + 1
        else:
            return mid
    
    return -1

assert(binarySearch([1,2,4,7,8.9], 2)) == 1

def binarySearchDup(nums, target):
    low = 0
    high = len(nums) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if nums[mid] > target or (nums[mid] == target and mid > 0 and nums[mid-1] == target):
            high = mid - 1
        elif nums[mid] < target:
            low = mid + 1
        else:
            return mid
    
    return -1

assert(binarySearchDup([1,1,2,2,2,3,4,5,6], 2)) == 2

# -------------------------------------------------------
# Binary search closest (number doesn't exist but we find the two closest indicies)
def binarySearchClosest(nums, target):
    low = 0
    high = len(nums) - 1
    low_close = 0
    high_close = len(nums) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if nums[mid] > target:
            high = mid - 1
            high_close = high
        elif nums[mid] < target:
            low = mid + 1
            low_close = low
        else:
            return mid
    
    return high_close

assert(binarySearchClosest([1,1,2,2,2,5,5,6], 4)) == 4


# -------------------------------------------------------
# Combination with length x
def array_combos(nums, x):
    if nums is None or len(nums) == 0 or x > len(nums):
        return

    def addComboHelper(buffer, startIndex, bufferIndex):
        if bufferIndex == len(buffer):
            output.append(buffer[:])
            return

        if startIndex == len(nums):
            return

        for i in range(startIndex, len(nums)):
            buffer[bufferIndex] = nums[i]
            addComboHelper(buffer, i + 1, bufferIndex + 1)
        

    output = []
    addComboHelper([0]*x, 0, 0)
    return output
    
assert(array_combos([1,2,3,4,5], 3)) == [[1, 2, 3], [1, 2, 4], [1, 2, 5], [1, 3, 4], [1, 3, 5], [1, 4, 5], [2, 3, 4], [2, 3, 5], [2, 4, 5], [3, 4, 5]]

# -------------------------------------------------------
# Combinations of phone number
def phone_number(digits):
    phone = {'2': ['a', 'b', 'c'],
                 '3': ['d', 'e', 'f'],
                 '4': ['g', 'h', 'i'],
                 '5': ['j', 'k', 'l'],
                 '6': ['m', 'n', 'o'],
                 '7': ['p', 'q', 'r', 's'],
                 '8': ['t', 'u', 'v'],
                 '9': ['w', 'x', 'y', 'z']}
    
    def add_combo(current, current_digits):
        if current_digits == '' or len(current_digits) == 0:
            output.append(current)
            return
        
        for letter in phone[current_digits[0]]:
            add_combo(current + letter, current_digits[1:])

        return

    output = []
    add_combo('', digits)
    return output

assert(phone_number('23')) == ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']

# -------------------------------------------------------
# Target amount using combos
def combo_target(nums, target):

    def add_num(current_combo, index):
        if sum(current_combo) == target:
            output.append(current_combo[:])
            return
        
        if sum(current_combo) > target:
            return

        for i in range(index, len(nums)):
            current_combo.append(nums[i])
            add_num(current_combo, i)
            current_combo.pop()

    
    output = []
    add_num([], 0)
    return output

assert(combo_target([1,2,5], 5))  == [[1, 1, 1, 1, 1], [1, 1, 1, 2], [1, 2, 2], [5]]


# -------------------------------------------------------
# Backtracking max problem
'''
def doesPathExists(maze):
    if len(maze) == 0 or maze is None:
        return False

    memo = [[0] * len(maze[0])] * len(maze)
    return pathExists(maze, 0, 0, memo)

def pathExists(maze, i, j, memo):
    if oob(maze, i, j) or a[i][j] == 1:
        return False

    if i == len(maze) - 1 and j == len(maze[0] -1):
        return True

    

def outOfBounds(maze, i, j):
    return i < 0 or i  >= len(maze) or j < 0 or j >= len(maze[0])

doesPathExists([[0,0,0,0],[0,0,0,0],[0,0,0,0]])
'''

# -------------------------------------------------------
# Stack with max and a 0(1)
class StackWithMax:
    def __init__(self):
        self.main = []
        self.max_stack = []
    
    def push(self, a):
        self.main.append(a)
        if len(self.max_stack) == 0:
            self.max_stack.append(a)
            return
        if (a > self.max_stack[-1]):
            self.max_stack.append(a)
        else:
            self.max_stack.append(self.max_stack[-1])

    def getMax(self):
        return self.max_stack[-1]
    
    def pop(self):
        self.main.pop()
        self.max_stack.pop()


x = StackWithMax()
x.push(5)
x.push(1)
x.push(8)
print(x.getMax())

# -------------------------------------------------------
# Queue with two stacks
class Queue:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def __str__(self):
        if not self.s2:
            self.flushToS2()
        return str(self.s2)

    def enqueue(self, a):
        self.s1.append(a)        

    def dequeue(self):
        if len(self.s2) == 0:
            self.flushToS2()

        return self.s2.pop()

    def flushToS2(self):
        while self.s1:
            self.s2.append(self.s1.pop())

y = Queue()
y.enqueue(1)
y.enqueue(2)
y.enqueue(3)
# print(y.dequeue())
print(y)

# -------------------------------------------------------
# longest increasing subsequence
def longestIncreasingSubsequence(nums):
    if len(nums) == 0:
        return 0

    longest = [0] * len(nums)
    result = 1
    for i in range(len(nums)):
        longest[i] = 1
        for j in range(0, i):
            if (nums[j] < nums[i]):
                longest[i] = max(longest[i], longest[j] + 1)

        result = max(result, longest[i])
    return result

print(longestIncreasingSubsequence([1,3,2,5,3,5,6]))

# -------------------------------------------------------
#46 Permutations
def permute(nums): 
    if not nums:
        return []
    
    def add_num(current_array):
        if current_array and len(current_array) == len(nums):
            output.append(current_array[:])
            return
        
        for num in nums:
            if current_array:
                if num in current_array:
                    continue
            current.append(num)
            add_num(current)
            current.pop()
    
    output = []
    current = []
    add_num(current)
    return output

# -------------------------------------------------------
# 47 Permutations 2
