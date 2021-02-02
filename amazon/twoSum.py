#two sum using hashing done in O(n)
def twoSum(nums, target):
    d = {}
    for i, n in enumerate(nums):
        m = target - n
        if m in d:
            return [d[m], i]
        else:
            d[n] = i
print(twoSum([1,2,4,6],5))
