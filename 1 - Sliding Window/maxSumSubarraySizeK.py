"""
You are given an integer array nums and an integer k. You want to find a subsequence of nums of length k that 
has the largest sum.

Return any such subsequence as an integer array of length k.

A subsequence is an array that can be derived from another array by deleting some or no elements without
changing the order of the remaining elements.

Example 1:

Input: nums = [2,1,3,3], k = 2
Output: [3,3]

Explanation:
The subsequence has the largest sum of 3 + 3 = 6.
Example 2:

Input: nums = [-1,-2,3,4], k = 3
Output: [-1,3,4]

Explanation: 
The subsequence has the largest sum of -1 + 3 + 4 = 6.
Example 3:

Input: nums = [3,4,3,3], k = 2
Output: [3,4]

Explanation:
The subsequence has the largest sum of 3 + 4 = 7. 
Another possible subsequence is [4, 3].

personal test case:
input: nums = [1,3] k = 3
output: err 

input nums = [2,1,-2,4] k = 2
output: 2, 4
"""
# what would be the naiive solution to this?

# naive solution
def maxSubsequence(nums, k):
    indexes = {} # {number: index} , n

    # fill in index
    for i in range(len(nums)):
        indexes[nums[i]] = i
    print('indexes: {}'.format(indexes))
    
    # go backwards in sorted array
    s = sorted(nums)
    s = s[(len(nums)-k):]
    print('sorted: {}'.format(s))
    
    # get index of k biggest numbers
    maxnumsidx = []
    for num in s:
        maxnumsidx.append(indexes[num])
    print('maxnumidx: {}'.format(maxnumsidx))



    res = []
    for idx in sorted(maxnumsidx):
        res.append(nums[idx])
    
    return res


nums = [50, -75]
k = 2

print(maxSubsequence(nums, k))