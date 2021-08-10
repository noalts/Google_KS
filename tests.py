def twoSum(nums, target):
        for i in nums:
            if target - i in nums and nums.index(i) > nums.index(target-i):
                print([nums.index(i),nums.index(target-i)])
                break
            else:
                i +=1

twoSum([3,3],6)