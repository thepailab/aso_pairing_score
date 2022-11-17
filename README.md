# Aso pairing score

### Citation: Wang F, Calvo-Roitberg E, Rembetsy-Brown J, Sousa J, Meda Krishnamurthy P, Lee J, Fang M, Green M, Pai A, Watts J. (2022). G-rich motifs within phosphorothioate-based antisense oligonucleotides (ASOs) drive activation of FXN expression through indirect effects (Nucleic Acids Research)
https://doi.org/10.1093/nar/gkac1108



This script scans an input fasta file for sequences that match or are complementary to the ASO sequence of interest.

## Requirements:
python (v3.3.2)

## Overview
In _ G-rich motifs within phosphorothioate-based antisense oligonucleotides (ASOs) drive activation of FXN expression through indirect effects_ we showed that antisense oligonucleotides (ASOs) that were carefully designed can still have off-target effects. This script scans an input fasta file containing multiple features and calculates a pairing score based on the provided position-specific score matrix (pssm) that can be customized according to the researchers needs.

An example of a pssm is provided [here](https://github.com/thepailab/aso_pairing_score/blob/02c6e8ae2c33e1fdacdd88d0f6d32e42662c08f4/S30.PSSM). Each column represents a base on the ASO and each row the matching nucleotide, thus, each cell is the assigned score for finding that nucleotide at a given ASO position.

```
usage: scanMotifs_summedScore.py [-h] [--pssm PSSM] [--fasta FASTA]
                                 [--outname OUTNAME] [--distance DISTANCE]
                                 [--minscore MINSCORE]

optional arguments:
  -h, --help           show this help message and exit
  --pssm PSSM          pssm for motif desired - REQ
  --fasta FASTA        fasta file to be searched (full path) - REQ
  --outname OUTNAME    name of output file (full path) - REQ
  --distance DISTANCE  amount of sequence to be used [full, X (nuc)]
  --minscore MINSCORE  minimum score to report (default = 10)
```

## Output


| Column Name  | Description |
| ------------- | ------------- |
| feature  | name of the feature used to blast the ASO  |
| pssm_start  | start of the feature targeted by the ASO |
| pssm_end  | end of the feature targeted by the ASO  |
| seq  | targeted sequence  |
| pssm_score  | summed pairing score between the ASO and the feature  |
| strand  | strand used to calculate the score  |












