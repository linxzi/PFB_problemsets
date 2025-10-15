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
    j = random.randrange(i + 1) 
    #print(j)
    print(f'old {seqList[i]} and {seqList[j]}')
    temp = seqList[i]
    seqList[i] = seqList[j] 
    seqList[j] = temp
    print(f'new {seqList[i]} and {seqList[j]}')

seqOut = "".join(seqList)
print(seqOut)



