#!/usr/bin/env python3

# addition
print("addition start")
n = 1
sum = 0

while n < 101:
    print(n)
    sum = sum + n
    n += 1

print(sum)


# factorial
print("factorial start")
f = 1
sumF = 1

while f < 10:
    f += 1
    sumF = sumF * f

print(sumF)

# for loop #1
print("for loop #1 start")
listF = [101,2,15,22,95,33,2,27,72,15,52]
 
for item in listF:
    if (item%2 ==0):
        print(item)

# for loop #2
print("for loop #2 start")

listF = [101,2,15,22,95,33,2,27,72,15,52]
 
sortF = sorted(listF)
evenS = 0
oddS = 0

for item in sortF:
    print(item)
    if (item%2 == 0):
        evenS = evenS + item
    else:
        oddS = oddS + item

print(f'Sum of even numbers: {evenS}\nSum of odds: {oddS}')

# range()
print("range() start")

for num in range(101):
    if num > 0:
        print(num)
    
# list comprehension
print("list comprehension start")

listComp = [x for x in range(100)]
print(listComp)

listComp100 = [1+x for x in range(100)]
print(listComp100)

#User input, for loops, and Range
print("User input, for loops, and Range start")
import sys

inMin = int(sys.argv[1])
inMax = int(sys.argv[2])

n = inMin

while n < (inMax+1):
    print(n)
    n += 1

print("Comprehension:")

nComp = [x for x in range(inMax+1) if (x >= inMin)]
print(nComp)

print("Comprehension (odd only):")
nComp = [x for x in range(inMax+1) if (x >= inMin) and (x%2 != 0)]
print(nComp)


# Lists, for loops, and strings
print("Lists, for loops, and strings start")
listS = ['ATGCCCGGCCCGGC','GCGTGCTAGCAATACGATAAACCGG', 'ATATATATCGAT','ATGGGCCC']
index = 0
for item in listS:
    print(f'{index}\t{len(item)}\t{item}')
    index += 1

print("after sorting:")

print(sorted(listS,key=len,reverse=True))

# shuffle
import random
print("shuffle start")
seq = 'GCGTGCTAGCAATACGATAAACCGG'
seqList = list(seq)
#print(seqList)
temp = ''

for i in range(len(seqList)):
    #print(i)
    j = random.randrange(len(seqList)) 
    k = random.randrange(len(seqList)) 
    #print(j)
    print(f'old {seqList[j]} and {seqList[k]}')
    temp = seqList[k]
    seqList[k] = seqList[j] 
    seqList[j] = temp
    print(f'new {seqList[j]} and {seqList[k]}')

seqOut = "".join(seqList)
print(seqOut)

# How similar are two sequences
print("How similar are two sequences start")
align1 = "CCCGCCCCCAAAGTCCC----------CCAAATCTTGCAGTTCCCTCCTAAATCCTCCCC"
align2 = "ACTGGAGTTTAAGTACCCCCTTTTCCATTTTTTCCTGAAGTCGTGGGCAGGGCGCAAGGT"

align1List = list(align1)
align2List = list(align2)

same = 0

for i in range(len(align1List)):
    if align1List[i] == align2List[i]:
        same +=1

print(f'{same/len(align1List)} similarity')

