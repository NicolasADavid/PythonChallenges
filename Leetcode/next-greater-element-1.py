class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        ans = []
        
        for num in nums1:
            index = nums2.index(num)
            nextGreater = -1
            for i in range(index, len(nums2)):
                if nums2[i] > num:
                    nextGreater = nums2[i]
                    break
            
            ans.append(nextGreater)
        
        return ans