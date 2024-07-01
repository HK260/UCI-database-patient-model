# UCI-database-patient-model

## Project Description

This project involves performing an initial analysis on a dataset to explore and evaluate different classification models for predicting patient readmission. The analysis primarily focuses on two machine learning models: Logistic Regression and Random Forest, with various sampling techniques to address class imbalance in the dataset. The goal is to identify the model that best balances precision, recall, and overall accuracy for both readmitted and non-readmitted classes.

## Models Evaluated

### Logistic Regression

Evaluated with different sampling techniques to handle class imbalance.
Metrics: Precision, Recall, Overall Accuracy.

### Random Forest

Evaluated with random under-sampling to handle class imbalance.
Metrics: Precision, Recall, Overall Accuracy.

## Insights

Logistic Regression with Random Under-sampling: This combination shows a balanced trade-off between recall and accuracy. It is suitable when both classes' recall is critical, and some reduction in overall accuracy is acceptable.

Random Forest with Random Under-sampling: This combination should be used when the priority is to identify readmitted patients (higher recall), and overall accuracy is less critical.

## Next Steps

Further Tuning: Further hyperparameter tuning and combining sampling methods (e.g., SMOTE + undersampling) can be explored to enhance performance.

Collect More Data: Collecting more data for readmitted patients could help in better training and evaluation of the models.

Feature Engineering: Create new features or select important features to improve model performance.
