#!/usr/bin/env python3  
from Bio import SeqIO
from Bio.SeqUtils import gc_fraction

#############################
# FASTA Parser
#############################

# n = 0
# nNt = 0
# longest_seq = ''
# shortest_seq = ''
# GC_count = 0
# GC_count_lowest = 0
# for seq_record in SeqIO.parse("test.fa", "fasta"):   # give filename and format
#   print('ID', seq_record.id)
#   print('Sequence', seq_record.seq)
#   nNt += len(seq_record.seq)
#   print('Length', len(seq_record))
#   n += 1

#   if longest_seq == '':
#     longest_seq = seq_record.seq
#   elif len(seq_record.seq) > len(longest_seq):
#     longest_seq = seq_record.seq

#   if shortest_seq == '':
#     shortest_seq = seq_record.seq
#   elif len(seq_record.seq) < len(shortest_seq):
#     shortest_seq = seq_record.seq  

#   #current_GC = (seq_record.seq.count('G') + seq_record.seq.count('C'))/len(seq_record.seq) * 100
#   current_GC = gc_fraction(seq_record) * 100
#   if GC_count == 0:
#     GC_count = current_GC
#   elif current_GC > GC_count:
#     GC_count = current_GC

#   if GC_count_lowest == 0:
#     GC_count_lowest = current_GC
#   elif current_GC < GC_count_lowest:
#     GC_count_lowest = current_GC

# print(f'sequence count: {n}')
# print(f'total number of nucleotides: {nNt}')
# print(f'Ave len: {nNt/n:.2f}')
# print(f'Longest sequence: {longest_seq}')
# print(f'Shortest sequence: {shortest_seq}')
# print(f'Highest GC count: {GC_count:.2f}%')
# print(f'Lowest GC count: {GC_count_lowest:.2f}%')


#############################
# Extracting Salmonella paratyphi B entries from uniprot_sprot.fasta
#############################

# n = 0
# with open("s_paratyphi.prot.fa", "w") as out_f:
#     for res_record in SeqIO.parse("uniprot_sprot.fasta", "fasta"):
#         if "Salmonella paratyphi B" in res_record.description:
#             print(n) 
#             n += 1
#             out_f.write(f'>{res_record.description}\n{res_record.seq}\n')

#############################
# Parse BLAST Output
#############################

from Bio.Blast import NCBIXML
result_handle = open("result.xml")
blast_records = NCBIXML.parse(result_handle)
for blast_record in blast_records:
   query_id = blast_record.query_id
   for alignment in blast_record.alignments:
     for hsp in alignment.hsps:
        if hsp.expect < 1e-5:
           print(f'qid: {query_id} hit_id: {alignment.title} E: {hsp.expect}' )
           









