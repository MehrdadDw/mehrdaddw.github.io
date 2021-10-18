def twoSum( nums, target) :
        d={}
        for ind,x in enumerate(nums):
            if (x not in d):
                d[x]=[ind]
            else:
                d[x].append(ind)
        for x in d:
            if x==(target-x):
                if len(d[x])>1:
                    return (d[x][0],d[x][1])
                else:
                    continue
                
            
            elif (target-x) in d :
                return (d[x][0],d[target-x][0])
        return []

print(twoSum([3,2,4],6))