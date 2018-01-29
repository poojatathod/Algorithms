inputSequence=[50,55,51,52,53,54,55]
longSubSeqLen=[]
check=[]

for i in range (len(inputSequence)):
    longSubSeqLen.append(1)

for i in range (len(inputSequence)):
    if (i==0):
        check.append(0)

    else:
        for j in range (0,i):
            if inputSequence[j]<inputSequence[i]:
                check.append(longSubSeqLen[j])
            else:
                check.append(0)
    var=0
    var=1+max(check)
    check=[]
    longSubSeqLen[i]=var

print max(longSubSeqLen)
