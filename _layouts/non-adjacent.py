def maxSubsetSum(arr):
    l=len(arr)
    if l==0:
        return 0
    elif (l==1):
        return max(arr[0],0)
    else:
        ans=[]
        for i in range(len(arr)):
            # choose ith
            left_arr,right_arr=[],[]
            if (i-1>=0):
                left_arr=arr[:i-1]
            if (i+2<=l-1):
                right_arr=arr[i+2:]
            l1=maxSubsetSum(left_arr)
            r1=maxSubsetSum(right_arr)
            ans.append(arr[i]+l1+r1)
    return max(ans)

print(maxSubsetSum([3,7,4,6,5]))
