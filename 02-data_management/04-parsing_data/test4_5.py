import sys
args = sys.argv
flag = False
seq = ''

out_file = open(args[2],'w')
with open (args[1]) as FIN:
	for line in FIN:
		if line[0:9] == 'ACCESSION':
			header = line.split()[1].strip()
			out_file.write('>'+header+'\n')
		elif line[0:6] == 'ORIGIN':
			flag = True
		elif flag :
			fields = line.split()
			if fields != '':
				seq = ''.join(fields[1:])
				out_file.write(seq.upper() + '\n')
out_file.close()