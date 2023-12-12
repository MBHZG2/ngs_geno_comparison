import sys

def count_snps(filename):
    with open(filename, 'r') as f:
        count = 0
        for line in f:
            count += 1
    return count

def count_missing_genotypes(filename):
    missing_genotypes = set()
    with open(filename, 'r') as f:
        for line in f:
            genotypes = line.split()
            if genotypes[-1] == "0":
                missing_genotypes.add(genotypes[1])
    return len(missing_genotypes)

def count_not_found_positions(filename):
    not_found_positions = set()
    with open(filename, 'r') as f:
        for line in f:
            genotypes = line.split()
            if genotypes[0] not in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', 'X', 'Y']:
                not_found_positions.add(genotypes[1])
    return len(not_found_positions)

def main():
    Genotyp_SNP_beadchip = sys.argv[1]
    SNPS_NOT_IN_Comparisons = sys.argv[2]
    SAMPLE_ID = Genotyp_SNP_beadchip.split(".")[0]

    all_missed_snps = count_snps(SNPS_NOT_IN_Comparisons)
    all_missing_genotypes = count_missing_genotypes(Genotyp_SNP_beadchip)
    all_not_found_positions = count_not_found_positions(Genotyp_SNP_beadchip)

    to_print = [SAMPLE_ID, all_missed_snps, all_missing_genotypes, all_not_found_positions]
    to_print = [str(x) for x in to_print]
    print(" ".join(to_print))

if __name__ == '__main__':
    main()
