"""
This script is for integrating the
homer annotation and the diffreps output
together.
"""

from collections import defaultdict

# did the same for ino80_diffreps_chr and ino80_diffreps_chr_annotated

diffreps = defaultdict(list)

list1 = ["diffReps_Female_ELS_vs_Female_Std.txt","diffReps_Male_ELS_vs_Female_ELS.txt","diffReps_Male_ELS_vs_Male_Std.txt","diffReps_Male_Std_vs_Female_Std.txt"]
list2 = ["diffReps_Female_ELS_vs_Female_Std_annotated.txt","diffReps_Male_ELS_vs_Female_ELS_annotated.txt","diffReps_Male_ELS_vs_Male_Std_annotated.txt","diffReps_Male_Std_vs_Female_Std_annotated.txt"]
list3 = ["diffReps_Female_ELS_vs_Female_Std_integrated.txt","diffReps_Male_ELS_vs_Female_ELS_integrated.txt","diffReps_Male_ELS_vs_Male_Std_integrated.txt","diffReps_Male_Std_vs_Female_Std_integrated.txt"]

for index in range(0, len(list1)):
# reading the diffreps file
	with open(list1[index], "r") as f:
		for i in range(33):
			next(f)
		for lines in f:
			lines = lines.strip().split("\t")
			diffreps[(lines[0], lines[1], lines[2])] = lines[5:]


# reading the homer output file
	with open(list2[index], "r") as f, \
		open(list3[index], "w") as outfile:
		for i in range(0,74):
			next(f)
		print>>outfile, "\t".join(["Chr", "Start", "End", "Strand", "Annotation", "Detailed Annotation", "Distance to TSS", "Nearest Ensembl Gene ID", "Gene Name", "Gene Alias", "Gene Description", "Gene Type"])+"\t"+"\t".join(['Control.cnt', 'Treatment.avg', 'Control.avg', 'Treatment.enr', 'Control.enr', 'Event', 'log2FC', 'pval', 'padj', 'winSta', 'winEnd', 'winFC', 'winP', 'winQ'])
		for lines in f:
			lines = lines.strip().split("\t")
			if len(lines) > 11:
				print>>outfile, "\t".join([lines[1], lines[2], lines[3], lines[4], lines[7], lines[8], lines[9], lines[14], lines[15], lines[16], lines[17], lines[18]]) + "\t"+"\t".join(diffreps[(lines[1], str(int(lines[2]) - 1 ), lines[3])])





