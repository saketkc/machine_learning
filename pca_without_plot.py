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
import numpy as np
import pylab as pl
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
reduced_data = PCA(n_components=2).fit_transform(data_array)
kmeans = KMeans(init='k-means++', k=6, n_init=1).fit(reduced_data)
print len(reduced_data)
print reduced_data[:,0]
h = .02     # point in the mesh [x_min, m_max]x[y_min, y_max].

# Plot the decision boundary. For that, we will asign a color to each
x_min, x_max = reduced_data[:, 0].min() + 1, reduced_data[:, 0].max() - 1
y_min, y_max = reduced_data[:, 1].min() + 1, reduced_data[:, 1].max() - 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))

# Obtain labels for each point in mesh. Use last trained model.
Z = kmeans.predict(np.c_[xx.ravel(), yy.ravel()])
pl.figure(1)
pl.clf()
pl.plot(reduced_data[:, 0], reduced_data[:, 1], 'k.',color='red', markersize=2)
pl.show()
for i,label in enumerate(Z):
	print i,label 

