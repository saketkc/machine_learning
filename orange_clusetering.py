import Orange

iris = orange.ExmapleTable("bond.new.arff")
import orngMDS

matrix = orange.SymMatrix(len(iris))
matrix = Orange.distance.distance_matrix(iris, Orange.distance.Euclidean)

clustering = Orange.clustering.hierarchical.HierarchicalClustering()
clustering.linkage = Orange.clustering.hierarchical.AVERAGE
root = clustering(matrix)

root.mapping.objects = iris
sample = iris.select(Orange.data.sample.SubsetIndices2(iris, 20), 0)
topmost = sorted(Orange.clustering.hierarchical.top_clusters(root, 2), key=len)
my_colors = [(255,0,0), (0,255,0), (0,0,255)]
labels = [str(d.get_class()) for d in sample]
top_clusters = Orange.clustering.hierarchical.top_clusters(root, 3)

for cluster in topmost:
    dist = Orange.statistics.distribution.Distribution(iris.domain.class_var, \
        [ ex for ex in cluster ])
    for e, d in enumerate(dist):
	
        print "%s: %3.0f " % (iris.domain.class_var.values[e], d),
    print

colors = dict([(cl, col) for cl, col in zip(top_clusters, my_colors)])
Orange.clustering.hierarchical.dendrogram_draw(
    "hclust-colored-dendrogram.png", root, data=sample, labels=labels, 
    cluster_colors=colors, color_palette=[(0,255,0), (0,0,0), (255,0,0)], 
    gamma=0.5, minv=2.0, maxv=7.0)

