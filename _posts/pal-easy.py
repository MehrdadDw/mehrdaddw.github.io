def palindromeIndex(s):
    res=0
    faultes=False
    faulties=(0,0)
    for index,c in enumerate(s):

        
        if (s[-1-index]!=c):
            faultes=True
            faulties=(index,-1-index) 
            break
    print(faulties)
    s=s[0 : faulties[0] : ] + s[faulties[0] + 1 : :]
    if (faultes):
        for index,c in enumerate(s):
            
            if (s[-1-index]!=c):
                return len(s)+(faulties[1])+1
        return faulties[0]
    return -1       
    # Write your code here
s1="hgygsvlfcwnswtuhmyaljkqlqjjqlqkjlaymhutwsnwcwflvsgygh"
print(len(s1))
print(palindromeIndex(s1))