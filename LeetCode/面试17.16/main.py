
nums = [2,1,4,5,3,1,1,3]

m = [0 for i in range(-3, 10000)]
        #print(m[-2])
for i in range(len(nums)):
    m[i] = max(m[i-1], m[i-2] + nums[i])
print(m)
