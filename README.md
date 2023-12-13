# Genotype Comparison Pipeline

## Introduction

This repository contains a Bash pipeline for comparing genotypes between Whole Genome Sequencing (WGS) and SNP-CHIP datasets. The pipeline is designed to be used in a Linux environment.

## Clone the repository:
git clone https://github.com/MBHZG2/ngs_geno_comparison.git
cd ngs_geno_comparison
## Update the configuration file config.txt with the appropriate inputs and tools path
## Run the Pipeline

### Usage
#### to run 
bash PiP_GENO_NGS_COM_compined.run.sh -c $sample_config_file.txt
#### Step1 generate config file for eahc sample
bash generate.conf.for.call.sh
#### Step 2: Run the variant calling script
sh call.sh -B "$BCFTOOLS_PATH" -P "$PLINK_PATH" -O "$OUTPUT_DIR" -I "$BAM_PATH" -S "$WGS_SAMPLE" -R "$REF_PATH" -N "$SNP_POS_FILE"
#### Step 3: Run the comparison script
sh Comparison_GENOTYPE_WGS_SNP_CHIP.sh -W "$WGS_SAMPLE" -G "$GENOT_SAMPLE_ID" -O "$OUTPUT_DIR" -I "$input_genotype_tepd_file" -i "$input_WGS_tepd_file" -m "$PLINK_MAP_FILE"




