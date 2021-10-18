def isMatch( s: str, p: str) -> bool:
        s_index=0
        index=0
        for char in p:
            #not last
            if (index!=len(p)-1):
                if (p[index+1]=='*'):
                    if (p[index]!='.'):
                        while (s[s_index]==p[index]):
                            s_index+=1
                            if (s_index>=len(s)):
                                return True
                    else:
                        if (index+1==len(p)-1):
                            return True
                        else:
                            while (s_index<=len(s)-1 and s[s_index]!=p[index+2]):
                                s_index+=1

                    index+=1
                else:
                    if (s[s_index]==p[index] or (p[index]=='.')):
                        s_index+=1
                    else:
                        return False
                if (s_index>=len(s) ):
                    if (index>=len(p)):
                        return True
                    else:
                        return False
            else:
                if (s[s_index]!=p[index] and (p[index]!='.')): 
                    return False
                else:
                    s_index+=1
            index+=1
            if (index>len(p)-1):
                break
        if (s_index<len(s)):
            return False

        return True
print(isMatch("ab",
".*c"
))