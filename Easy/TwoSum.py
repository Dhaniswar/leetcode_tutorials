""" 

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]


"""




# Using hash map (which is one of the best way)



class Solution(object):
    def twoSum(self, nums, target):
        num_map = {}  # Use a DICTIONARY, not a list
        
        for i, num in enumerate(nums):
            complement = target - num
            
            # Check if complement exists in the dictionary KEYS
            if complement in num_map:
                return [num_map[complement], i]  # Return the stored index and current index
            
            # Store current number as KEY and its index as VALUE
            num_map[num] = i
        
        return []  # Return empty if no solution found

# Test the function
n = int(input("Enter the total element of length: "))
nums = []
for num in range(n):
    element = int(input(f"Enter {num} index element: "))
    nums.append(element)

target = int(input("Please enter the target: "))
s1 = Solution()

result = s1.twoSum(nums, target)
print("Output: ", result)





""" 
Another way but this is worst practice cause it has worst time complexcity


class Solution(object):
    def twoSum(self, nums, target):
        
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                
                if nums[i] + nums[j] == target:
                    return [i, j]
        
        return []  # Return empty if no solution found

# Test the function
n = int(input("Enter the total element of length: "))
nums = []
for num in range(n):
    element = int(input(f"Enter {num} index element: "))
    nums.append(element)

target = int(input("Please enter the target: "))
s1 = Solution()

result = s1.twoSum(nums, target)
print("Output: ", result)


"""



