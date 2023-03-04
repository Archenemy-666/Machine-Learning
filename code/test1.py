from sklearn import datasets
from sklearn import tree
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from sklearn import metrics
from sklearn import model_selection

dia = datasets.fetch_openml(data_id = 45086)
mytree = tree.DecisionTreeClassifier(criterion="entropy")

mytree.fit(dia.data,dia.target)

parameters = [{"min_samples_leaf":[1,4,6,12]}]
dtc = tree.DecisionTreeClassifier()
tuned_dtc = model_selection.GridSearchCV(dtc, parameters, scoring="roc_auc", cv=10)
cv = model_selection.cross_validate(tuned_dtc, dia.data, dia.target, scoring="roc_auc", cv=10,return_train_score=True)
print(cv["test_score"].mean())

tuned_dtc.fit(dia.data, dia.target)
print(tuned_dtc.best_params_)

dtc2 = tree.DecisionTreeClassifier()
cv2 = model_selection.cross_validate(tuned_dtc,dia.data,dia.target,scoring=["accuracy","roc_auc"],cv=10)
accuracy_mean = cv2["test_accuracy"].mean()
test_roc_auc_mean = cv2["test_roc_auc"].mean()
print(accuracy_mean,test_roc_auc_mean)
print(cv2["test_accuracy"],cv2["test_accuracy"])