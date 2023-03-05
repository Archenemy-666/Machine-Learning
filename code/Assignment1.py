from sklearn import tree
from sklearn import datasets
import numpy as np
import matplotlib.pyplot as plt 
from sklearn import metrics 
from sklearn import model_selection

#importing dataset 45019: BioResponse
dia = datasets.fetch_openml(name = 'pc2')
#setting up parameters
parameters = [1,2,5,10,20,60,90,140,200,250]

#plotting graphs 
train_scores = []
test_scores = []
test2_scores = []

for min_sample_leaf in parameters:
    model = tree.DecisionTreeClassifier(criterion="entropy", min_samples_leaf=min_sample_leaf)
    cv = model_selection.cross_validate(model,dia.data,dia.target,scoring=["roc_auc"],cv=10,return_train_score=True)
    train_scores.append(cv["train_roc_auc"].mean())
    #print(cv)
    
    #plugging in testroc
    test2_scores.append(cv["test_roc_auc"].mean())

    
    #evaluating model on predicting test data:
    model.fit(dia.data,dia.target)
    pp = model.predict_proba(dia.data)
    test_score = metrics.roc_auc_score(dia.target, pp[:,1])
    test_scores.append(test_score)

# GridSearch CV
parameters2 = [{"min_samples_leaf":[1,2,5,10,20,140]}] 
model2 = tree.DecisionTreeClassifier()
tuned_model = model_selection.GridSearchCV(model2, parameters2, scoring="roc_auc", cv=10)
cv2 = model_selection.cross_validate(tuned_model,dia.data,dia.target,scoring="roc_auc",cv=10,return_train_score=True)
GridSCV_mean = cv2["test_score"].mean()
tuned_model.fit(dia.data,dia.target)
bestLeaf = tuned_model.best_params_
print(bestLeaf)
print("GridSearchCV_mean:",GridSCV_mean)

plt.plot(parameters,train_scores,label = "train_scores")
plt.plot(parameters,test_scores,label = "test_scores")
plt.plot(parameters,test2_scores,label = "test2_scores")
plt.show()


   
