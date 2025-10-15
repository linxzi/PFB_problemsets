#!/usr/bin/env python3
import sys

oriDNA = sys.argv[1]
countDNA = oriDNA.upper()

# count the number of letters
countA = countDNA.count('A')
countT = countDNA.count('T')
countC = countDNA.count('C')
countG = countDNA.count('G')

print(f'{countDNA} has {countA} As, {countT} Ts, {countC} Cs, and {countG} Gs.')

# replace all Ts with Us
replaceDNA = countDNA.replace('T', 'U')
print(replaceDNA)

# count GC percentage
print(f'GC = {((countG+countC)/(countG+countC+countA+countT))*100:.0f}%; AT = {((countA+countT)/(countG+countC+countA+countT))*100:.0f}%')

# substring from 100-200
subDNA = countDNA[99:200]
print(f"substring = {subDNA}")

subA = subDNA.count('A')
subT = subDNA.count('T')
subC = subDNA.count('C')
subG = subDNA.count('G')

print(f'GC = {((subG+subC)/(subG+subC+subA+subT))*100:.0f}%')

# reverse sequence
translation_table = str.maketrans({'A': 'T', 'T': 'A', 'G': 'C','C':'G'})
rDNA = countDNA.translate(translation_table)
print(rDNA[::-1])

rDNA = ''
for seq in oriDNA:
    if seq == 'T':
        rDNA += 'A'
    elif seq == 'A':
        rDNA += 'T'
    elif seq == 'C':
        rDNA += 'G'
    elif seq == 'G':
        rDNA += 'C'
    elif seq == 't':
        rDNA += 'a'
    elif seq == 'a':
        rDNA += 't'
    elif seq == 'c':
        rDNA += 'g'
    elif seq == 'g':
        rDNA += 'c'

print(rDNA[::-1])

# finding start position
startDNA = countDNA.find('GAATTC') + 1
endDNA = countDNA.find('GAATTC') + 7

print(f'startPos:{startDNA} endPos:{endDNA}')
