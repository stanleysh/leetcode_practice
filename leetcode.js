// Question 1, two sum
function TwoSum(nums, target) {
    for (let i = 0; i < nums.length; i++) {
        solution = nums[i] - target
        if (nums.includes(solution) && nums.indexOf(solution) != i) {
            return [i, nums.indexOf(solution)]
        }
    }
}

// Question 2, add two linkedlist
function AddTwoNums(l1, l2) {
    let s = new ListNode('dummy');
    let current = s;
    let carry = 0;
    
    while (l1 || l2 || carry) {

        current.next = new ListNode();
        current = current.next;

        current.val = (l1 ? l1.val : 0) + (l2 ? l2.val : 0) + carry;

        // True == 1, so you can add
        carry = current.val >= 10;
        current.val %= 10;

        if (l1) l1 = l1.next;

        if (l2) l2 = l2.next;
    }
    
    return s.next;
}

// Questions 3, Longest substring without repeating character
function LongestSubstring(string) {
    let letters_dict = {};
    let longest = 0;
    let j = 0;
    for (let i = 0; i < s.length; i++) {
        if (s[i] in letters_dict && j < letters_dict[s[i]] + 1)
            j = letters_dict[s[i]] + 1
        letters_dict[s[i]] = i;
        longest = Math.max(longest, i - j + 1);
    };
    return longest;
}
