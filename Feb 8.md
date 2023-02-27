- if you set sensitivity : i.e. call all tru you have 100% sensitivity but your specificity is hit. 
- 100% specificity is setting calling all false, this hits the sensitivity. 


## F-measure : 
sometimes the harmonic mean of precision and recall, called F-measire is reported which in a ingle measire summarizes both:
	f-measure : 2 * precision * recall / (precision + recall)
_note : Both precision and recall should be good in order to get good F-measure._

Robustness to class distribution:
- specificity and sensitivity are robust to imbalance data unlike precision. 
- model correctly predicts all +ve and 90% of all -ve's
- out of 10 +ve and 90 -ve : 
	- 10 predicted right : 10/10 (1)  and 81/90 -ve right (0.9)
	- sensitivity 10/10 = 1 , specificity 81/90 = 0.9
	- precision = 10/10+9 = 0.53

- out of 90 =ve and 10 -ve 
	- 90 +ve correct prediction 9/10 -ve predicted 
	- sensitivy (1) , specificty (0.9)
	- precision see? 

In medical reports even though the patient needs to know precisoin they specify specificity and sensitivity, because these are not dependent on the dataset when changes changes the precision. 


## ROC curve:
Using different thresholds on the confidence, different sensitivity and specificity measures can be obtained which re then plotted on a graph called ROC curve

- traditionally plotted between sensitivity (true +ve  rate ) and 1-specificty (false +ve rate)
### Comparing ROC Curves 
- comparing specificty and sensitivity of two models but an ROC curve of the 2 models can be compared. 
- to quantitatively compare models we can find the __Area under the ROC curve__


## Evaluation of multinomial targets
These measures extend to cases when the target can take more than two values(multiple classes)
confusion matrix shows in detail what types of mistakes the model generally 


## Domain INdependent :
R squared coeff . 