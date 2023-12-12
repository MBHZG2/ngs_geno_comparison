import sys
D={}

#give chromosmes code (chr or NC), to change the code based on NGS code chromosmes 

Dic_ensembel_code_chromosome={'NC_010451.4': 'chr9', 'NC_010449.5': 'chr7', 'NC_010462.3': 'chrY', 'NC_010448.4': 'chr6', 'NC_010445.4': 'chr3',
	   'chrY': 'NC_010462.3', 'chrX': 'NC_010461.5', 'NC_010444.4': 'chr2', 'chr12': 'NC_010454.4', 'chr11': 'NC_010453.5',
		 'chr10': 'NC_010452.4', 'chr17': 'NC_010459.5', 'NC_010457.5': 'chr15', 'chr15': 'NC_010457.5', 'chr14': 'NC_010456.5',
		   'chr18': 'NC_010460.4', 'NC_010447.5': 'chr5', 'NC_010454.4': 'chr12', 'NC_010455.5': 'chr13', '-': 'chrNC_000845.1',
			 '.': 'chr-', 'chr13': 'NC_010455.5', 'NC_010458.4': 'chr16', 'NC_010459.5': 'chr17', 'chrType': 'Name', 
			 'chrNC_000845.1': '-', 'NC_010446.5': 'chr4', 'Name': 'chrType', 'NC_010452.4': 'chr10', 'chr5': 'NC_010447.5', 
			 'chr-': '.', 'NC_010450.4': 'chr8', 'chr7': 'NC_010449.5', 'chr6': 'NC_010448.4', 'NC_010443.5': 'chr1', 'chr4': 
			 'NC_010446.5', 'chr3': 'NC_010445.4', 'chr2': 'NC_010444.4', 'chr1': 'NC_010443.5', 'NC_010453.5': 'chr11', 
			 'chr9': 'NC_010451.4', 'chr8': 'NC_010450.4', 'NC_010460.4': 'chr18', 'NC_010461.5': 'chrX', 
			 'NC_010456.5': 'chr14', 'chr16': 'NC_010458.4'}
#make genotype dic from NGS tped file
def read_genotype_data(Genotype_from_WGS):
    Dic_genotype_from_NGS_markers = {}
    with open(Genotype_from_WGS, 'r') as NGS_file:
        for lines in NGS_file:
            lines = lines.split()
            Genotype = lines[4] + "/" + lines[5]
            tag_NGS = lines[0] + "#" + lines[3]
            Dic_genotype_from_NGS_markers[tag_NGS] = Genotype
    return Dic_genotype_from_NGS_markers


#function to make dictionary to updated chromosomes postiosn with scrofa11

def read_map_file(map_file):
    Dic_map_file = {}
    with open(map_file, 'r') as File_map:
        for SNPs in File_map:
            SNPs = SNPs.split()
            Dic_map_file[SNPs[1]] = "chr" + SNPs[0] + "#" + SNPs[3]
    return Dic_map_file
#header
H=["chr","pos","snp","NGS","GENO"]
print " ".join(H)

#duplicated SNPs in postions
def read_duplicate_list(duplicate_list_file):
    DUP = []
    with open(duplicate_list_file, 'r') as dup:
        for items in dup:
            items = items.rstrip()
            DUP.append(items)
    return DUP

#read tped from SNP_beadchip dataset_remove duplicates_integrate information from both WGS and SNP_beadchip tped files
def print_output(Genotype_from_WGS, map_file, duplicate_list_file, Genotype_from_SNP_CHIP):
    Dic_genotype_from_NGS_markers = read_genotype_data(Genotype_from_WGS)
    Dic_map_file = read_map_file(map_file)
    DUP = read_duplicate_list(duplicate_list_file)
    NCBI = Dic_genotype_from_NGS_markers.keys()[1][0:2]
    with open(Genotype_from_SNP_CHIP, 'r') as geno:
        for items1 in geno:
            items1 = items1.split()
            SNP_ID = items1[1]
            if SNP_ID in Dic_map_file:
                SNP_ID_POS11 = Dic_map_file[SNP_ID]
                SNP_ID_POS11_NC = SNP_ID_POS11
                if SNP_ID_POS11[0:2]!= NCBI:
                    SNP_ID_POS11_NC = Dic_ensembel_code_chromosome[SNP_ID_POS11.split("#")[0]] + "#" + SNP_ID_POS11.split("#")[1]
                if SNP_ID_POS11_NC in Dic_genotype_from_NGS_markers:
                    GENO_NGS = Dic_genotype_from_NGS_markers[SNP_ID_POS11_NC]
                    if str(GENO_NGS)!= "0":
                        if items1[4]!= "0":
                            if SNP_ID_POS11_NC not in DUP:
                                geno_SNP_CHIP = items1[4] + "/" + items1[5]
                                CHR_CODE = "chr" + items1[0]
                                SNP = items1[1]
                                POS = items1[3]
                                TO_print = [CHR_CODE, SNP, POS, GENO_NGS, geno_SNP_CHIP]
                                print(" ".join(TO_print))

print_output(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4])



