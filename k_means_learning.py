import numpy as np
import arff
from sklearn import cluster
filepath = "bondchanges.arff"
arff_file = arff.load(filepath)
first_entry = arff_file.next()
#length_of_row = len(first_entry)-1
data_array = np.array([first_entry._values[:-1]])
target_array = np.array([first_entry._values[-1]])
unique_target_list = {first_entry._values[-1][0]:0}
i = 1
for row in arff_file:

    data_values = row._values[:-1]
    target_values = row._values[-1]

    if target_values not in unique_target_list:
        unique_target_list[target_values] = i
        i+=1
    print target_values
    data_array = np.append(data_array,[data_values],0)
    target_array = np.append(target_array,[target_values],0)

arff_file.close()
#print data_array
#print target_array
print "STARTING CLUSTERING1"
k_means = cluster.KMeans(k=len(unique_target_list))
print "STARTING CLUSTERING2"
k_means.fit(data_array)
a= []
for value in unique_target_list.itervalues():
    a.append(value)
print "STARTING CLUSTERING"

print a[::10]
print k_means.labels_[::10]




