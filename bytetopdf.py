#!/usr/bin/env python3

import sys

print("len: " + str(len(sys.argv)))
if len(sys.argv) > 3 or len(sys.argv) < 2:
	print('Usage: python bytetopdf.py <input file> <optional: output file>')
	sys.exit(0)

inpath = sys.argv[1]

# cleanup file paths
if (len(sys.argv) == 3):
	outpath = sys.argv[2]
else:
	outpath = './out.pdf'

infileh = open(inpath,"r")
infile = infileh.read()
if (infile.startswith("255044462d") != True): # "%PDF-" is the magic number
	print("WARN: not a pdf!")

byte_pdf = bytes.fromhex(infile)

outfile = open(outpath,'wb')
outfile.write(byte_pdf)
outfile.close()
