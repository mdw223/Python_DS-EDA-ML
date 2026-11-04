# Machine learning concepts and types of models

need:
data preperation...

algorithms...
supervised learning- the bales on training examples are known, looks for patternsi nthe training set to make predictions about unlabeled testing data, classification algo used to det. the correct category for a data item

unsupervised learning - no labeled data or training data set, looks for patterns in the data by discovery, clustering and data association algos

deep learning - structured process involving neural networks that leverages layers of machine learning in which the ouput of one layer becomes the input for the next

Automation and iterative processes...

scalability...
modeling...

------


feature - one col or independent varibale in your input set for feature engineering - coverting data into values to build your feature matrix

label - the target dependent variable, groud truth that your output is compared agianst

-----

Steps of ML:
1. chooce a class of model and import 
2. choose model params and instantiate
3. arrange data into a feature matric and target vector
4. fit model to data by calling the fit methods of the model instance
5. apply the model to new data (predict labels for supervised learning thru regression or classification    OR transform for unsupervised learning)
6. evaluate the model and adjust hyperparams

------


Supervised learning classifiers:

Classificaiton - given a set of data points and their labels, learn how they are classified so a new point can be put in the right class

Can use linear regression, logistic, kNN, naive bays, k means clustering....

They differ in: performance, memory, size, linearity, initial params

------

we use scikit-learn for ML
Data must be reshaped like arr.reshape(-1,1)

lr3 = linear_model.LinearRegresison()
lr3.fit(X=tips_dummy_ref, y=tips['tip'])