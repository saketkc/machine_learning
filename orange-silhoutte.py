import orange
import orngIO
import orngClustering
data = orngIO.loadARFF('bond.new.arff')
for i  in range(0,400):
    km_hc = orngClustering.KMeans(data, centroids = 7,minscorechange=0, initialization=orngClustering.KMeans_init_hierarchicalClustering(n=100))
    
