#Attempt for this subarray problem (Works but is too time intensive)
def longestSubarray(nums, limit):
        maxAbsDiffLength = 1
        i = 0
        j = 1
        max1 = max(nums[i:j])
        min1 = min(nums[i:j])
        while j < len(nums):
            e = max1 - min1
            print(nums[i:j])
            print("MaxAbsDiff: ", e)
            if e <= limit:
                maxAbsDiffLength = j-i+1
                j += 1
                if j >= len(nums):
                    return maxAbsDiffLength
                if nums[j] > max1:
                    max1 = nums[j]
                if nums[j] < min1:
                    min1 = nums[j]
                continue
            i += 1
            j += 1
            if j >= len(nums):
                break
            if nums[i-1] == min1:
                min1 = min(nums[i:j])
            if nums[j] < min1:
                min1 = nums[j]
            if nums[i-1] == max1:
                max1 = max(nums[i:j])
            if nums[j] > max1:
                max1 = nums[j]
            print(nums[i:j])
        return maxAbsDiffLength


print(longestSubarray([8, 2, 4, 7], 4))