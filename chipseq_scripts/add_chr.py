"""
This code is for adding the 
chr prefix to a file if not
present.
"""
import os

chromosomes = ["X", "Y", "MT"]

def check_str_to_int(element):
	try:
	    return int(element)

	except ValueError:
	    return "Not an integer"

def add_chr_prefix(filename):
	# function to check if a string can be
	# converted to an integer
	with open(filename, "r") as f, \
		open(filename + "_chr", "w") as outfile:
		for lines in f:
			lines = lines.strip().split("\t")
			if check_str_to_int(lines[0]) != "Not an integer":
				print>>outfile, "chr" + "\t".join(lines)

			elif lines[0] in chromosomes:
				print>>outfile, "chr" + "\t".join(lines)

			else:
				print>>outfile, "\t".join(lines)

for file in os.listdir(os.getcwd()):
	if file.endswith(".bed"):
		add_chr_prefix(file)

for file in os.listdir(os.getcwd()):
        if file.endswith(".txt"):
                add_chr_prefix(file)
