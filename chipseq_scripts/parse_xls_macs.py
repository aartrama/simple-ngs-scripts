files = ['DRN_Chip1_S1_L001_R1_001_unique_sorted_rmdup_peaks.xls', 'DRN_Chip2_S2_L001_R1_001_unique_sorted_rmdup_peaks.xls', \
	'DRN_Chip3_S3_L001_R1_001_unique_sorted_rmdup_peaks.xls']
files = ['Cocaine_peaks.xls', 'Saline_peaks.xls']

for file in files:
	new_bed_file = file.split(".")[0]
	new_bed_filename = new_bed_file + '_consolidated.bed'
	with open(file, "r") as f, \
		open(new_bed_filename, "w") as outfile:
		for i in range(0, 27):
			next(f)
		for lines in f:
			lines = lines.strip().split()
			if (lines[7]) > 1.2:
				#print>>outfile, "chr"+lines[0]+"\t"+lines[1]+"\t"+lines[2]
				print>>outfile, "chr"+lines[0]+"\t"+lines[1]+"\t"+lines[2]+"\t"+lines[7]+"\t"+lines[8]
