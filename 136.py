def singleNumber(nums):
    d = {}
    for num in nums:
        if num not in d:
            d[num] = 1
        else:
            d[num] += 1
        
    for num, count in d.items():
        if count == 1:
            return num