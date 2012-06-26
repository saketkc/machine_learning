a = open('bond-mod.tab','a')
i=0
for line in open('bond.tab','r'):
    line = line.replace("\n","")
    split_line = line.split("\t")
    #print len(split_line)
    if i==0:
        string_to_write = "ecs" + "\t" + ("\t").join(split_line[0:-1])+"\n"
        
    else :
        p,q = 0,-1
        split_line[q],split_line[p] = split_line[p],split_line[q]
        string_to_write = ("\t").join(map(str,split_line))+"\n"
    a.write(string_to_write)
    i+=1
    
a.close()

