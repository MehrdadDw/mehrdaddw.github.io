def convert(s: str, numRows: int) -> str:
        import math
        batch_size=numRows+max(numRows-2,0)
        index=0
        res={}
        for index,x in enumerate(s):
            # single one
            if (index%(batch_size)>numRows-1):
                partition=(numRows-1)-((index%(batch_size))-numRows+1)

                for i in range(numRows):
                    val=""
                    if (i==partition):
                        val=x
                    if i in res:
                            res[i].append(val)
                    else:
                            res[i]=val

            else:
                partition=(index%(batch_size))
                
                if partition in res:
                        res[partition].append(x)
                else:
                        res[partition]=[x]
        resut=""
        for i in range(numRows):
            if i in res:
                resut+=("".join(res[i]))

        return resut
convert("PAYPALISHIRING",4)

# PAHNAPLSIIGYIR 
# PAHNAPLSIIGYIR
