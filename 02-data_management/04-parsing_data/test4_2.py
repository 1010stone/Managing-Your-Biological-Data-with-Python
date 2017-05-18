import sys
args = sys.argv
out_file = open(args[2],'w')

seq = ''
with open (args[1])as FIN:
	for line in FIN:
		if line[0] == '>' and seq == '':				
			header = line
		elif line[0] != '>':
			seq = seq + line
		elif line[0] =='>' and seq != '':
			if seq.strip()[0] == 'M' and seq.count('W')>1:
				out_file.write(header + seq)
				header = line
				seq = ''

if seq.strip()[0] == 'M' and seq.count('W')>1:
					out_file.write(header + seq)
					header = line
					seq = ''

out_file.close()
