def countTriplets(arr, r):
    max1=max(arr)
    res=0
    for ind1 in range(len(arr)):
        for ind2 in range(ind1+1,len(arr)):

            if arr[ind1]*r*r>max1:
                break
            b=arr[ind1]*r
            if arr[ind2]!=b:
                continue
            for ind3 in range(ind2+1,len(arr)):
                if (arr[ind1]*r*r==arr[ind3]):

                    res+=1
        


    return res

a=[
 1,3,9,9,27,81

]

print(countTriplets(a,3))
1339347780085
8040276546818

