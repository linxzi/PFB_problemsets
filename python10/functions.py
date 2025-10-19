#! /usr/bin/env python3

#####################
# 1 & 2 & 3 & 4
#####################
# import sys
# import re

# inStr = sys.argv[1]
# inWidth = sys.argv[2]

# def fold(aStr,width):
#     chunks = []
#     for i in range(0, len(aStr), width):
#         chunks.append(aStr[i:i+width])
#     return '\n'.join(chunks)

# with open(f'{inStr}.txt', 'r') as input:
#     lines = input.read()
#     lines = lines.rstrip()
#     lines = re.sub(r'[^a-zA-Z0-9\s]', '', lines)
#     lines = lines.replace('\n', '')
#     print(fold(lines,int(inWidth)))

#####################
# 5
#####################
# import sys
# import re

# inStr = sys.argv[1]

# def calGC(aStr):
#     gcCount = aStr.count('G') + aStr.count('C')
#     return (gcCount / len(aStr)) * 100

# print(f'GC content: {calGC(inStr):.2f}%')

#####################
# 6
#####################  
# import sys
# import re

# inStr = sys.argv[1]

# def revComp(aStr):
#     compDict = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
#     translationTable = str.maketrans(compDict)
#     newStr = aStr .translate(translationTable)
#     return newStr

# print(revComp(inStr)[::-1])

#####################
# 7
#####################
import subprocess

subprocess.run(['ls', '-l'])

print('-----')
output = subprocess.check_output('ls -l | grep function', shell = True)
print(output.decode('utf-8'))



