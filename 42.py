def trap(height) -> int:
    '''
    O(n) time complexity and space complexity
    '''
    
    l, r= [height[0]], [height[-1]]
    rev = height[::-1]
    
    for i in range(1, len(height)):
        l.append(max(height[i], l[i-1]))
    for j in range(1, len(rev)):
        r.append(max(rev[j], r[j-1]))    
    r = r[::-1]
    
    print(l)
    print(r)

    
    sum = 0
    for k in range(1, len(height)-1):
        curr = min(l[k], r[k]) - height[k]
        if curr > 0:
            sum += curr
        
        print("index ", k, "can hold ", curr, "sq of water")
            
    return sum
        
height1 = [0,1,0,2,1,0,1,3,2,1,2,1]      
height2 = [4,2,0,3,2,5]


def trap_2(height):
    '''
    O(n) time complexity 
    O(1) space complexity
    '''
    
    l, r = 0, len(height)-1
    s = 0
    maxL = height[l]
    maxR = height[r]
    curr = 0
    while l < r:
        if height[l] < height[r]:
            l += 1
            h = height[l] 

        else:
            r -= 1
            h = height[r] 

         
        curr = min(maxR, maxL) - h 
        s += max(0, curr)
            
        maxL = max(maxL, height[l])
        maxR = max(maxR, height[r])
    
    return s

print(trap_2(height1))
