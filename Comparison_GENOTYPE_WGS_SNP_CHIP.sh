#!/bin/bash

# Script to compare genotypes between WGS and SNP-CHIP datasets

# Function to log errors
log_error() {
  echo "[ERROR] $1" >> "$outdir/error.log"
}

# Parse command-line options
while getopts G:W:O:I:i:m: flag; do
  case "${flag}" in
    W) WGS_ID=${OPTARG} ;;
    G) SNP_CHIP_ID=${OPTARG} ;;
    O) outdir=${OPTARG} ;;
    I) input_pathTPED_SNP_CHIP=${OPTARG} ;;
    i) input_pathTPED_WGS=${OPTARG} ;;
    m) PLINK_MAP_FILE=${OPTARG} ;;
  esac
done

# Create output directory if it doesn't exist
mkdir -p "$outdir" || { log_error "Failed to create output directory"; exit 1; }

# Step 1: Check duplicated positions in WGS dataset
cat "$input_pathTPED_WGS/$WGS_ID.F.tped" | awk '{print $1"#"$4}' | sort | uniq -c | awk '{if ($1!=1) print $2}' > "$outdir/$WGS_ID.duplicated.SNPs.txt"

# Step 2: Prepare comparison file
python2 Comparison_file_make.py "$input_pathTPED_WGS/$WGS_ID.F.tped" "$PLINK_MAP_FILE" "$outdir/$WGS_ID.duplicated.SNPs.txt" "$input_pathTPED_SNP_CHIP/$SNP_CHIP_ID.tped" > "$outdir/$WGS_ID.$SNP_CHIP_ID.genotypes.comparisons.txt"

# Step 3: Compute the frequency of missed SNPs
python2 comparison_freq.SNPs.py "$outdir/$WGS_ID.$SNP_CHIP_ID.genotypes.comparisons.txt" freq > "$outdir/$WGS_ID.$SNP_CHIP_ID.genotypes.freq.txt"

# Step 4: List of SNPs included in the comparison
awk '{print $2}' "$outdir/$WGS_ID.$SNP_CHIP_ID.genotypes.comparisons.txt" > "$outdir/$WGS_ID.$SNP_CHIP_ID.lista_included.txt"
awk '{print $2}' "$input_pathTPED_SNP_CHIP/$SNP_CHIP_ID.tped" | sort -u > "$outdir/$WGS_ID.$SNP_CHIP_ID.GENOTYPED.txt"

# Step 5: List of SNPs missed and not included in the comparison
python2 FIND_MISSED_SNPS.py "$outdir/$WGS_ID.$SNP_CHIP_ID.lista_included.txt" "$input_pathTPED_SNP_CHIP/$SNP_CHIP_ID.tped" | sort -u > "$outdir/$WGS_ID.$SNP_CHIP_ID.missedSNPS.all"
comm -23 "$outdir/$WGS_ID.$SNP_CHIP_ID.GENOTYPED.txt" "$outdir/$WGS_ID.$SNP_CHIP_ID.missedSNPS.all" > "$outdir/$WGS_ID.$SNP_CHIP_ID.MISSED.NOTGENOTYPED.txt"

# Step 6: Stats for missed SNPs to add
python2 STATS.MISSED_TOADD.py "$input_pathTPED_SNP_CHIP/$SNP_CHIP_ID.tped" "$outdir/$WGS_ID.$SNP_CHIP_ID.MISSED.NOTGENOTYPED.txt" > "$outdir/$WGS_ID.$SNP_CHIP_ID.TOtableADD.txt"

# Step 7: Make final table
python make.TABLE.WGS.GENO.py "$outdir/$WGS_ID.$SNP_CHIP_ID.genotypes.freq.txt" "$outdir/$WGS_ID.$SNP_CHIP_ID.TOtableADD.txt" "$outdir/$WGS_ID.duplicated.SNPs.txt" > "$outdir/$WGS_ID.$SNP_CHIP_ID.FINAL.TABLE.GENOTYPE.WGS.txt"

# Log completion message
echo "Genotype comparison completed successfully." >> "$outdir/log.txt"

