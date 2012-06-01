import numpy as np
from scipy.cluster.vq import kmeans2
from scipy.spatial.distance import pdist, squareform
from scikits.learn import datasets
import matplotlib.pyplot as plt
from matplotlib import cm
def silhouette_coefficient(y, D):
   
    return np.mean(silhouette_samples(y, D))


def silhouette_samples(y, D):
    
    n = y.shape[0]
    A = np.array([_intra_cluster_distance(y, D[i], i)
                  for i in range(n)])
    B = np.array([_nearest_cluster_distance(y, D[i], i)
                  for i in range(n)])
    return (B - A) / np.maximum(A, B)


def _intra_cluster_distance(y, d, i):
    
    label = y[i]
    print "dD2",d
    a = np.mean([d[j] for j in range(len(d))
                 if y[j] == label and not i == j])
    return a


def _nearest_cluster_distance(y, d, i):
    label = y[i]
    b = np.min(np.mean([d[j] for j in range(len(d))
                        if y[j] == cur_label])
               for cur_label in set(y) if not cur_label == label)
    return b
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
    print "n ",N

    K = len(np.unique(cIDX))    # number of clusters
    print "k ",K
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
    data = datasets.load_iris()
    X = data['data']

    # cluster and compute silhouette score
    K = 8
    C, cIDX = kmeans2(X, K)
    print cIDX
    D = pairwise_distances(X, metric='euclidean')
    s = silhouette_coefficient(cIDX,D)
    silhouette = silhouette_score(D, y, metric='precomputed')
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
