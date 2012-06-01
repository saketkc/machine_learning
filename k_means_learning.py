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
for row in arff_file:
    data_values = row._values[:-1]
    target_values = row._values[-1]
    target_list.append(target_values)
    data_array = np.append(data_array,[data_values],0)
    target_array = np.append(target_array,[target_values],0)
arff_file.close()
l = len(target_list)-1
silhoutte_dict = {}
#cluster_values = []
#silhoutte_values = []

for kc in range(3,70):
	k_means = cluster.KMeans(k=kc)
	k_means.fit(data_array)
	k_means_labels = k_means.labels_
	k_means_labels_unique = len(np.unique(k_means_labels))
	if kc==k_means_labels_unique:  
		sl  = metrics.silhouette_score(data_array, k_means_labels, metric='euclidean')
                if not math.isnan(float(sl)):
       	        	silhoutte_dict[kc] = sl
        	#cluster_values.append(kc)
                #silhoutte_values.append(sl)
#print "Cluster values "
#print cluster_values
#print "Silhoute values "
#print silhoutte_values
print "Cluster-Sihoutte Dict"
print silhoutte_dict
#sl_max = max(silhoutte_values)
key,value = max(silhoutte_dict.iteritems(), key=lambda x:x[1])
print "Max SL => ", value
print  "Corresponding CL => ", key
 
#fig = pl.figure(figsize=(8, 3))        
#ax = fig.add_subplot(1, 3, 1)
#plt.plot(cluster_values,silhoutte_values)
#pl.show()
#plt.savefig('cluster.png')
	#k_means_cluster_centers = k_means.cluster_centers_
	#first_ec_number_map = defaultdict(list)
#while (l>=0):
 #  first_ec_number = target_list[l].split('.')[0]
  # first_ec_number_map[first_ec_number].append(k_means.labels_[l])
	
   #l = l-1

#print  first_ec_number_map
#colors = ['#FF0000','#00FF00','#0000FF','#FFFF00','#00FFFF','#000000']
#fig = pl.figure(figsize=(8, 3))
#
#for k, col in zip(range(6), colors):
 #   my_members = k_means_labels == k
    #print my_members
  #  cluster_center = k_means_cluster_centers[k]
  #  ax.plot(X[my_members, 0], X[my_members, 1], 'w',  markerfacecolor=col, marker='.')
#pl.scatter(data_array[:, 0], data_array[:, 1])
#pl.scatter(k_means.cluster_centers_[:, 0], k_means.cluster_centers_[:, 1], marker='o', s=100)
#pl.show()
#print data_array[:, 0]


