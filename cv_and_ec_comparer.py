ecs=[]
cvs=[]
for line in open('allecs.txt','r'):
    line = line.replace("\n","")
    ec = line.split(" ")
    ecs.append(ec[1])
for line in open('allclustervalues.txt','r'):
    line = line.replace("\n","")
    cv = line.split(" ")
    cvs.append(cv[1])
maps={}
for i,ec in enumerate(ecs):
    ec_1 = ec[1]
    cv = cvs[i]
    if cv in maps.keys():
       
       if ec_1 in maps[cv].keys():
           maps[cv][ec_1]+=1
       else:
           maps[cv][ec_1]=1
    else:
        maps[cv]={ec_1:1}

matrix = [[0]*6 for x in xrange(0,len(maps))]
for index,key in enumerate(maps):
	for cvkey in maps[key].keys():
		matrix[index][int(cvkey)-1]=maps[key][cvkey]


print "Cluster Number ","EC1 " ,"EC2 ","EC3 ","EC4 ","EC5 ","EC6 "
for index,j in enumerate(matrix):
	string = str(index+1)+" "
	for value in j:
		string+=str(value)+" "
	print string
	
    	

