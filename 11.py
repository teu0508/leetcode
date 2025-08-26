test = [2,3,4,5,18,17,6]


def maxArea(height) -> int: 
    
    l, r = 0, len(height)-1
    lm = l
    rm = r
    curr = min(height[l], height[r])*(r-l)
    m = curr

    while l < r:
        if height[l] < height[r]:
            l = l + 1
        else:
            r = r - 1
        curr = min(height[l], height[r])*(r-l)
        m = max(m, curr)

    return m
        
print(maxArea(test))