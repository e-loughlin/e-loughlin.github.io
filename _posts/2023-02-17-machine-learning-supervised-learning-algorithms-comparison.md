---
title: "Machine Learning - Supervised Learning Algorithms Comparison"
tags:
  - Engineering
  - Machine Learning
  - Algorithms
  - Python
  - Neural Networks
  - Bootstrap Aggregation
  - KNN
  - Support Vector Machines
  - Decision Trees
header:
  teaser: /assets/images/2023-02-17-machine-learning-supervised-learning-algorithms-comparison/img03.png
  og_image: /assets/images/2023-02-17-machine-learning-supervised-learning-algorithms-comparison/img03.png
gallery:
---

## Introduction

Supervised learning is a subset of machine learning that can also be broadly defined as function approximation. Functions are approximated using induction on labeled training data of input-output pairs of datasets.
Several different algorithms and methods of supervised learning exist, and hyperparameters of each algorithm can govern their specific behaviour and performance. The purpose of this project is to explore, study, analyze and gain a deeper understanding of supervised learning methods through experimentation and analysis. 

## Methods

In this project, five different learning algorithms were studied: Decision Trees, Neural Networks, Boosting (Bootstrap Aggregation), Support Vector Machines, and K-Nearest Neighbours. Two labeled classification datasets were selected for which each of the learners were trained and assessed on. Each dataset was split into a training set (70%) and a test set (30%). Learning curves were generated for each dataset-algorithm pair, whereby k-folds operations were performed (k=5) on the training set for cross-validation scoring. For each algorithm, two hyperparameters were selected for isolated tuning in order to study its effect on various aspects of the algorithm, as well as to better dissect the algorithm itself with respect to how the hyperparameter impacts its performance and behavior. The primary metrics used to compare each algorithm included training time, learning rates, and classification scoring. Additionally, confusion matrices of the overall performance were provided for some outputs. These metrics were used to analyze the different characteristics of the various algorithms which are discussed throughout the report.

For each of the algorithm-dataset pairs, hyperparameters were selected by running a grid-search algorithm. From there, manual tuning was conducted. The hyperparameter values are presented in the results section for each run. Implementation of each algorithm was conducted using Python and Scikit-Learn libraries. All runs were completed with a constant seed in order to control for randomness.

## Datasets

## Two Labeled Classification Datasets

Two labeled classification datasets were selected for testing and experimentation. These datasets differ in a multitude of ways, as discussed below. The intention behind selecting datasets that differ in several ways is driven by the goal of eliciting differences in behavior and performance across the selected algorithms in order to better highlight and understand algorithmic differences.

### Handwritten Digits Data Set

The first dataset selected is a handwritten digits dataset \cite{deng2012mnist}. Each image is 8x8 pixels, where each pixel is considered a feature. There are thus 64 features, and the value of each represents the intensity of the pixel as a real number between 0.0 and 1.0 (0 being black, and 1 being white). The classification target consists of the set [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]. The dataset is balanced, in that the number of samples for each class is approximately the same. The total number of samples in this dataset is 3823.

![Visualization of different digits samples](/assets/images/2023-02-17-machine-learning-supervised-learning-algorithms-comparison/MNISTHandwrittenDigitsDataset/Visualization_DifferentDigitsSamples.png)

*Figure 1: Visualization of different digits samples*

This dataset was considered interesting from a machine learning perspective for a number of reasons:

- Human readers are easily capable of visually classifying most of the samples themselves without being aware of exactly how their brain does so.
- Images tend to contain a large degree of noise.
- Correct classification often depends on higher-order factors such as shape/structure, not just feature values (individual pixel intensities).
- It has a relatively large number of features (64), 10 possible outputs, and a relatively small number of samples (3823).

Accuracy was selected as the performance metric for the training dataset because the dataset is balanced, and because it's an intuitive measure of success.

### Adult Income Prediction Dataset

This dataset \cite{Kohavi} consists of 16 features where each row represents a person. Features include discrete traits like ethnicity, country of origin, and education level, as well as continuous features such as income and age. The class being predicted is whether an individual has a salary of greater or less than \$50,000 USD each year. This dataset was selected to contrast the digits dataset, as it differs in several ways. For instance, the target class output is binary, the dataset is unbalanced (25% > 50k, 75% <= 50k), and the number of features is comparatively small (16), while the number of samples is comparatively large (approx. 30,000).

Pre-processing of this dataset involved removing rows that had null entries, and one-hot encoding of all discrete features. Additionally, all continuous features were normalized to a real number between 0 and 1.

