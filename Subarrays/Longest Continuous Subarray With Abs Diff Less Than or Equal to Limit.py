#Attempt for this subarray problem (Works but is too time intensive)
def longestSubarray(nums, limit) -> int:
    if max(nums) - min(nums) <= limit:
        return len(nums)
    maxAbsDiff = 1
    i = 0
    j = 2
    while j <= len(nums):
        e = max(nums[i:j]) - min(nums[i:j])
        if e <= limit:
            maxAbsDiff = j-i
            j += 1
            continue
        i += 1
        j += 1
    return maxAbsDiff