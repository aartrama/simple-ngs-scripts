from collections import defaultdict
# first, run region analysis on a set of bed files which do not have fold change and p values. Then, change the bed
# files to include the fold change and p values (tab delimited) and run this code
files = ["Saline_peaks_consolidated.bed", "Cocaine_peaks_consolidated.bed"]

for file in files:
	dictionary = defaultdict(list)

	with open(file,"r") as f:
		for lines in f:
			lines = lines.strip().split()
			dictionary[lines[0]+"\t"+lines[1]+"\t"+lines[2]] = [lines[3], lines[4]]

	with open(file+".full.annotated", "r") as f, \
		open(file+".full.annotated.consolidated", "w") as outfile:
		print>>outfile, "Chromosome\tStart\tEnd\tFold-enrichment\tq-value\tGeneid\tTranscriptId\tStrand\tGene_start\tGene_end\tRegion\tDistance\tType\tGene_name"
		for lines in f:
			lines = lines.strip().split()
			neglogqvalue = dictionary[lines[0]+"\t"+lines[1]+"\t"+lines[2]][1]
			qvalue = str(10**(-1*float(dictionary[lines[0]+"\t"+lines[1]+"\t"+lines[2]][1])))
			print>>outfile, "\t".join([lines[0], lines[1], lines[2], dictionary[lines[0]+"\t"+lines[1]+"\t"+lines[2]][0], qvalue, \
				lines[3], lines[4], lines[5], lines[6], lines[7], lines[8], lines[9], lines[10], lines[11]])
