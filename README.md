# Genotype Comparison Pipeline

## Introduction

This repository contains a Bash pipeline for comparing genotypes between Whole Genome Sequencing (WGS) and SNP-CHIP datasets. The pipeline is designed to be used in a Linux environment.

## Usage

### Prerequisites

- [BCFTOOLS](https://samtools.github.io/bcftools/bcftools.html)
- [PLINK](https://www.cog-genomics.org/plink/)
- Python 2.x

### Setup

1. **Clone the repository:**

   ```bash
   git clone https://github.com/MBHZG2/ngs_geno_comparison.git
   cd ngs_geno_comparison
2. **Update the configuration file config.txt with the appropriate paths and settings**

Run the Pipeline
Run the variant calling script:
sh call.sh -B "$BCFTOOLS_PATH" -P "$PLINK_PATH" -O "$OUTPUT_DIR" -I "$BAM_PATH" -S "$WGS_SAMPLE" -R "$REF_PATH" -N "$SNP_POS_FILE"
3. **Run the comparison script** 

sh Comparison_GENOTYPE_WGS_SNP_CHIP.sh -W "$WGS_SAMPLE" -G "$GENOT_SAMPLE_ID" -O "$OUTPUT_DIR" -I "$input_genotype_tepd_file" -i "$input_WGS_tepd_file" -m "$PLINK_MAP_FILE"


### Scripts
**1. call.sh**
This script performs variant calling from BAM files using BCFTOOLS and converts the VCF file to PLINK format using PLINK.

**Usage**
sh call.sh -B <bcftools_path> -P <plink_path> -O <output_path> -I <input_bam_path> -S <sample_id> -N <snps_pos> -R <ref_path>


**2. Comparison_GENOTYPE_WGS_SNP_CHIP.sh**
This script compares genotypes between WGS and SNP-CHIP datasets. It performs several steps including checking duplicated positions, preparing a comparison file, computing the frequency of missed SNPs, and generating final tables.

**Usage**
sh Comparison_GENOTYPE_WGS_SNP_CHIP.sh -W <wgs_id> -G <snp_chip_id> -O <output_dir> -I <input_pathTPED_SNP_CHIP> -i <input_pathTPED_WGS> -m <plink_map_file>

