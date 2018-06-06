import os

for file in os.listdir(os.getcwd()):
	if file.endswith(".txt"):
		print file
		file_prefix = file.split(".txt")[0]
		with open(file, "r") as f, \
			open(file_prefix+".bed", "w") as outfile:
			for i in range(33):
				next(f)
			for lines in f:
				lines = lines.strip().split()
				print>>outfile, lines[0]+"\t"+lines[1]+"\t"+lines[2]
