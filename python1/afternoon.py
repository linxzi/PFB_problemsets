#!/usr/bin/env python3
import sys

dna = "GTACCTTGATTTCGTATTCTGAGAGGCTGCTGCTTAGCGGTAGCCCCTTGGTTTCCGTGGCAACGGAAAA"
if "GTA" in dna:
    print("Aye GTA")
else:
    print("Bye GTA")

numCheck = int(sys.argv[1])

if numCheck > 0:
    print("positive")
    if numCheck < 50:
        print("<50")
        if numCheck % 2 == 0:
            print("it is an even number that is smaller than 50")
        else: 
            print("not even")
    elif numCheck > 50:
        print(">50")
        if numCheck % 3 == 0:
            print("it is larger than 50 and divisible by 3")
        else:
            print("not divisible by 3")
    else:
        print("It's 50")
elif numCheck < 0:
    print("negative")
else:
    print("It's 0")