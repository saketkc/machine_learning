import csv
reader = csv.reader(open("ec_clustering_tree.txt","r"),dialect='excel-tab')
matrix = [[0]* 6 for x in xrange(0,6)]
for i,row in enumerate(reader):
	if i>0:
		ec=[0,0,0,0,0,0]
		for j,element in enumerate(row):
			if j>1:
				ec[j-1] = int(element)

		for index, element in ec:
			if
		for j,element in enumerate(matrix):
			matrix[j] = [a+b for a,b in zip(ec,matrix[j])]
				
print matrix
	
