from sklearn import *
digits = datasets.load_digits()
digits_X = digits.data
digits_Y = digits.target
sample_length = len(digits_X)
digits_Y_train = digits_Y[:0.9*sample_length]
digits_Y_test = digits_Y[0.9*sample_length:]
digits_X_train = digits_X[:0.9*sample_length]
digits_X_test = digits_X[0.9*sample_length:]
knn = neighbors.KNeighborsClassifier()
print knn.fit(digits_X_train,digits_Y_train).score(digits_X_test,digits_Y_test)
logistic = linear_model.LogisticRegression()
print logistic.fit(digits_X_train,digits_Y_train).score(digits_X_test,digits_Y_test)
