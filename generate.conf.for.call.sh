#!/bin/bash
#This script generates conf file for each samples
# Path to the file containing sample names (assuming one sample name per line)
SAMPLE_NAMES_FILE="sample_names.txt"

# Define variables for common paths and parameters
BCFTOOLS_PATH="/path/to/bcftools"
PLINK_PATH="/path/to/plink"
REFERENCE_PATH="/path/to/reference.fasta"
BAM_BASE_PATH="/path/to/BAM_files/"
SNP_POS_FILE="/path/to/POS_file.txt"
PLINK_MAP_FILE="raw_tradotto_shiftato.map"
OUTPUT_DIR="CALL_ALL"
GENOT_SAMPLE_ID="GENOT_SAMPLE_ID"
GENO_FOLDER="geno"
WGS_OUTPUT_FOLDER="OUTPUT"

# Loop through each sample in the file
while IFS= read -r SAMPLE_NAME; do
    # Generate a configuration file for each sample
    CONFIG_FILE="config_$SAMPLE_NAME.txt"

    # Create the configuration file
    echo "BCFTOOLS_PATH=\"$BCFTOOLS_PATH\"" > "$CONFIG_FILE"
    echo "PLINK_PATH=\"$PLINK_PATH\"" >> "$CONFIG_FILE"
    echo "REF_PATH=\"$REFERENCE_PATH\"" >> "$CONFIG_FILE"
    echo "BAM_PATH=\"$BAM_BASE_PATH$SAMPLE_NAME/\"" >> "$CONFIG_FILE"
    echo "SNP_POS_FILE=\"$SNP_POS_FILE\"" >> "$CONFIG_FILE"
    echo "PLINK_MAP_FILE=\"$PLINK_MAP_FILE\"" >> "$CONFIG_FILE"
    echo "WGS_SAMPLE=\"$SAMPLE_NAME\"" >> "$CONFIG_FILE"
    echo "OUTPUT_DIR=\"$OUTPUT_DIR\"" >> "$CONFIG_FILE"
    echo "GENOT_SAMPLE_ID=\"$GENOT_SAMPLE_ID\"" >> "$CONFIG_FILE"
    echo "input_genotype_tepd_file=\"$GENO_FOLDER/\"" >> "$CONFIG_FILE"
    echo "input_WGS_tepd_file=\"$WGS_OUTPUT_FOLDER/\"" >> "$CONFIG_FILE"

done < "$SAMPLE_NAMES_FILE"

