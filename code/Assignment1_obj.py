from sklearn import tree
from sklearn import datasets
import numpy as np
import matplotlib.pyplot as plt 
from sklearn import metrics 
from sklearn import model_selection

#importing dataset 45019: BioResponse
#setting up parameters
def roc_plot(dia):#plotting graphs 
    train_scores = []
    test_scores = []
    test2_scores = []
    parameters = [1,2,5,10,20,60,90,140,200,250]
    for min_sample_leaf in parameters:
        model = tree.DecisionTreeClassifier(criterion="entropy", min_samples_leaf=min_sample_leaf)
        cv = model_selection.cross_validate(model,dia.data,dia.target,scoring=["roc_auc"],cv=10,return_train_score=True)
        train_scores.append(cv["train_roc_auc"].mean())
    #plugging in testroc
        test2_scores.append(cv["test_roc_auc"].mean())
                
    
    #evaluating model on predicting test data:
        model.fit(dia.data,dia.target)
        pp = model.predict_proba(dia.data)
        test_score = metrics.roc_auc_score(dia.target, pp[:,1])
        test_scores.append(test_score)
    print("test_scores : ",cv["test_roc_auc"])
    print("test_scores_mean : ",cv["test_roc_auc"].mean())
    print("test2_scores_mean : ",test2_scores)
    return train_scores,test2_scores,test_score,parameters

# GridSearch CV
def GridSearch(parameters2,dia):
    model2 = tree.DecisionTreeClassifier()
    tuned_model = model_selection.GridSearchCV(model2, parameters2, scoring="roc_auc", cv=10)
    cv2 = model_selection.cross_validate(tuned_model,dia.data,dia.target,scoring="roc_auc",cv=10,return_train_score=True)
    GridSCV_mean = cv2["test_score"].mean()
    tuned_model.fit(dia.data,dia.target)
    bestLeaf = tuned_model.best_params_
    print("GridSearchCV test score : ",cv2["test_score"])
    print("GridSearchCV test score mean : ",GridSCV_mean)
    return bestLeaf, GridSCV_mean

def about(dia):
    mytree = tree.DecisionTreeClassifier()
    mytree.fit(dia.data,dia.target)
    predictions = mytree.predict(dia.data)
    print(metrics.accuracy_score(dia.target, predictions))
    print(metrics.f1_score(dia.target, predictions, pos_label='TRUE'))
    print(metrics.precision_score(dia.target, predictions, pos_label="TRUE"))
    print(metrics.recall_score(dia.target, predictions, pos_label="TRUE"))
    

def main():
    dia = datasets.fetch_openml(name = 'pc2')

    parameters2 = [{"min_samples_leaf":[1,2,5,10,20,60,90,140,200,250]}] 
    
    train_scores,test2_scores,test_scores,parameters = roc_plot(dia)
    best_leaf, GridMean = GridSearch(parameters2,dia)
    
    #optimal leaf for marking
    optmial_leaf = best_leaf['min_samples_leaf']
    
    #------------------------------------------------------------------

    plt.plot(parameters,train_scores,label = "train_scores")
    plt.plot(parameters,test2_scores,label = "test2_scores") 
    plt.axvline(x=optmial_leaf,color='black',linestyle='--',label = 'optimal_leaf')
    plt.fill_between(parameters, test2_scores, train_scores, where=test_scores <= train_scores, interpolate=True,color ='red', alpha=0.2, label='min_samples_leaf') 
    plt.fill_between(parameters, test2_scores, train_scores, where=test_scores > train_scores, interpolate=True, color='green', alpha=0.2,label='ROC_AUC')
    plt.legend()
    plt.show()

    about(dia)
if __name__ == "__main__":
    main()
