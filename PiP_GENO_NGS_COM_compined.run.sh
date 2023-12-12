#!/bin/bash

# Read configuration file
if [[ -f "config.txt" ]]; then
  source "config.txt"
else
  echo "Error: Configuration file 'config.txt' not found."
  exit 1
fi


# Part 1: Call Variants
mkdir -p OUTPUT
sh call.sh -B "$BCFTOOLS_PATH" -P "$PLINK_PATH" -O "$OUTPUT_DIR" -I "$BAM_PATH" -S "$WGS_SAMPLE" -R "$REF_PATH" -N "$SNP_POS_FILE"

# Part 2: Comparison
sh Comparison_GENOTYPE_WGS_SNP_CHIP.sh -W "$WGS_SAMPLE" -G "$GENOT_SAMPLE_ID" -O "$OUTPUT_DIR" -I "$input_genotype_tepd_file"\
 -i "$input_WGS_tepd_file" -m "$PLINK_MAP_FILE"