# new Restriction Fragments script
print("new Restriction Fragments start")
dna = "GATGGGATTGGGGTTTTCCCCTCCCATGTGCTCAAGACTGGCGCTAAAAGTTTTGAGCTTCTCAAAAGTCTAGAGCCACCGTCCAGGGAGCAGGTAGCTGCTGGGCTCCGGGGACACTTTGCGTTCGGGCTGGGAGCGTGCTTTCCACGACGGTGACACGCTTCCCTGGATTGGCAGCCAGACTGCCTTCCGGGTCACTGCCATGGAGGAGCCGCAGTCAGATCCTAGCGTCGAGCCCCCTCTGAGTCAGGAAACATTTTCAGACCTATGGAAACTACTTCCTGAAAACAACGTTCTGTCCCCCTTGCCGTCCCAAGCAATGGATGATTTGATGCTGTCCCCGGACGATATTGAACAATGGTTCACTGAAGACCCAGGTCCAGATGAAGCTCCCAGAATTCGCCAGAGGCTGCTCCCCCCGTGGCCCCTGCACCAGCAGCTCCTACACCGGCGGCCCCTGCACCAGCCCCCTCCTGGCCCCTGTCATCTTCTGTCCCTTCCCAGAAAACCTACCAGGGCAGCTACGGTTTCCGTCTGGGCTTCTTGCATTCTGGGACAGCCAAGTCTGTGACTTGCACGTACTCCCCTGCCCTCAACAAGATGTTTTGCCAACTGGCCAAGACCTGCCCTGTGCAGCTGTGGGTTGATTCCACACCCCCGCCCGGCACCCGCGTCCGCGCCATGGCCATCTACAAGCAGTCACAGCACATGACGGAGGTTGTGAGGCGCTGCCCCCACCATGAGCGCTGCTCAGATAGCGATGGTCTGGCCCCTCCTCAGCATCTTATCCGAGTGGAAGGAAATTTGCGTGTGGAGTATTTGGATGACAGAAACACTTTTCGTGGGGTTTTCCCCTCCCATGTGCTCAAGACTGGCGCTAAAAGTTTTGAGCTTCTCAAAAGTCTAGAGCCACCGTCCAGGGAGCAGGTAGCTGCTGGGCTCCGGGGACACTTTGCGTTCGGGCTGGGAGCGTGCTTTCCACGACGGTGACACGCTTCCCTGGATTGGCAGCCAGACTGCCTTCCGGGTCACTGCCATGGAGGAGCCGCAGTCAGATCCTAGCGTCGAGCCCCCTCTGAGTCAGGAAACATTTTCAGACCTATGGAAACTACTTCCTGAAAACAACGTTCTGTCCCCCTTGCCGTCCCAAGCAATGGATGATTTGATGCTGTCCCCGGACGATATTGAACAATGGTTCACTGAAGACCCAGGTCCAGATGAAGCTCCCAGAATTCGCCAGAGGCTGCTCCCCCCGTGGCCCCTGCACCAGCAGCTCCTACACCGGCGGCCCCTGCACCAGCCCCCTCCTGGCCCCTGTCATCTTCTGTCCCTTCCCAGAAAACCTACCAGGGCAGCTACGGTTTCGCTACGTCTGGGCTTCTTGCATTCTGGGACAGCCAAGGTCATCTGTGACTTGCACGTACTCCCCTGCCCTCAACAAGATGTTTTGCCAACTGGCCAAGACCTGCCCTGTGCAGCTGTGGGTTGATTCCACACCCCCGCCCGGCACCCGCGTCCGCGCCATGGCCATCTACAAGCAGTCACAGCACATGACGGAGGTTGTGAGGCGCTGCCCCCACCATGAGCGCTGCTCAGATAGCGATGGTCTGGCCCCTCCTCAGCATCTTATCCGAGTGGAAGGAAATTTGCGTGTGGAGTATTTGGATGAC"
dnaOri = dna

dna = dna.replace('GAATTC','G^AATTC')

dna = dna.split('^')


print(f'the first segment starts at {dnaOri.find(dna[0])}')
print(f'the second segment starts at {dnaOri.find(dna[1])}')
print(f'the third segment starts at {dnaOri.find(dna[2])}')

print(f'the first segment ends at {dnaOri.find(dna[1])-1}')
print(f'the second segment ends at {dnaOri.find(dna[2])-1}')
print(f'the third segment ends at {len(dnaOri)-1}')

print(f'the length of the first segment is {dnaOri.find(dna[1]) - (dnaOri.find(dna[0]))}')
print(f'the length of the second segment is {dnaOri.find(dna[2]) - (dnaOri.find(dna[1]))}')
print(f'the length of the third segment is {len(dnaOri) - (dnaOri.find(dna[2]))}')
