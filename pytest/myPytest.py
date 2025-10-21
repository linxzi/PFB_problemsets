#! usr/bin/env python3
import pytest

###########################
# 1 & 2
###########################

# def gc_content(seq):
#     valid = {'A', 'C', 'G', 'T', 'a', 'c', 'g', 't', 'N', 'n'}
#     seq = seq.upper()
#     if not set(seq).issubset(valid):
#         raise ValueError("Invalid characters in sequence")
#     if len(seq) == 0:
#         return 0
#     return (seq.count('G') + seq.count('C')) / len(seq)

# def test_GCGC():
#     assert gc_content("GCGCGC") == 1.0

# def test_ATAT():
#     assert gc_content("ATAT") == 0.0

# def test_ATGC():
#     assert gc_content("ATGC") == 0.5

# def test_empty_sequence():
#     assert gc_content("") == 0

# def test_ATGXB():
#     with pytest.raises(ValueError):
#         gc_content("ATGXB")

# def test_ATGNNNTAGC():
#     assert gc_content("ATGNNNTAGC") == 0.3

# def test_gattacaa():
#     assert gc_content("gattacaa") == 0.25

###########################
# 3
###########################

# def reverse_complement(seq):
#     if not set(seq).issubset({'A', 'C', 'G', 'T', 'a', 'c', 'g', 't', 'N', 'n'}):
#         raise TypeError("Sequence contains invalid characters")
#     complement = str.maketrans('ACGTacgt', 'TGCAtgca')
#     return seq.translate(complement)[::-1]

# def test_lowercase():
#     assert reverse_complement("acgt") == "acgt"

# def test_uppercase():
#     assert reverse_complement("ACGT") == "ACGT"

# def test_mixedcase():
#     assert reverse_complement("AcGt") == "aCgT"

# def test_nonATGCN():
#     try:
#         observed = reverse_complement("ATGXN")
#     except TypeError:
#         return
#     assert False, "Expected TypeError for non-ATGCN characters: got ({observed})"

###########################
# 4 & 5
###########################

# def isnumeric(value):
#     try:
#         float(value)
#         return True
#     except ValueError:
#         return False

# def test_numbers():
#     assert isnumeric(1.3) is True

# def test_string():
#     assert isnumeric("1.3") is True

# def test_scientific():
#     assert isnumeric("1e-6") is True

# def test_negative():
#     assert isnumeric("-0.0001") is True

# def test_symStr():
#     assert isnumeric("not-a-number") is False


