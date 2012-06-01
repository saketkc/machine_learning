import numpy as np
import arff

from sklearn import cluster
import math
from collections import defaultdict
from sklearn import metrics
from sklearn.cluster import KMeans
from sklearn.datasets import load_digits
from sklearn.decomposition import PCA
from sklearn.preprocessing import scale
filepath = "bondchanges.arff"
arff_file = arff.load(filepath)
first_entry = arff_file.next()
data_array = np.array([first_entry._values[:-1]])
target_array = np.array([first_entry._values[-1]])
target_list = [first_entry._values[-1][0]]
ecnumbers = []
ec_first_number = []
for row in arff_file:
    data_values = row._values[:-1]
    target_values = row._values[-1]
    ecnumber = target_values.split('_')[0]
    if ecnumber not in ecnumbers :
	ecnumbers.append(ecnumber)
 
    target_list.append(ecnumber.split('.')[0])
    data_array = np.append(data_array,[data_values],0)
    target_array = np.append(target_array,[target_values],0)
    
arff_file.close()
l = len(target_list)-1
print "Total EC NUMBERS :", len(ecnumbers)
#cluster_values = []
#silhoutte_values = []
 
k_means = cluster.KMeans(init='k-means++', k=7, n_init=1000)
k_means.fit(data_array)
ec_classes = {}
k_means_labels = k_means.labels_
i =0
for label in k_means_labels:
        corresp_ec_row = target_list[i]
        if ec_classes.get(corresp_ec_row):
		ec_classes[corresp_ec_row].append(label)
        else:
		ec_classes[corresp_ec_row]= [label]
	i = i+1
               
	
#print k_means_label
#print "ECCLASSES,", ec_classes
for key,value in ec_classes.iteritems():
	countcluster_1 = value.count(0)
	countcluster_2 = value.count(1)
	countcluster_3 = value.count(2)
	countcluster_4 = value.count(3)
	countcluster_5 = value.count(4)
	countcluster_6 = value.count(5)
	countcluster_7 = value.count(6)
	print key, "=> ", countcluster_1," , ",countcluster_2," , ",countcluster_3," , ",countcluster_4," , ",countcluster_5," , ",countcluster_6," , ",countcluster_7
	
#ax = plt.subplot(111)
#number
#ax.plot(
#ax.scatter(cluster_value,silhoutte_value,s=20,color='red')
#k_means_labels_unique = len(np.unique(k_means_labels))
#sl  = metrics.silhouette_score(data_array, k_means_labels, metric='euclidean')

