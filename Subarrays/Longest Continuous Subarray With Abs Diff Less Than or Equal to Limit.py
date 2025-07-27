#Attempt for this subarray problem (Works but is too time intensive)
def longestSubarray(self, nums: List[int], limit: int) -> int:
    def FindMaxAbsDiff(n):
        return max(n) - min(n)
    if FindMaxAbsDiff(nums) <= limit:
        return len(nums)
    maxAbsDiff = 1
    i = 0
    j = 2
    while j <= len(nums):
        e = FindMaxAbsDiff(nums[i:j])
        if e <= limit:
            maxAbsDiff = j-i
            j += 1
            continue
        i += 1
        j += 1
    return maxAbsDiff