F1 Score was selected as the performance metric for all training on this dataset since it is unbalanced. If accuracy were to be selected, a learner could produce a 75% accuracy score by always guessing <= 50k. The F1 Score is therefore a more appropriate performance metric as it combines recall and precision into a single metric. It should be noted, however, that in overall performance comparison, both F1 Score and Accuracy of the end results were used.

## Results

### Decision Trees


### Dataset 1: Digits

| Splitting Criterion   | Gini |
|------------------------|------|
| Max Depth              | 20   |
| Max Features           | None |
| Max Leaf Nodes         | None |
| Min Samples Per Leaf   | 1    |
| Min Samples Per Split  | 2    |

*Table 1: Hyperparameter Values - Decision Tree - Digits Dataset*

The parameters selected by this search were experientially (and through grid search) determined. However, these values allowed the decision tree to grow infinitely until it matches the training data exactly, thus overfitting. Despite the propensity toward higher bias, the maximum cross-validation scores were found values that allowed overfitting.

![Learning Curve - Decision Tree - Digits Dataset](/assets/images/2023-02-17-machine-learning-supervised-learning-algorithms-comparison/DecisionTree/LearningCurve_DecisionTree_MNISTHandwrittenDigitsDataset.png)

*Figure 1: Learning Curve - Decision Tree - Digits Dataset*

The learning curve demonstrates that more samples corresponded with greater cross-validation performance. However, the model was still biased toward the training set in all cases since the learner performed with perfect accuracy on the training set. This indicates that the model is overfitting the dataset.

![Timing Curve - Decision Tree - Digits Dataset](/assets/images/2023-02-17-machine-learning-supervised-learning-algorithms-comparison/MNISTHandwrittenDigitsDataset/DecisionTree/TimingCurve_DecisionTree_MNISTHandwrittenDigitsDataset.png)

*Figure 2: Timing Curve - Decision Tree - Digits Dataset*

The timing curves for both datasets appear that the fit time increases linearly, or \(O(n)\) or perhaps logarithmically. Decision Trees' average fit time complexity is \(O(n \log(n))\), so the results appear to match theory.

![Validation Curve - Max Depth - Decision Tree - Digits Dataset](/assets/images/2023-02-17-machine-learning-supervised-learning-algorithms-comparison/MNISTHandwrittenDigitsDataset/DecisionTree/ValidationCurve_MaxDepth_DecisionTree_MNISTHandwrittenDigitsDataset.png)

*Figure 3: Validation Curve - Max Depth - Decision Tree - Digits Dataset*

Figure 3 shows the effects of tuning the maximum depth of the decision tree. This graph demonstrates that increasing the maximum depth of the tree tends to cause overfitting to occur, since a tree can be created which fits the training data perfectly. This graph depicts an example of overfitting and the bias-variance trade-off, whereby the model continuously proves to be more accurate overall at the expense of increasing the overall bias toward the training data.

![Validation Curve - Min Impurity Decrease - Decision Tree - Digits Dataset](/assets/images/2023-02-17-machine-learning-supervised-learning-algorithms-comparison/MNISTHandwrittenDigitsDataset/DecisionTree/ValidationCurve_MinImpurityDecrease_DecisionTree_MNISTHandwrittenDigitsDataset.png)

*Figure 4: Validation Curve - Min Impurity Decrease - Decision Tree - Digits Dataset*

Figure 4 shows the effects of tuning the minimum impurity decrease. This hyperparameter controls how much information gain must occur in order to consider the splitting of a node. In this case, the Gini index is used. Minimizing this parameter (0.0) allows any amount of information gain to result in a node splitting, and therefore would allow the generation of a tree that perfectly matches the training data. The figure confirms this hypothesis, as the training accuracy of the model is 100% when this index is set to 0.0, and gradually decreases as the value increases. This corresponds to smaller trees being generated, which are also considered more generalized (less overfit) models since the variance decreases along with the bias. Overfitting implies that the model is overly complex and has learned the noise and random fluctuations in the training data rather than the underlying patterns. It is notable that in both cases of hyperparameter tuning, any reduction in the complexity of the Decision Tree (to generalize it and reduce overfitting) tended to also cause its cross-validation score to drop. This is because by reducing the size of the tree, or by pruning, it is likely removing some of the information that the tree has learned. While some of those pruned branches may have captured noise that led to overfitting, they may have also contained useful patterns as well which is why the lost complexity also performed worse on unseen data.

