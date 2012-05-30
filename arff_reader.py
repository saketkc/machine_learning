import numpy as np
import arff
from sklearn import cluster

def get_data_and_target(filepath):
	filepath = "bondchanges.arff"
	arff_file = arff.load(filepath)
	first_entry = arff_file.next()
	length_of_row = len(first_entry)-1
	data_array = np.array([first_entry._values[:length_of_row]])
	target_array = np.array(first_entry._values[length_of_row:])
	unique_target_list = {first_entry._values[length_of_row:][0]:0}
	i = 1
	for row in arff_file:

		data_values = row._values[:length_of_row]
		target_values = row._values[length_of_row:]

		if target_values[0] not in unique_target_list:
			unique_target_list[target_values[0]] = i
			i+=1
		print target_values
		data_array = np.append(data_array,[data_values],0)
		target_array = np.append(target_array,target_values,0)

	arff_file.close()
	return {"data": data_array, "target" : target_array}
	
