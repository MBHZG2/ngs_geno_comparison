#!/bin/bash

# Default configuration file
CONFIG_FILE="config.txt"

# Parse command-line options
while getopts "c:" flag; do
  case "${flag}" in
    c) CONFIG_FILE=${OPTARG} ;;
    *) echo "Usage: $0 -c <config_file>"; exit 1 ;;
  esac
done

# Read configuration file
if [[ -f "$CONFIG_FILE" ]]; then
  source "$CONFIG_FILE"
else
  echo "Error: Configuration file '$CONFIG_FILE' not found."
  exit 1
fi

# Part 1: Call Variants
mkdir -p OUTPUT
sh call.sh -B "$BCFTOOLS_PATH" -P "$PLINK_PATH" -O "$OUTPUT_DIR" -I "$BAM_PATH" -S "$WGS_SAMPLE" -R "$REF_PATH" -N "$SNP_POS_FILE"

# Part 2: Comparison
sh Comparison_GENOTYPE_WGS_SNP_CHIP.sh -W "$WGS_SAMPLE" -G "$GENOT_SAMPLE_ID" -O "$OUTPUT_DIR" -I "$input_genotype_tepd_file"\
 -i "$input_WGS_tepd_file" -m "$PLINK_MAP_FILE"



