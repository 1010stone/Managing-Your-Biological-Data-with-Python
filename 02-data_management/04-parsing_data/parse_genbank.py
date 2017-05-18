'''

Read a Genbank file and convert it to a FASTA file.

-----------------------------------------------------------
(c) 2013 Allegra Via and Kristian Rother
    Licensed under the conditions of the Python License

    This code appears in section 4.4.3 of the book
    "Managing Biological Data with Python".
-----------------------------------------------------------
'''
#打开文件
genbank_file = open("AY810830.gb")
output_file = open("AY810830.fasta","w")
#定义标签
flag = False
for line in genbank_file:
    if line[0:9] == 'ACCESSION':
        #提取accession名
        accession = line.split()[1].strip()
        #将格式化的accession写入文件
        output_file.write('>' + accession + '\n')
    #如果行为'ORIGIN'，则标签为真.  读完ORIGIN后，flag=True。以下读取每一行，都会只执行elif flag部分
    if line[0:6] == 'ORIGIN': 
        flag = True
    #如果标签为真，空格作为分隔符分隔
    elif flag:
        fields = line.split()
        #如果不为空，取出从每行第二个元素开始的所有元素，大写，加换行符，写入文件。能避免带入序列后面的空行
        if fields != []:
            seq = ''.join(fields[1:])
            output_file.write(seq.upper() + '\n')
            
genbank_file.close()
output_file.close()


