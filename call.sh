#!/bin/bash
#$1=sample(SS_10)
#$2=Path to bam file
#!/bin/bash

# Script to compare genotypes between WGS and SNP-CHIP datasets

# Function to log errors
log_error() {
  echo "[ERROR] $1" >> "$outdir/error.log"
}

# Parse command-line option




# Parse command-line options
while getopts "B:P:O:I:S:N:R:" flag; do
  case "${flag}" in
    B) BCFTOOLS_PATH=${OPTARG} ;;
    P) PLINK_PATH=${OPTARG} ;;
    O) OUTPUT_PATH=${OPTARG} ;;
    I) INPUT_BAM_PATH=${OPTARG} ;;
    S) SAMPLE_ID=${OPTARG} ;;
    N) SNPS_POS=${OPTARG} ;;
    R) ref_path=${OPTARG} ;;
    *) echo "Usage: $0 -B <bcftools_path> -P <plink_path> -O <output_path> -I <input_bam_path> -S <sample_id> -N <snps_pos> -R <ref_path>"; exit 1 ;;
  esac
done



$BCFTOOLS_PATH mpileup \
-R $SNPS_POS --threads 8  -q 20 -f \
$ref_path $INPUT_BAM_PATH/$SAMPLE_ID.rmdup.bam|$BCFTOOLS_PATH call \
--consensus-caller -O v -o $OUTPUT_PATH/$SAMPLE_ID.calls.vcf



$PLINK_PATH -vcf $OUTPUT_PATH/$SAMPLE_ID.calls.vcf \
 --make-bed --allow-extra-chr --out $OUTPUT_PATH/$SAMPLE_ID

$PLINK_PATH  -bfile $OUTPUT_PATH/$SAMPLE_ID  \
--out $OUTPUT_PATH/$SAMPLE_ID \
--recode transpose --allow-extra-chr