### Dataset 2: Adult Income Prediction

| Splitting Criterion   | Gini |
|------------------------|------|
| Max Depth              | 15   |
| Max Features           | None |
| Max Leaf Nodes         | 40   |
| Min Samples Per Leaf   | 1    |
| Min Samples Per Split  | 2    |

*Table 2: Hyperparameter Values - Decision Tree - Adult Dataset*

![Learning Curve - Decision Tree - Adult Dataset](/assets/images/2023-02-17-machine-learning-supervised-learning-algorithms-comparison/UCIAdultDataSet/DecisionTree/LearningCurve_DecisionTree_UCIAdultDataSet.png)

*Figure 5: Learning Curve - Decision Tree - Adult Dataset*

Figure 5 shows an interesting trend in that increasing the number of training samples reduces the variance between the training score and the cross-validation score. In this example, as the bias toward the training data decreases, the variance decreases since the cross-validation score improves. The fact that the training data was never capable of reaching an F1 score of 1.0 suggests that a Decision Tree could not be generated which perfectly matched all training data, which might indicate noise in the dataset or perhaps weak correlations. This would intuitively seem correct as the features alone (age, ethnicity, country of origin, etc) are unlikely to be perfect predictors of income, and thus no set of concrete rules can be learned to predict with perfect accuracy. Generalization in Decision Trees is typically achieved by limiting the size of the tree in some way, which can be seen in the hyperparameters having been set (Max Depth of 15, Max Leaf Nodes of 40) which prevents it from biasing too heavily on training data.

![Timing Curve - Decision Tree - Adult Dataset](/assets/images/2023-02-17-machine-learning-supervised-learning-algorithms-comparison/UCIAdultDataSet/DecisionTree/TimingCurve_DecisionTree_UCIAdultDataSet.png)

*Figure 6: Timing Curve - Decision Tree - Adult Dataset*

![Validation Curve - Max Depth - Decision Tree - Adult Dataset](/assets/images/2023-02-17-machine-learning-supervised-learning-algorithms-comparison/UCIAdultDataSet/DecisionTree/ValidationCurve_MaxDepth_DecisionTree_UCIAdultDataSet.png)

*Figure 7: Validation Curve - Max Depth - Decision Tree - Adult Dataset*

Varying the maximum depth of the tree showed interesting behavior. Whereas the cross-validation score benefited with ever-increasing max-depth in the Digits dataset, this dataset appeared to perform better overall with a maximum depth having been limited at 10. If a decision tree model with a smaller maximum depth performs better on a dataset compared to one with unlimited depth, it might mean that the dataset contains noisy data or has a high degree of variance.

![Validation Curve - Min Impurity Decrease - Decision Tree - Adult Dataset](/assets/images/2023-02-17-machine-learning-supervised-learning-algorithms-comparison/UCIAdultDataSet/DecisionTree/ValidationCurve_MinImpurityDecrease_DecisionTree_UCIAdultDataSet.png)

*Figure 8: Validation Curve - Min Impurity Decrease - Decision Tree - Adult Dataset*

Adjusting the minimum impurity decrease as per Figure 8 showed a decrease in bias, since the performance metric on training data and on cross-validation data matched when it was set to 0.003. However, the performance overall suffered so it was considered more optimal to keep the value at 0, thus accepting some overfitting.

![Confusion Matrix - Decision Tree - Adult Dataset](/assets/images/2023-02-17-machine-learning-supervised-learning-algorithms-comparison/UCIAdultDataSet/DecisionTree/ConfusionMatrixNormalized_DecisionTree_UCIAdultDataSet.png)

*Figure 9: Confusion Matrix - Decision Tree - Adult Dataset*

The normalized confusion matrix was included to demonstrate that while the model tended to successfully predict the more common class (<= 50k) most of the time (95%), it could only correctly predict the other class (>50k) 58% of the time. This could indicate that a considerable amount of noise exists in features for this class which the single Decision Trees could not adequately capture. Noise in a dataset could prevent splitting on specific values for features from producing information gain (Gini or reduction in entropy), which could explain its difficulty in successfully predicting this class.
<!-- Include: DecisionTree -->

### Boosting

<!-- Include: Boosting -->

### K-Nearest Neighbours

<!-- Include: KNN -->

### Support Vector Machines

<!-- Include: SVM -->

### Neural Networks

<!-- Include: ANN -->

## Overall Comparison

<!-- Include: Comparison -->

**References**

<!-- Bibliography to be included -->

