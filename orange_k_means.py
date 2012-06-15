import Orange
bondorder  =  Orange.data.Table("bondchanges.arff")
rndind = Orange.data.sample.SubsetIndices2(bondorder, p0=0.8)
train = bondorder.select(rndind, 0)
test = bondorder.select(rndind, 1)

knn = Orange.classification.knn.kNNLearner(train, k=10)
for i in range(50):
    instance = test.random_example()
    print instance.getclass(), "=>",  knn(instance)
