import sys
a = open(sys.argv[1].split('.')[0]+'-mod.tab','a')
i=0
for line in open(sys.argv[1],'r'):
    line = line.replace("\n","")
    split_line = line.split("\t")
    #print len(split_line)
    if i==0:
        string_to_write = "\"ecs\""
        for element in split_line[0:-1]:
            string_to_write += "\t" + element
        string_to_write+="\n"
    elif i>=3 :
        p,q = 0,-1
        split_line[q],split_line[p] = split_line[p],split_line[q]
        string_to_write = ("\t").join(map(str,split_line))+"\n"
    a.write(string_to_write)
    i+=1
    
a.close()

