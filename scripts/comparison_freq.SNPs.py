import sys
#File includes genotype from WGS and SNPs genotypes
Comparison_file=sys.argv[1]
#check the order of script
Order=sys.argv[2]
#
ID=Comparison_file.split(".")[0]
Dic_allels={'A':'T','T':'A','C':'G','G':'C'}
SNPS_LIST=[]
Missed=[]
#sort genotype
with open  (Comparison_file,'r') as file1:
	for lines in file1:
		lines=lines.split()
		NGS_GENO=lines[-2].split("/")
		NGS_GENO.sort()
		SNPS_LIST.append(lines[1])
		NGS_GENO="/".join(NGS_GENO)
		Geno_SNPs=lines[-1].split("/")
		Geno_SNPs=[str(x) for x in Geno_SNPs]
		Geno_SNPs.sort()
		Geno_SNPs="/".join(Geno_SNPs)
		if str(NGS_GENO)!=str(Geno_SNPs):
			NGS_GENO=NGS_GENO.split("/")
			updated_geno=[]
			if len(NGS_GENO[0])==1:
				if len(NGS_GENO[1])==1:
					if NGS_GENO[0] not in Dic_allels:
						updated_geno=[Dic_allels[NGS_GENO[0].upper()],Dic_allels[NGS_GENO[1].upper()]]
						
					else:
						updated_geno=[Dic_allels[NGS_GENO[0]],Dic_allels[NGS_GENO[1]]]
			if len (updated_geno)<2:
				Missed.append(lines[1])
			else:
				updated_geno.sort()
				updated_geno="/".join(updated_geno)
				if updated_geno!=Geno_SNPs:
					Missed.append(lines[1])


						

if Order=="freq":
	to_print=[ID,float(len(Missed))/float(len(SNPS_LIST)),len(Missed),len(SNPS_LIST)]
	to_print=[str(x) for x in to_print]
	print " ".join(to_print)
else:
	for SNPs in Missed:
		print SNPs


