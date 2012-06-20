import orange
import Orange
import orngIO
import orngClustering
import sys
import getopt
def load_data(filepath):
    data = orngIO.loadARFF(filepath)
    return data
    

def perform_clustering(data,initialization=orngClustering.kmeans_init_diversity,cluster_size=6,minscorechange=0,):
    km = orngClustering.KMeans(data, centroids = cluster_size,minscorechange=0, initialization=initialization)
    #orngClustering.KMeans_init_hierarchicalClustering(n=100))
    callback(km,cluster_size)
    #km_random = orngClustering.KMeans(data, centroids = 7,minscorechange=0, inner_callback=callback)
    #km_diversity = orngClustering.KMeans(data, centroids = 7,minscorechange=0, initialization=orngClustering.kmeans_init_diversity, inner_callback=callback)


    

def callback(km,cluster_size):
    clusters = km.clusters
    height = cluster_size
    width = 6 ## EC CLASSES !
    count_matrix =  [[0]*width for x in xrange(0,height)]

    for i in range(0,len(clusters)):
        ec_with_rmrid = str(km.data[i][-1])
        ec_1 = ec_with_rmrid[0]
        cluster = clusters[i] 
        count_matrix[cluster][int(ec_1)-1] +=1
        #for j in clusters
        #print clusters[i], " => ", km.data[i][-1]
    #print count_matrix
    col_totals = [ sum(x) for x in zip(*count_matrix) ]
    
    for index,x in enumerate(count_matrix):
        row_sum = sum(x)
        count_matrix[index] = ["{0:.2f}".format(float(a)/b) for a,b in zip(x,col_totals)]
        print count_matrix[index] , " => ", row_sum

    max_counts = [max(a,b) for a,b in zip(*count_matrix)]
    print max_counts
    print "**********************"
   
   


def main(argv):
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hi:c:", ["help","c"])        
    except getopt.GetoptError, err:
        print str(err)        
        print """python orange-final.py -i <input file path> -c <number of clusters> """
        sys.exit(2)
    for o, a in opts:
        
        if o in ("-h","--help"):
            print """python orange-final.py -i <input file path> -c <number of clusters> """
        elif o in ("-i","--input"):            
            filepath = a
        elif o in("-c","--clusters"):
            clusters = a
        else :
            assert False,"unhandle option"
    if clusters!='' and filepath!='':
        data = load_data(filepath)
        for i in range(6,400):
            perform_clustering(data,cluster_size=int(i))        

        
         
        


if __name__=="__main__":
    main(sys.argv)
        
        



