import sys
args = sys.argv

filename = open(args[1],'r')

seq = ''

for line in filename:
	#如果以>开头，seq为空，标题作为header
	if line[0] == '>' and seq == '':
		header = line
		accession = str(header.split('|')[1])
	#如果不以>开头，则在读取序列。新序列放在seq中
	elif line[0] != '>' :
		seq = seq + line
	#如果读到下一个标题，则将目前的header和seq写入上一个标题命名的文件中
	elif line[0] == '>' and seq != '':
		with open(accession,'w') as FIN:
			FIN.write(header + seq)
			#重新命名标题，seq初始化
			seq = ''
			header = line
			accession = str(header.split('|')[1])
with open(accession,'w') as FIN:
	FIN.write(header + seq)
