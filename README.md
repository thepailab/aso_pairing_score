# Aso pairing score

### Citation: Wang F, Calvo-Roitberg E, Rembetsy-Brown J, Sousa J, Meda Krishnamurthy P, Lee J, Fang M, Green M, Pai A, Watts J. (2022). Intron-targeted ASOs drive activation of FXN expression through indirect effects. (bioRxiv)


This script scans an input fasta file for sequences that match or are complementary to the ASO sequence of interest.

## Requirements:
python (v3.3.2)

## Overview
In _Intron-targeted ASOs drive activation of FXN expression through indirect effects_ we showed that antisense oligonucleotides (ASOs) that were carefully designed can still have off-target effects. This script scans an input fasta file and calculates a pairing score based on the provided position-specific score matrix (pssm) that can be customized according to the researchers needs.

An example of a pssm is provided here. Each column represents a base on the ASO and each row the matching nucleotide, thus, each cell is the assigned score for finding that nucleotide at a given ASO position.

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
| chromosome  | Content Cell  |
| pssm_start  | Content Cell  |
| pssm_end  | Content Cell  |
| seq  | Content Cell  |
| pssm_score  | Content Cell  |
| strand  | Content Cell  |












