import sys
import pdb
import os
import subprocess
import argparse
import collections
from os.path import isfile, join
import gzip
import getopt
import math

# Function to read in the position specific scoring matrix (PSSM) into a dictionary of dictionaries
def getPSSM(pssmfile):
    # open .PSSM file
    pssmdata = open(pssmfile)
    # initialize dictionary of dictionaries
    pssm = collections.defaultdict(dict)
    # read in the pssm file - line by line until there are no more lines
    while('TRUE'):
        # read the next line of the file
        pssmline=pssmdata.readline().split()
        # stop if reached the end of the file
        if not pssmline: break
        # store pssm values into a dictionary, where the first key is the position number ('pos#') and second key is the base pair
        for i in range(0,len(pssmline)-1): pssm['pos'+str(i)][pssmline[0]] = pssmline[i+1]
    return(pssm)

#Function to reverse complement 
alt_map = {'N':'N'}
complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A', 'N':'N'} 
def reverse_complement(seq):    
    for k,v in alt_map.iteritems():
        seq = seq.replace(k,v)
    bases = list(seq) 
    bases = reversed([complement.get(base,base) for base in bases])
    bases = ''.join(bases)
    for k,v in alt_map.iteritems():
        bases = bases.replace(v,k)
    return bases

# Function to read in fasta file and save it as a dictionary, where each key in the dictionary refers to one chromosome
def getFasta(fastafile):
    # open fasta file (.fa) - can open if zipped or not
    if fastafile[-2:] == "gz": fasta = gzip.open(fastafile)
    else: fasta = open(fastafile)
    # initialize a dictionary to save the fasta file in
    fastadict = dict()
    while('TRUE'):
        # read in the next line of the file
        fastaline = fasta.readline().strip()
        # stop if reached the end of the file
        if not fastaline: break
        # check if line indicates a chromosome, and initialize a new dictionary entry
        if fastaline[0] == '>':
            chr = fastaline[1:]
            fastadict[chr] = ''
        else:
            fastadict[chr] = fastadict[chr] + fastaline.upper()
    return(fastadict)

# Function to calculate PSSM score
def PSSMscore(seq, pssm, pssm_bk):
    scorehere = list()
    for j in range(0, len(pssm)):
        if 'N' in seq:
            scorehere.append(0.0)
        else:
            scorehere.append(float(pssm['pos'+str(j)][seq[j]]))
    reduce_score = reduce(lambda x, y: x+y, scorehere)
    #if reduce_score == 0:
    #   scorevalue = 0
    #else:
    #   scorevalue = round(math.log(reduce_score/pssm_bk, 2), 3)
    #return(scorevalue)
    return(reduce_score)

## Function to:
# (2) score all positions within that sequence
# (3) return the strongest motif (highest scoring) within the sequence
def getScores(fastadict, pssm, outname, distance, minscore):
    # initialize a file for output
    outfile = open(outname, 'w')
    #header for outfile: name, sequence length, highest PSSM score, position of highest scoring sequence, relative position of highest scoring sequen
ce
    #outfile.write('gene'+'\t'+'seq_len'+'\t'+'max_PSSM_score'+'\t'+'max_PSSM_pos'+'\t'+'max_PSSM_relpos'+'seq'+'\n')
    outfile.write('chromosome'+'\t'+'pssm_start'+'\t'+'pssm_end'+'\t'+'seq'+'\t'+'pssm_score'+'\t'+'strand'+'\n')
    # set the background sequence distribution to be equal probability of each base at each site
    pssm_bk = pow(0.25, len(pssm))
    # go through all the chromosomes in the fasta file (as keys in the fasta dictionary)
    for chr in fastadict.keys():
        # get chromosome 
        chromosome = chr
        # get the sequence in the fasta entry
        seq = fastadict[chr]
        # get the length of the sequence
        seqlen = len(seq)
        #if seqlen < len(pssm)*2: continue
        sequse = seq
        # if want to focus on a particular region within the sequence, separately store the shorter sequence
        if distance != 'full' and len(seq) > int(distance):
            sequse = seq[len(seq)-int(distance):]
        seqlen = len(sequse)
        # initialize a dictionary to store the scores
        scores = dict()
        revscores = dict()
        # walk across the sequence base-by-base to score each possible location of the motif
        for i in range(0,seqlen+1-len(pssm)):
            # define a sequence of pssm length at position i
            seqhere = seq[i:i+len(pssm)]
            revseq = reverse_complement(seqhere)
            # get scores for these sequences
            scorevalue = PSSMscore(seqhere, pssm, pssm_bk)
            revvalue = PSSMscore(revseq, pssm, pssm_bk)
            # write information into outfile
            if scorevalue >= minscore:
                outfile.write(str(chromosome) +'\t'+ str(i) +'\t'+ str(i+len(pssm)) +'\t'+ str(seqhere) +'\t'+ str(scorevalue) +'\t+\n')
            if revvalue >= minscore:
                outfile.write(str(chromosome) +'\t'+ str(i) +'\t'+ str(i+len(pssm)) +'\t'+ str(revseq) +'\t'+ str(revvalue) +'\t-\n')
    outfile.close()
if __name__ == '__main__':
    # input a set of arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('--pssm', type=str, help='pssm for motif desired - REQ')
    parser.add_argument('--fasta', type=str, help='fasta file to be searched (full path) - REQ')
    parser.add_argument('--outname', type=str, help='name of output file (full path) - REQ')
    parser.add_argument('--distance', type=str, default='full', help='amount of sequence to be used [full, X (nuc)]')
    parser.add_argument('--minscore', type=int, default=10, help='minimum score to report (default = 10)')
    args = parser.parse_args()

    pssm = getPSSM(args.pssm)
    fastadict = getFasta(args.fasta)
    #pdb.set_trace()
    getScores(fastadict, pssm, args.outname, args.distance, args.minscore)
