import sys
args = sys.argv

A,T,C,G = 0,0,0,0
seq = ''

with open(args[1])as FIN:
	for line in FIN:
		if line[0] == '>' and seq == '':
			header = line
		elif line[0] != '>':
			seq = seq + line.strip().upper()
		elif line[0] == '>' and seq != '':
			A = str(seq).count('A')/len(str(seq))
			T = str(seq).count('T')/len(str(seq))
			C = str(seq).count('C')/len(str(seq))
			G = str(seq).count('G')/len(str(seq))
			print(header,A,T,C,G)

			header = line
			seq = ''
A = str(seq).count('A')/len(str(seq))
T = str(seq).count('T')/len(str(seq))
C = str(seq).count('C')/len(str(seq))
G = str(seq).count('G')/len(str(seq))
print(header,'%4.2f	%4.2f	%4.2f	%4.2f'%(A,T,C,G))
