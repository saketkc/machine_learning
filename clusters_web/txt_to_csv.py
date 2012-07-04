import sys
import re
filereader =open(sys.argv[1],'r')
filewriter = open(sys.argv[1].split('.')[0]+".csv",'a')
i=0
for line in filereader:
	line = line.strip()
	line = re.sub(' +',';',line)
	line_split = line.split(";")
	if len(line_split)>1:
		if i==0:
			filewriter.write("6.1,6.2,6.3,6.4,6.5,6.6\n")
		if i>0:
			filewriter.write(str(i)+",")
			for column in line_split[1:-1]:
				string = column+","
				filewriter.write(string)
			filewriter.write(line_split[-1]+'\n')
	i+=1
		
		

