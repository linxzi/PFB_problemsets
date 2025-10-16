#!/usr/bin/env python3

###########
# 1
###########
# readFile = open("Python_06.txt","r")
# for line in readFile: # Python magic: reads in a line from file
#   line = line.upper()
#   print(line)
# readFile.close()

###########
# 2
###########
# with open("Python_06.txt","r") as readFile, open("Python_06_uc.txt","w") as writeFile:
#   for line in readFile:
#     line = line.upper()
#     line = line.rstrip()
#     writeFile.write(f"{line}\n")
# print("Wrote 'Python_06.txt'")

###########
# 3
###########
# genes = {}
# readFile = open("Python_06.seq.txt","r")
# for line in readFile:
#     line = line.rstrip()
#     seqName,seq = line.split()
#     rSeq = ''
#     for nt in seq:
#         if nt == 'T':
#             rSeq += 'A'
#         elif nt == 'A':
#             rSeq += 'T'
#         elif nt == 'C':
#             rSeq += 'G'
#         elif nt == 'G':
#             rSeq += 'C'
#     rSeq = rSeq [::-1]

#     genes[seqName] = rSeq
# print(genes)

###########
# 4
###########
n = 0
nID = 0
nChar = 0
nNT = 0
lineNT = 0
target = "TCGA"
count = 4
def check_chars(input, target_letters):
    for char in input:
        if char not in target_letters:
            return False
    return True

readFile = open("Python_06_test.fastq","r")
for line in readFile: # Python magic: reads in a line from file
  line = line.rstrip()
  n += 1
  print(f'n={n}')
  if count%4 == 0:
    nID += 1
  nChar += len(line)
  #before,after = line.split("\t")
  #print(f'before')
  #print(before)
  #print(f'after')
  #print(after)
  if check_chars(line, target) == True:
    nNT += len(line)
    lineNT += 1
    print(f'lineNT={lineNT}')
  count +=1
print(f'total number of lines: {n}')
print(f'total number of sequence IDs: {nID}')
print(f'total number of characters: {nChar}')
print(f'total number of nucleotides: {nNT}')
print(f'average line lenth of all lines: {nChar/n}')
print(f'average line lenth of all lines that contain sequences: {nNT/lineNT}')

readFile.close()





