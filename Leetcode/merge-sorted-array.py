class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.

        nums 1 is length m + n
        """

        idxp = len(nums1) - 1
        idx1 = m - 1
        idx2 = n - 1

        while idx1 >= 0 and idx2 >= 0:
            if nums1[idx1] > nums2[idx2]:
                nums1[idxp] = nums1[idx1]
                idx1 -= 1
            else:
                nums1[idxp] = nums2[idx2]
                idx2 -= 1

            idxp -=1
        
        while idx2 >= 0:
            nums1[idxp] = nums2[idx2]
            idx2 -= 1
            idxp -= 1
        
        return
    
in1 = [1,2,3,0,0,0]
in2 = [2,5,6]
m = 3
n = 3
print(in1)
Solution().merge(in1, m, in2, n)
print(in1)



        
