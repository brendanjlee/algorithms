class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        last = m + n - 1
        
        # start loop from the back
        # len(num1) = m + n
        # len(num2) = n
        while m > 0 and n > 0:
          if nums1[m - 1] < nums2[n - 1]:
            nums1[last] = nums2[n - 1]
            n -= 1
          else:
            # send the (m-1)th element of nums1 to nums1[last]
            nums1[last] = nums1[m - 1]
            m -= 1
          last -= 1

       # edge case: left over number in beginning
       while n > 0:
        nums1[last] = nums2[n]
        n -= 1
        last -= 1
