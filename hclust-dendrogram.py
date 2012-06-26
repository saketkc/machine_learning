import orange
import orngClustering

data = orange.ExampleTable("allchanges.arff")
#sample = data.selectref(orange.MakeRandomIndices2(data, 20), 0)
root = orngClustering.hierarchicalClustering(data)
#orngClustering.dendrogram_draw("allchanges.png", root,labels=[str(d.getclass()) for d in data]) 

