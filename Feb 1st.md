# Extensions and variations: Continuous features 
## How to handle continuous features:
- set ranges for numeric features / continuous 
	- sort and then ask where to split ? 
		- usually average split (middle)

## How to handle continuous targets (regression):
- decision trees tweeked to work with regression, which originally is a classification tool. 
	- classification trees have discrete (nominal) class labels, Regression trees allow continuous (numeric)
	- if the node value equals the average , we use that node. 
	- if non exist set it to default or give the majority of the tree nodes targets

## how do we choose the feature 
entropy only works for finite number of classes, cannot be used for regression.

Using varience as our measure of impurity, we need low varience. it can be caliculated as :
![[Pasted image 20230201145954.png]]

Where D is the dataset that has reached the node, n is the number of instances in D, t is the mean of the target feature for the dataset D, and ti iterates across the target value of each instance in .


# Tree Pruning 
## Overfitting : 
Hypothesis is said to overfit the training data if there exists another hypothesis h', such that h is more accurate than h' on the training data but less accurate on the test data.

### Over fitting on Decision trees:
- Target or feature noice can easily cause overfitting.
- In the above case grow the tree rather than come to a conclusion -> causes overfitting helps in this case train but fails to test.

- If every tree is based on one or two leaves it would be a bad tree to generalize.

### Resolving the overfitting
- shaping the tree to be smaller. The question arises what point do we shape the tree to be smaller.
#### Tree Pruning: 
##### prepruning : 
stop growing tree at some point during top down construction when there is no longer sufficient data to make reliable decision.
	- __Parameter__ : Minimum number of examples to grow a node. 
	- Downside : __Pre-pruning approaches are computationally efficient and can work well for small datasets.__ By stopping the partitioning of the data early, however, induction algorithms that use pre-pruning can fail to create the most effective trees because they miss interactions between features that emerge within subtrees that are not obvious when the parent nodes are being considered. Pre-pruning can mean that these useful subtrees are never created.
##### Post pruning / Reduced Error Pruning :
1. Grow the full tree, 
2. validate the set. example with accuracy 
3. temperory prune and validate, take a decision again, if pruning on that node is required. 
4. then remove subtrees that do not have sufficient evidence 

##### Prepruning v/s postpruning and using both:


	


















# question
1. ~~In overfitting hypothesis does it mean if there exist a better model on target then does the model called overfit model. (__over fitting topic__)~~
2. ~~How do you marginalize the h from the h' in the pruning process. (if the pruning increases accuracy on test then ) are we testing the pruning on the testing set ? if yes, no questions asked.~~ 
3. 
