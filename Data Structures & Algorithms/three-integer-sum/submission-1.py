class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() # Sort list
        tripletList = []

        # Loop through using index i and a = nums[i]
        for i, a in enumerate(nums):
            if a > 0: # If a is positive then all numbers that come after it are also positive
                break

            if i > 0 and a == nums[i - 1]: # If we encountered a duplicate, skip this iteration
                continue

            bottom = i + 1
            top = len(nums) - 1
            while bottom < top:
                threeSum = a + nums[bottom] + nums[top]
                if threeSum > 0: # If sum is too big, move top pointer down
                    top -= 1
                elif threeSum < 0: # If sum is too small, move bottom pointer up
                    bottom += 1
                else:
                    tripletList.append([a, nums[bottom], nums[top]]) # Add to list
                    # Move both pointers in their designated direction
                    bottom += 1
                    top -= 1
                    while nums[bottom] == nums[bottom - 1] and bottom < top: # Ensure we are not using duplicates
                        bottom += 1
        return tripletList