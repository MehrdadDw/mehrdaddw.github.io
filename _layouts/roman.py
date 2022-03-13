def intToRoman(num: int) -> str:
        l=len(str(num))
        digits=["I","V","X","L","C","D","M"]
        res=[]
        
        counter=0
        while num>0:
            current=num%10
            if (current<=3):
                res.append(digits[counter])
            elif (current==4):
                res.append(digits[counter]+digits[counter+1])

            elif (current<=8):
                c=digits[counter+1]
                for i in range(current-5):
                    c+=digits[counter]

                res.append(c)                            
            elif (current==9):
                res.append(digits[counter]+digits[counter+2])        
            elif (current==10):
                res.append(digits[counter+2])    
                
            num//=10
            counter+=2
        return "".join(res[::-1])
print(intToRoman(999))