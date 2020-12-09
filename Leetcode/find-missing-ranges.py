from typing import List

class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:

        if not nums:
            if lower == upper:
                return [str(upper)]
            else:
                return [str(lower) + "->" + str(upper)]
            
        ranges = []

        for i, num in enumerate(nums):

            # edge case: start
            if i == 0:
                # Nothing missing
                if num == lower:
                    pass
                # One missing
                elif(num - 1 == lower):
                    ranges.append(str(lower))
                # Range missing
                else:
                    ranges.append(str(lower) + "->" + str(num - 1))

                if len(nums) > 1:
                    continue

            # common case
            # Something missing
            if len(nums) > 1 and nums[i - 1] != num - 1:
                # One missing
                if nums[i - 1] == num - 2:
                    ranges.append(str(num-1))
                # Range missing
                else:
                    ranges.append(str(nums[i-1]+1) + "->" + str(num-1))

            # edge case: end
            if i == len(nums) - 1:
                # Nothing missing
                if num == upper:
                    continue
                # One missing
                if num == upper - 1:
                    ranges.append(str(upper))
                # Range missing
                else:
                    ranges.append(str(num+1) + "->" + str(upper))
        
        return ranges


# Java solution
# class Solution {
#     public List<String> findMissingRanges(int[] nums, int lower, int upper) {
#         int n = nums.length;

#         if (n == 0) {
#             return Collections.singletonList(formatRange(lower, upper));
#         }

#         List<String> missingRanges = new ArrayList<>();

#         // Edge case 1) Missing ranges at the beginning
#         if (nums[0] > lower) {
#             missingRanges.add(formatRange(lower, nums[0] - 1));
#         }

#         // Missing ranges between array elements
#         for (int i = 1; i < n; ++i) {
#             if (nums[i] - nums[i - 1] > 1) {
#                 missingRanges.add(formatRange(nums[i - 1] + 1, nums[i] - 1));
#             }
#         }
        
#         // Edge case 2) Missing ranges at the end
#         if (nums[n - 1] < upper) {
#             missingRanges.add(formatRange(nums[n - 1] + 1, upper));
#         }

#         return missingRanges;
#     }

#     // formats range in the requested format
#     String formatRange(int lower, int upper) {
#         if (lower == upper) {
#             return String.valueOf(lower);
#         } else {
#             return lower + "->" + upper;
#         }
#     }
# }


if __name__ == "__main__":
    print(Solution().findMissingRanges([0,1,3,50,75], 0, 99))
    # print(Solution().findMissingRanges([-1], -1, 0))
    # print(Solution().findMissingRanges([1,2], 0, 9))