people = ["Mary","John","Emma"]
heights = [180,165,170]

def sortPeople(names, heights):
    
    d ={} 
    dp = heights[:]
    n = len(heights)
    for i in range(n):
        for j in range(0, n-i-1):
            if heights[j+1] > heights[j]:
                heights[j+1], heights[j] = heights[j], heights[j+1]


    for k in heights:
        i = dp.index(k)
        d[names[i]] = k
    print(d.keys())
    return list(d.keys())
    
    
print(sortPeople(names=people, heights = heights))