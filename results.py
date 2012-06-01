import matplotlib.pyplot as plt

a={3: 0.2344490412743328, 4: 0.23144170179853213, 5: 0.24592438102327069, 6: 0.2282941017804368, 7: 0.24393457205678365, 8: 0.26501323001936145, 9: 0.27782623835540377, 10: 0.24980046243802492, 11: 0.30587447265896361, 12: 0.29257071186081979, 13: 0.28884076846349543, 14: 0.28503656450981385, 15: 0.29711063099105478, 16: 0.31264773605609286, 17: 0.32147300456547023, 18: 0.32161239559522004, 19: 0.32880311500504905, 20: 0.33726852459851264, 21: 0.36068936228872128, 22: 0.35041539255505355, 23: 0.36290424813818406, 24: 0.36240092893456338, 25: 0.37007066206340827, 26: 0.38332459142150249, 27: 0.38303214482476206, 28: 0.39808890618241688, 29: 0.4033180479334591, 30: 0.39585803670550129, 31: 0.41995408304341886, 32: 0.41714173622716993, 33: 0.41517408919466725, 34: 0.43287690305628518, 37: 0.43302562956385987, 39: 0.44827407431804561, 40: 0.45189102111374269, 41: 0.46875454403203848, 42: 0.46080995870835645, 43: 0.4823718591102179, 46: 0.48006885224843721, 49: 0.50376009006721267,  50: 0.50147863046274799, 57: 0.54181692213806687, 63: 0.56040437084510575}
silhoutte_value = []
cluster_value = []
for key,value in a.iteritems():
	cluster_value.append(key)
	silhoutte_value.append(value)

#plt.figure(1)
ax = plt.subplot(111)
ax.scatter(cluster_value,silhoutte_value,s=20,color='red')
ax.plot(cluster_value, silhoutte_value,lw=2)
ax.set_title('Silhoutte Value v/s Number of Cluster for reactions involving Bond formation/cleavage')
ax.set_xlabel('Number of Clusters')
ax.set_ylabel('Silhoutte Score')
#plt.subplot(211)
#plt.plot(cluster_value, silhoutte_value, 'bo', t2, f(t2), 'k')
plt.savefig('results.png')
plt.show()

