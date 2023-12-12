import sys

def read_snp_list(file_path):
    snp_set = set()
    with open(file_path, 'r') as file:
        for line in file:
            snp_set.add(line.rstrip())
    return snp_set

def read_genotypes(file_path, snp_set):
    genotypes = {}
    with open(file_path, 'r') as file:
        for line in file:
            line = line.split()
            if line[1] in snp_set:
                genotypes[line[1]] = line[2]
    return genotypes

F_SNPs_list = sys.argv[1]
Genotyped_tped = sys.argv[2]

snp_set = read_snp_list(F_SNPs_list)
genotypes = read_genotypes(Genotyped_tped, snp_set)

snp_list = [snp for snp in snp_set if snp in genotypes]

for snp in snp_list:
    print(snp)
