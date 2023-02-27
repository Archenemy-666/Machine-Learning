# About:
- Does not involve construction if an explicit function relating to features to target.
- classifies based on direct comparision to known training instances.
- just memorize training instances
- computationally very expensive, requiring comparision to all past training instances.

### Nearest neighbour method (simplest ML method):
- calculate dist between test point and every training instance.
- the nearest training instance falls under the same category.
__note: Euclidean distance is used in the above case__ , 
	Another alternative is using absolute value __which is Manhatten Distance__

### Implicit classification function:
- Although explicitly calculated, the learned classification function is based on regions of the feature space divided by the training examples.
- The __voronoi diagram__ gives the complex polyhedra segmenting the sample space into the regions closest to each other.
__Implcit Decision Boundries are created.__

### K - Nearest neighbors:
There are exceptions when considering distance between just one closest element, hence we see more than one (k) nearest neighbours. 
__This is called k-nearest neighbour__, because here we are considering (k) no.of elements under classification.

It is important to have the right value for (k), if its less its a case of overfitting, if its high it would cause underfitting. 

Weighted k - nearest neighbours:
Here we add weight if the value if closer.

- In case of regression task, when we are implementing k-nearest neighbour we value of the node will be the avg of the k nearest neighbors. 

There is an issue when the distance is calculated between nodes that with more than one feature, where the units of each feature can have an affect, i.e one of the feature with higher numerical value will dominate, which has nothing to do with the property of the nodes. 

__This requires a Normalization to address this issue__

This issue does not exist with decision tree, where we look at each feature independently. Where as here we are considering all the features together at once. 


#### How to Normalize : 
predictive model should not be affected because the absolute values of some features are larger than others. KNN is specially sensitive to this. 

Make sure that the fetures fall under the same frequency/range. This is a normalization step. 


#### Cosine Similarity:
There are sometimes we consider not euclidean distance but the Cosine similarity, where we take the cosine of the angle in the plotted graph of nodes among the features.

- useful for text data
- useful for high dimensional data

Try K-nearest neighbor on your dataset in assignment. 



