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

// Question 3, Longest substring without repeating character
function LongestSubstring(s) {
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

// Question 5, Longest palindromic substring
 function LongestPalindromicSubstring(s) {
    if (!s) 
        return "";
    let start = 0;
    let end = 0;
    let longest = 0;
    for (let i = 0; i < s.length; i++) {
        let odd_length = expand(s, i, i);
        let even_length = expand(s, i, i + 1);
        let current_longest = Math.max(odd_length, even_length);
        if (current_longest > longest) {
            longest = current_longest;
            start = i - (Math.floor((current_longest -1) / 2));
            end = i + Math.floor(current_longest / 2) ;
        }
    }

    function expand(string, left, right) {
        let l = left;
        let r = right;
        while (l >= 0 && r < string.length && (string[l] == string[r])) {
            l -= 1;
            r += 1;
        };
        return r - l - 1;
    };

    return s.slice(start, end + 1);
 }

//  Question 11, Container with most water
function WaterContainer(height) {
    let i = 0;
    let j = height.length - 1;
    let largest_area = 0;
    let current_shortest = 0;
    let current_area = 0
    while (i < j) {
        current_shortest = Math.min(height[i], height[j]);
        current_area = (j - i) * current_shortest;
        largest_area = Math.max(current_area, largest_area);
        if (height[i] <= height[j])
            i += 1;
        else
            j -= 1;
    };
    return largest_area;
}

 
//  Question 17, combinations of a phone
function PhoneCombination(digits) {
    const phone = 
    {   '2': ['a', 'b', 'c'], '3':['d','e','f'], 
        '4': ['g', 'h', 'i'], '5': ['j', 'k', 'l'], 
        '6':['m','n','o'], '7':['p','q','r','s'],
        '8':['t', 'u', 'v'], '9': ['w','x','y','z']
    };

    if (!digits)
        return [];

    function add_current_num(current_combo, rem_digits) {
        if (!rem_digits) {
        output.push(current_combo);
        return;
        };

        phone[rem_digits[0]].forEach(letter => {
            add_current_num(current_combo + letter, rem_digits.slice(1, rem_digits.length));
        });
    };

    let output = [];
    add_current_num("", digits);
    return output;
}
