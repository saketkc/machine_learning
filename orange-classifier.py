import Orange
import orange
import sys
data = orange.ExampleTable(sys.argv[1])
classifier = orange.BayesLearner(data) 
for i in range(5): 
	c = classifier(data[i]) 
	print "original", data[i].getclass(), "classified as", c
