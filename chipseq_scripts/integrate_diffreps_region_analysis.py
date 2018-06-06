"""
This code is for integrating the
output of diffreps and region
analysis. 
"""

dictionary = {'diffReps_Male_Std_vs_Female_Std.txt': 'diffReps_Male_Std_vs_Female_Std_1_22.bed.full.annotated', \
	      'diffReps_Male_ELS_vs_Male_Std.txt': 'diffReps_Male_ELS_vs_Male_Std_1_22.bed.full.annotated', \
	      'diffReps_Male_ELS_vs_Female_ELS.txt': 'diffReps_Male_ELS_vs_Female_ELS_1_22.bed.full.annotated', \
	      'diffReps_Female_ELS_vs_Female_Std.txt': 'diffReps_Female_ELS_vs_Female_Std_1_22.bed.full.annotated'}

from collections import defaultdict

for key in dictionary:
	region_analysis_output = defaultdict(list)

	with open(key, "r") as f:
		for i in range(0,33):
			next(f)
		for lines in f:
			lines = lines.strip().split()
			region_analysis_output[(lines[0], lines[1], lines[2])] = lines[3:]

	# print region_analysis_output
	with open(dictionary[key], "r") as f, \
		open(dictionary[key]+"_comprehensive.csv", "w") as outfile:
		print>>outfile, "Chromosome,Start,End,Geneid,TranscriptId,Strand,Gene_start,Gene_end,Region,Distance,Type,Gene_name,Length,Treatment.cnt,Control.cnt,Treatment.avg,Control.avg,Treatment.enr,Control.enr,Event,log2FC,pval,padj,winSta,winEnd,winFC,winP,winQ"
		for lines in f:
			lines = lines.strip().split("\t")
			print>>outfile, ",".join(lines)+","+",".join(region_analysis_output[(lines[0], lines[1], lines[2])])


