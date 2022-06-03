# Aso pairing score

Citation: Wang F, Calvo-Roitberg E, Rembetsy-Brown J, Sousa J, Meda Krishnamurthy P, Lee J, Fang M, Green M, Pai A, Watts J. (2022). Intron-targeted ASOs drive activation of FXN expression through indirect effects. (bioRxiv)


This script scans an input fasta file for sequences that match or are complementary to the ASO sequence of interest.

Requirements:
python (v3.3.2)

Overview

for threshold in 40 45 ;do for psmms in FA9 FA9_L5 FA48 FA48_SCRAMBLED FA9_L5_SCRAMBLED FA9_SCRAMBLED;do bsub -q long -n 5 -R rusage[mem=10000] -R span[hosts=1] -W 12:00 -J "$psmms"_"$threshold" -o "$psmms"_"$threshold".o -e "$psmms"_"$threshold".e python scanMotifs_summedScore.py --minscore $threshold --pssm /project/umw_athma_pai/ezequiel/FXN_damon/kmer_enrichment/"$psmms".PSSM --fasta /project/umw_athma_pai/ezequiel/FXN_damon/kmer_enrichment/upregulatedgenes.fasta --outname /project/umw_athma_pai/ezequiel/FXN_damon/kmer_enrichment/"$psmms"_"$threshold".kmerout;done;done


