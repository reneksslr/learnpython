from sklearn import tree, ensemble, naive_bayes
from sklearn.metrics import accuracy_score
import numpy as np

clf_1 = tree.DecisionTreeClassifier()
clf_2 = ensemble.AdaBoostClassifier()
clf_3 = ensemble.RandomForestClassifier()
clf_4 = naive_bayes.GaussianNB()

# CHALLENGE - create 3 more classifiers...
# 1
# 2
# 3

# [height, weight, shoe_size]
X = [[181, 80, 44], [177, 70, 43], [160, 60, 38], [154, 54, 37], [166, 65, 40],
     [190, 90, 47], [175, 64, 39],
     [177, 70, 40], [159, 55, 37], [171, 75, 42], [181, 85, 43]]

Y = ['male', 'male', 'female', 'female', 'male', 'male', 'female', 'female',
     'female', 'male', 'male']

X_T = [[190, 70, 43],[154, 75, 42],[181,65,40]]
Y_T = ['female','male','male']

# CHALLENGE - ...and train them on our data
clf_1 = clf_1.fit(X, Y)
clf_2 = clf_2.fit(X, Y)
clf_3 = clf_3.fit(X, Y)
clf_4 = clf_4.fit(X, Y)


prediction_1 = clf_1.predict(X_T)
prediction_2 = clf_2.predict(X_T)
prediction_3 = clf_3.predict(X_T)
prediction_4 = clf_4.predict(X_T)

classifiers = ['Decision Tree','AdaBoost','RandomForest','GaussianNB']
acc_clf_1 = accuracy_score(prediction_1,Y_T)
acc_clf_2 = accuracy_score(prediction_2,Y_T)
acc_clf_3 = accuracy_score(prediction_3,Y_T)
acc_clf_4 = accuracy_score(prediction_4,Y_T)

print("Entscheidungsbaum:",prediction_1,acc_clf_1)
print("AdaBoostClassifier:",prediction_2,acc_clf_2)
print("RandomForestClassifier:",prediction_3,acc_clf_3)
print("GaussianNB:",prediction_4,acc_clf_4)

acc = np.array([acc_clf_1,acc_clf_2,acc_clf_3,acc_clf_4])
max = np.argmax(acc)
print(classifiers[max] + ' ftw !!!')

# CHALLENGE compare their reusults and print the best one!
