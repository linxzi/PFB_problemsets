#!/usr/bin/env python3

########################
# 1 - 7
########################
class DNARecord(object):
  def __init__(self, sequence, gene_name, species_name): 
    self.sequence = sequence.upper()
    self.gene_name = gene_name
    self.species_name = species_name

    print(self.sequence)
    print(self.gene_name)
    print(self.species_name)

  def get_length(self):
    length = len(self.sequence)
    return length
  
  def count_nucleotide(self):
    countA = self.sequence.count("A")
    countC = self.sequence.count("C")
    countG = self.sequence.count("G")
    countT = self.sequence.count("T")
    count = {'A': countA, 'C': countC, 'G': countG, 'T': countT}
    return count
  
  def get_gc_content(self):
    gcCount = self.sequence.count('G') + self.sequence.count('C')
    finalCount = (gcCount / len(self.sequence)) * 100
    return finalCount
  
  def fasta_format(self):
    fastaStr = f'>{self.gene_name} {self.species_name}\n'
    for i in range(0, len(self.sequence), 60):
        fastaStr += self.sequence[i:i+60] + '\n'
    return fastaStr



dna_rec_obj_1 = DNARecord('ACTGATCGTTACGTACGAGTACTGATCGTTACGTACGAGTACTGATCGTTACGTACGAGTACTGATCGTTACGTACGAGTACTGATCGTTACGTACGAGTACTGATCGTTACGTACGAGTACTGATCGTTACGTACGAGTACTGATCGTTACGTACGAGTACTGATCGTTACGTACGAGTACTGATCGTTACGTACGAGTACTGATCGTTACGTACGAGTACTGATCGTTACGTACGAGTACTGATCGTTACGTACGAGTACTGATCGTTACGTACGAGTACTGATCGTTACGTACGAGTACTGATCGTTACGTACGAGTACTGATCGTTACGTACGAGTACTGATCGTTACGTACGAGTACTGATCGTTACGTACGAGT', 'ABC1', 'Drosophila melanogaster')
print(dna_rec_obj_1.get_length())
print(dna_rec_obj_1.count_nucleotide())
print(f'GC content: {dna_rec_obj_1.get_gc_content():.2f}%')
print(dna_rec_obj_1.fasta_format())


######################
# Challenge Question
######################

def comp(obj1,obj2):
  if obj1.get_gc_content() == obj2.get_gc_content():
    return True
  else:
    return False

print(comp(dna_rec_obj_1, dna_rec_obj_1))  