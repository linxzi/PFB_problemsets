#!/usr/bin/env python3

import re

poem = open("Python_07_nobody.txt", "r")

###############
# 1
###############

# n = 1
# for line in poem:
#     found = re.search(r"Nobody",line)
#     print(found)
#     print(f'line {n}:')
#     n +=1

###############
# 2
###############

# subName = ''
# for line in poem:
#     subName += re.sub(r'Nobody' , 'goat', line)
#     #print(subName)

# with open("goat.txt","w") as file:
#     file.write(subName)

###############
# 3 & 4 & 5
###############

# fasta = open("Python_07.fasta", "r")

# header = {}
# n = 0
# for line in fasta:
#     if re.search(r'>',line):
#         header[n] = line
#         #print(header[n])
#         n += 1

# fasta = open("Python_07.fasta", "r")
# seq = {}
# n = 0
# for line in fasta:
#     #print(line)
#     if not re.search(r'>',line):
#         seq[n] = line
#         #print(seq[n])
#         n += 1
# #print(seq)

# seqStr = '\n'.join(value.strip() for value in seq.values())
# #print(seqStr)
# seqDict = seqStr.strip().split('\n\n')
# #print(seqDict)

# finalDict = {}
# n = 1
# for item in seqDict:
#     finalDict[(f'seq{n}')] = item
#     n += 1
# #print(finalDict)


# n = 1
# for item in header:
#     for (upstream, downstream) in re.findall(r">(.+?)\s(.+)$", header[item]):
#         print("id:" , upstream)
#         print("desc:" , downstream)
#         print(finalDict[(f'seq{n}')])
#         n += 1


###############
# 6
###############

# fastaA = open("Python_07_Apol.fasta", "r")

# n = 1
# for line in fastaA :
#     found = re.search(r"[AG]AATT[CT]",line)
#     print(found)
#     print(f'line {n}:')
#     n +=1


###############
# 7 & 8
###############

# fastaA = open("Python_07_Apol.fasta", "r")

# seq = []
# n = 0
# for line in fastaA:
#     if not re.search(r"[AG]AATT[CT]",line):
#         seq.insert(n,line)
#     else:
#         lineNew = re.sub(r'([AG])AATT([CT])' , r'\1^AATT\2', line)
#         seq.insert(n,lineNew)
#     n += 1
#     #print(seq[n])

# #print(seq)
# seqString = " ".join(seq)
# print(seqString)

# noSpace = ''
# for line in seqString:
#     line = line.rstrip()
#     noSpace += line
# print(noSpace)

# seqList = noSpace.split('^')
# print(seqList)

###############
# 9 & 10
###############
import re
import sys

enz = {}

pattern = r"  +"

with open("bionet.txt","r") as bionet:
    lines = bionet.readlines()[10:]
    for line in lines:
        line = line.rstrip()
        if not line == '':
            enzId,seq = re.split(pattern,line)
            #print(afterS)
            enz[enzId] = seq

#print(enz)

inId = sys.argv[1]
inSeq = sys.argv[2]
pattern2 = ''
if inId in enz:
    #print(inId)
    #print(enz[inId])
    with open(inSeq,"r") as inFas:
        lines = inFas.readlines()[1:]
        for line in lines:
            #print(line)
            if re.search(enz[inId],line):
                print(inId)
                print(enz[inId])
                pattern2 = enz[inId]
        frags = re.split(pattern2,line)
        print(f'number of fragments: {len(frags)}')  
        print(frags)
        print(sorted(frags))








