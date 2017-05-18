'''

Read a multiple FASTA file and extract human sequences.

-----------------------------------------------------------
(c) 2013 Allegra Via and Kristian Rother
    Licensed under the conditions of the Python License

    This code appears in section 4.4.4 of the book
    "Managing Biological Data with Python".
-----------------------------------------------------------
'''
'''
将header和seq分别读取。并且根据程序流，将两者一一对应。如果"Homo sapiens"在header中，就写入文件。
最后一次记录的有效信息需要单独读入
'''
fasta_file = open('SwissProt.fasta','r')
out_file = open('SwissProtHuman.fasta','w')
seq = ''
#初始化字符串
for line in fasta_file:
#对于每一行
    if line[0] == '>' and seq == '':
        #处理第一行。以>开头，且字符串为空，该行作为header。
        header = line
    elif line [0] != '>':
        #如果第一个字符串不是>，即不是header的行，行加到seq中，作为序列
        seq = seq + line

    #读到了下一条序列，此时line是下一条序列的标题，header记录的是前一条序列的标题，seq记录的是前一条序列的序列信息（不为空）。
    #如果"Homo sapiens"在标题中，将header和seq写入文件。
    #序列初始化，目前读到的这行作为新的header
    elif line[0] == '>' and seq != '':
        if "Homo sapiens" in header:
            out_file.write(header + seq)
        seq = ''
        header = line
#读到了最后一个标题，前一条有效信息写入了文件。此时标题作为header，序列初始化，然后依次读取每一条序列。
#一直在第一个elif执行，将最后一条序列全部读入seq。读完所有的信息后，分别记录在header和seq中。


# take care of the very last record of the input file
#写入最后一次读入的有效序列。
if "Homo sapiens" in header:
    out_file.write(header + seq)
out_file.close()
