Why not make multiple decision trees, then all the predictions will be combined.
How is this better/worse.

A machine learning model that combines several models is called an ensamble or a community. 
- cancels out random errors
- reinforce correct prediction 

The individual models in an ensamble must be __diverse__, i.e. differ in their prediction. 
Each individual model makes predictions __independent__ of the other models.
Each model must be good, at least __better than random guessing__. ( at least auc = 0.51, 0.01 more than randomness)

Two types of Ensambles:
- Homogenous 
- Hetrogenous

## Homogenous Ensambles:
Using a single ML method but manipulate training data, i.e. the same learner. where as different learners make the ensamble hetrogenous. 
homogenous is split into:
1. Bagging 
2. Boosting 

### bagging:
Random resampling the training data.
A training set of size n, create m samples of size n by drawing n examples from the original data, with replacement.
n = 1,2,3,4,5 --> you pick 2,3,3,4,1 and 4,5,1,2,2 and 3,5,3,4,4 --> Learner --> model 1 , model 2, model 3 --> converge and release an ensamble 

Bagging decreases error by decreasing the variance in the resilt due to unstable learners, methods (like decision trees) whose output can cahnge dramatically. 
Any machine Learning method can be bagged
decision trees are particularly suited for bagging. --> result is called bagged decision trees.

#### Random Forest: (_better than single decision tree_)
sampling the features is called subspace sampling. 
A combination if bagging, subspace sampling, and decision tree --> Random Forest

### Boosting 
Developed to guarentee performance improvements on fitting and training data for a weak learner that only needs to generate in hypothesis with a training accuracy greater than 0.5.
Examples are given weights, At each iteration, a new hypothesis is learned and the examples are reweighted to focus the system on examples that are most recently learned classifier got wrong.

#### Algorithm:
1. General loop : set uniform weights(sum to 1)
	1. learn a model mt from the weighterd examples 
	2. increase weights of examples that predicted wieghts incorrectly
	3. decrease weights the ones that predicted correct.

#### Gradient Boosting:
iteratively trains the models, each specializing in the areas earlier models struggled with:
- common to use decision stumps, only one level deep decision tree, withthe gradient boosting
- can be extended for classification as well. 

for regression: 
- simply first model predicts the average target value.
- 
- 


___all the models are available in sklearn___