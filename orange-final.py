import orange
import orngIO
import orngClustering
data = orngIO.loadARFF('bond.new.arff')
def callback(km):
    print "Iteration: %d, changes: %d, score: %.4f" % (km.iteration,km.nchanges, km.score)
#km_random = orngClustering.KMeans(data, centroids = 7,minscorechange=0, inner_callback=callback)
print "DIVERSITY"
km_diversity = orngClustering.KMeans(data, centroids = 7,minscorechange=0, initialization=orngClustering.kmeans_init_diversity, inner_callback=callback)
print "HC"
#km_hc = orngClustering.KMeans(data, centroids = 7,minscorechange=0, initialization=orngClustering.KMeans_init_hierarchicalClustering(n=100), inner_callback=callback)
plot = orngClustering.plot_silhouette(km_hc, "kmeans-hc.png")
#plot1 = orngClustering.plot_silhouette(km_diversity, "kmeans-diversity.png")

for index,row in enumerate(km_diversity.data):
    ec_number_rxnid = row[-1]
    ec_number = (".").join(ec_number_rxnid.split('_')[0].split('.')[:3])
#print km_random.clusters[-10:]

#print km_diversity.clusters[-10:]
print km_hc.clusters[-10:]




