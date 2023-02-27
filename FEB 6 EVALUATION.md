read ch. 9, there are few things you can skip

# evaluation of machine learning methods 
Goal : estimate how the predictive model will perform when deployed
When deployed the model will be getting new data to make predictions 

__There should be no overlap between training and test data evaluation. Because there is a subset of already predicted data from the training data in the test data. Now the evaluation would be misleading with the accuracy. ( a fraudulant evaluation )__

## purpose of evaluation : 
- to convince the stakeholder to deploy the model
- what is "best" depends on application
	- tolerance are different on for example classification changes from application to application. 
- the evaluation measure and methodology must be aligned with needs
- improper evaluation can be misleading and damaging:
	- mixing train and test data.
	- not using right evaluation measure. 

what is a good way to have no mix of train data to test data
- keeping the things very much unique, this includes the components and attributes individually be unique elements.
- testing data should remain unseen during the entire training process. 

## training and test set:
Random sample a portion of data for testing, use the rest for training, so that we can create a consistant train and test as distrubution is consistant. ( not always a good idea : when the data is progressive, related to time which requires you to keep the data in sequence to the timeline). 

### how do we split the data into the right ratios:
#### cross validation : k-fold validation(k could be 10 i.e. 10 fold).
	- in 10 fold cross validation the data is first randomly divided into 10 equal parts.
	- 9 parts train 1 parts for test.
	- avg result of evaluations are then reported 
How do we combine the accuracy 
- Macro averaginf
- Micro averaging
Computation is ery high for K-fold as k keeps increasing.
least k i.e 2 will mean that the data is very small. -> hence extreams are not suitable for k, hence most 10.

## Validation Set:
Finding best parameter values is called parameter tuning 
what was the parameter in decision tree?

Sometimes a third set is created for parameter tuning called validation set or tuning set or hold out set. 

## Evaluation measures: 
- confusion matrix : target values  v/s prediction values
	- tru positive
	- tru negetive
	- false positive or type I error or "False alarm"
	- false negitive or type II error or "Miss" 

__Sensitivity__ : true positive rate / same as recall  -----> __TP / (TP + FN)__ 
__specificity__ : out of all -ve how many are predicted -ve -----> __TN/(FP + TN)__
__precision__ / +ve predictive model : out of all predicted +ve how many are correct --------> __TP/(TP+FP)
__Recall__ : out of all +ve how many were correctly predicted (extracted) --> same as sensitivity --------> __TP/(FP+FN)__
__Accuracy__ : out of all prediction how many are correct.

Sensitivity & specificity -> to report prediction ability
Precision & recall -> for information extraction 

__==next class : measures for regression tasks==__ 


# Question
- In mixin there is a case of partial mix on patients and visits, here we have intuitively added weightage to he patient over visit an could declare that there is a bleed in among the test and train. How do we not make this decision intuitively. 
- do we re-use the 10 blocks in the 10 fold for test and later to train or vis-a-vis.



note : 
in k fold everytime you are using a validation with each tile/fold the model is pruned or changed always and only accuracy is considered and trianing is lost 
