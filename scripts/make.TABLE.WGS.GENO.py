import sys


FILE_ERROR_FREQ=(sys.argv[1])
FILE_MISSED_SNPS_ALL_COUNTS=(sys.argv[2])
DUPLICATS_SNPS_POS=(sys.argv[3])
Duplicates_list=[]

with open(DUPLICATS_SNPS_POS,'r') as file1:
	for lines in file1:
		DUP_SNPS=lines.rstrip()
		Duplicates_list.append(DUP_SNPS)

DUPLICATES_COUNTS=str(len(Duplicates_list))

HEAD=["WGS_SAMPLE_ID","GENOTYPE_ERROR%","compared-error","compared-ALL","SNPs-panel-notcompared","missing-genotype-panel(0/0)"
,"scaffolds-panal-scrofa10","scaffolds-updated-scrofa11"," NGS-variant-calling-error"]

print " ".join(HEAD)
with open(FILE_MISSED_SNPS_ALL_COUNTS,'r') as file2:
	for lines2 in file2:
		lines2=lines2.split()
		with open(FILE_ERROR_FREQ,'r') as file3:
			for lines3 in file3:
				lines3=lines3.split()
				
				print " ".join(lines3+lines2[1:]+[DUPLICATES_COUNTS])

