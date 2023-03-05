from sklearn.datasets import fetch_openml
from sklearn import tree
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from sklearn import metrics
from sklearn import model_selection
mol_data = fetch_openml(name = 'pc1')

min_samples_leaf_values = [1, 5, 10, 20, 50,70,100,200,300,400]

train_roc_auc_scores = []
test_roc_auc_scores = []

for min_samples_leaf in min_samples_leaf_values:
    dtc = tree.DecisionTreeClassifier(criterion="entropy", min_samples_leaf=min_samples_leaf)
    cv = model_selection.cross_validate(dtc, mol_data.data, mol_data.target, scoring=["roc_auc"], cv=10, return_train_score=True)
    train_roc_auc_scores.append(cv["train_roc_auc"].mean())
    test_roc_auc_scores.append(cv["test_roc_auc"].mean())
    print(cv)

parameters2 = [{"min_samples_leaf": [1, 5, 10, 20, 50,70,100,200,300,400]}]
model = tree.DecisionTreeClassifier()
tuned_dtc = model_selection.GridSearchCV(model, parameters2, scoring="roc_auc", cv=10)
cv2 = model_selection.cross_validate(tuned_dtc, mol_data.data, mol_data.target, scoring="roc_auc", cv=10,return_train_score=True)
GC_mean = cv2["test_score"].mean()
tuned_dtc.fit(mol_data.data, mol_data.target)
best_case = tuned_dtc.best_params_
best_value = best_case['min_samples_leaf']
print("tuned dtc : ",cv2)

plt.plot(min_samples_leaf_values, train_roc_auc_scores, label="Training ROC AUC")
plt.plot(min_samples_leaf_values, test_roc_auc_scores, label="Test ROC AUC")
plt.xlabel("min_samples_leaf")
plt.ylabel("ROC AUC")

plt.legend()
plt.show()
plt2.plot(best_value,GC_mean,label="bestcase")
plt2.show()
