chapter 4.1, - 4.4 : Decision trees 

# Classification problem 
- Fetures : size color shape 
- target/class : +ve / -ve 
- training data : dateset

## Decision trees :
Tree based classifiers:
	nodes test features 
	leaves specify class 
	branches/edges
there exists many decision trees 

Advantages: 
- They can theoritically represent any classificaiton function over discrete features.
- rules can be re-written 
- _how not to over fit in decision trees_

### Decisoin tree Induction
Algorithms to automatically build decision trees. --> Decision tree Induction

- Recursively build a top down by divide and conquer of the _feature_.
- which feature to pick ? (is it necessary to introduce a Inductive Bias)
	- or else based on the split of the outcome _( a perfect split of outcome would be the best case and the depth is reduced of the tree)_
	- how do you know what a good split is ? 
		- entropy and __information gain__ is critical to make this decision. 
		- information gain -> ID3 (iterative Dichotomizer 3)
			- #### Entropy 
				measure of change. 
				==___entropy(s) = -p1 log2 (p1) - p0 log2 (p0)___==
				_where p1 is the fraction og positive examples in S and p0 is the fraction of negitive examples_
				if all examples are in one category, then enttropy is zero.(defined as 0.log(0) )
				__genralized:  in the summation from i -> c where (- pi log2 (pi))__
		The information gain fi feature F is expected _reduction in entropy_ resulting in splitting of feature. 
		Gain(S,F) = Entropy (S) - (Summation of v where v belongs to Values(F))  |Sv| over |S| (_complete this alg_)

	Preference Bias of interative Dichotomizer 3 
	OCCAM'S RAZER  applied to Decision tree / ID3
	More the features lesser the entropy, as this would lead to more partitions and end on a leaf node.(Disadvantage)
	
	__Information Gain ratio (Algorithm) to over come this issue. Divide info gain of a feature by the entropy of the dataset with respect to the feature.__

	__Gini Index : Alternate to entropy -> measure of impurity.__
	(Probability and stats)		
	

   

	
		 
		
