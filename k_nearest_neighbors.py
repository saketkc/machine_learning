import numpy as np
import arff
from sklearn import cluster
from sklearn import svm
from sklearn.neighbors import KNeighborsClassifier
def arff_read_to_array(filepath):
	
	arff_file = arff.load(filepath) #Load File
	first_entry = arff_file.next()  #read First Data entry 
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
	return {"target" : target_array,"data": data_array}

def k_nearest_neighbours():
	filepath = "bondchanges.arff"
	all_data = arff_read_to_array(filepath)
	X_data = all_data["data"]
	Y_data = all_data["target"]
	Y_data_map = {}
        new_Y_data = np.array([])
	for index,data in enumerate(Y_data):
		Y_data_map[index] = data
                new_Y_data = np.append(new_Y_data,[index],0) #Create
	X_training = X_data[:0.1*len(X_data)]
	Y_training = new_Y_data[:0.1*len(Y_data)]
	print X_training
	print 
        print Y_training
	X_test = X_data[0.9*len(X_data):]
	Y_test = new_Y_data[0.9*len(Y_data):]
	#svc = svm.SVC(C=1, kernel='')
	knn = KNeighborsClassifier() 
	print knn.fit(X_training, Y_training).score(X_test,Y_test)

filepath = "bondchanges.arff"
#print arff_read_to_array(filepath)
k_nearest_neighbours()
