import numpy as np
from scipy.cluster.vq import kmeans2
from scipy.spatial.distance import pdist, squareform
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
import arff
from sklearn import cluster
import pylab as pl
from collections import defaultdict
def silhouette(X, cIDX):
    """
    Computes the silhouette score for each instance of a clustered dataset,
    which is defined as:
        s(i) = (b(i)-a(i)) / max{a(i),b(i)}
    with:
        -1 <= s(i) <= 1

    Args:
        X    : A M-by-N array of M observations in N dimensions
        cIDX : array of len M containing cluster indices (starting from zero)

    Returns:
        s    : silhouette value of each observation
    """

    N = X.shape[0]              # number of instances
    K = len(np.unique(cIDX))    # number of clusters

    # compute pairwise distance matrix
    D = squareform(pdist(X))

    # indices belonging to each cluster
    kIndices = [np.flatnonzero(cIDX==k) for k in range(K)]

    # compute a,b,s for each instance
    a = np.zeros(N)
    b = np.zeros(N)
    for i in range(N):
        # instances in same cluster other than instance itself
        a[i] = np.mean( [D[i][ind] for ind in kIndices[cIDX[i]] if ind!=i] )
        # instances in other clusters, one cluster at a time
        b[i] = np.min( [np.mean(D[i][ind]) 
                        for k,ind in enumerate(kIndices) if cIDX[i]!=k] )
    s = (b-a)/np.maximum(a,b)

    return s
def main():
    # load Iris dataset
    #data = datasets.load_iris()
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
    k_means = cluster.KMeans(k=10)
    k_means.fit(data_array)
    k_means_labels = k_means.labels_
    k_means_cluster_centers = k_means.cluster_centers_
    first_ec_number_map = defaultdict(list)
    while (l>=0):
	first_ec_number = target_list[l].split('.')[0]
        first_ec_number_map[first_ec_number].append(k_means.labels_[l])
	l = l-1

    X = data_array

    # cluster and compute silhouette score
    K = 4
    #C, cIDX = kmeans2(X, K)
    cIDX = np.array(range(4))
    s = silhouette(X,cIDX)

    # plot
    order = np.lexsort((-s,cIDX))
    indices = [np.flatnonzero(cIDX[order]==k) for k in range(K)]
    ytick = [(np.max(ind)+np.min(ind))/2 for ind in indices]
    ytickLabels = ["%d" % x for x in range(K)]
    cmap = cm.jet( np.linspace(0,1,K) ).tolist()
    clr = [cmap[i] for i in cIDX[order]]

    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.barh(range(X.shape[0]), s[order], height=1.0, 
            edgecolor='none', color=clr)
    ax.set_ylim(ax.get_ylim()[::-1])
    plt.yticks(ytick, ytickLabels)
    plt.xlabel('Silhouette Value')
    plt.ylabel('Cluster')
    plt.show()

if __name__ == '__main__':
    main()
