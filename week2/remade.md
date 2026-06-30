# Data Classification Using AI using K-Nearest Neighbors (KNN)

## Project Overview

This industrial training project, developed as part of the DecodeLabs AI program, introduces the core concepts of **Supervised Machine Learning** through a practical classification task. The objective is to design, train, and evaluate a machine learning model capable of identifying patterns in data and accurately classifying unseen samples.

The project focuses on understanding the complete machine learning workflow, from data preparation to model evaluation, using the **K-Nearest Neighbors (KNN)** algorithm.

---

# Project Objective

The main objective of this project is to build an intelligent classification model that learns from historical data and predicts the category of new observations.

The project also aims to provide practical experience in:

* Data preprocessing
* Feature scaling
* Model training
* Performance evaluation
* Hyperparameter tuning
* Classification validation

---

# Input Stage

The project uses the **Iris Dataset**, one of the most popular benchmark datasets in machine learning.

### Dataset Details

* Total Samples: **150**
* Number of Classes: **3**
* Features: **4**

  * Sepal Length
  * Sepal Width
  * Petal Length
  * Petal Width

Each flower sample belongs to one of three Iris species, making it an ideal dataset for supervised classification.

### Data Preparation

Before training the model, several preprocessing steps are performed:

* The dataset is randomly shuffled to eliminate any ordering bias.
* The data is divided into **Training** and **Testing** datasets.
* Feature scaling is applied using **StandardScaler**, which standardizes every feature with:

  * Mean = 0
  * Standard Deviation = 1

This normalization ensures that all features contribute equally to the distance calculations used by the KNN algorithm.

---

# Processing Stage

The classification model is implemented using the **K-Nearest Neighbors (KNN)** algorithm available in the Scikit-learn library.

### Working Principle

KNN is a distance-based supervised learning algorithm that classifies new data points by identifying the closest neighboring samples in the training dataset.

The algorithm assumes that similar data points are located close to each other within the feature space.

### Model Development Steps

The machine learning workflow consists of three major stages:

### 1. Model Initialization

The KNN classifier is created by specifying the desired value of **K**, representing the number of neighboring samples considered during prediction.

### 2. Model Training

The classifier is trained using the training dataset. Unlike many machine learning algorithms, KNN stores the training data instead of creating a mathematical model.

### 3. Prediction

The trained classifier predicts the category of unseen test samples by analyzing the nearest neighbors based on Euclidean distance.

---

# Hyperparameter Tuning

Choosing the correct value of **K** is essential for achieving high prediction accuracy.

* A very small K value may lead to **Overfitting**, where the model becomes sensitive to noise.
* A very large K value may result in **Underfitting**, where important decision boundaries are ignored.

To determine the optimal K value, multiple values are tested and compared. The best value is selected using the **Elbow Method**, where the prediction error becomes minimal before stabilizing.

---

# Output and Model Evaluation

Model performance is evaluated using multiple classification metrics instead of relying only on accuracy.

### Accuracy

Accuracy measures the percentage of correctly classified samples. Although useful, it may produce misleading results when datasets are imbalanced.

### Confusion Matrix

A Confusion Matrix provides a detailed evaluation of prediction performance by comparing actual and predicted labels.

It consists of:

* **True Positive (TP)** – Correct positive predictions
* **True Negative (TN)** – Correct negative predictions
* **False Positive (FP)** – Incorrect positive predictions (Type I Error)
* **False Negative (FN)** – Incorrect negative predictions (Type II Error)

This evaluation helps identify both correct classifications and prediction errors.

### Precision

Precision measures how many predicted positive samples are actually correct.

### Recall

Recall indicates how effectively the model identifies all actual positive samples.

### F1 Score

The F1 Score combines Precision and Recall into a single performance metric using their harmonic mean.

It provides a balanced evaluation of the classifier, especially when both false positives and false negatives are important.

---

# Technologies Used

* Python
* Scikit-learn
* NumPy
* Pandas
* Matplotlib
* Seaborn

---

# Expected Outcome

After completing this project, the developed KNN classifier should:

* Accurately classify Iris flower species.
* Demonstrate the importance of preprocessing and feature scaling.
* Show the effect of different K values on model performance.
* Evaluate classification quality using multiple performance metrics.

---

# Conclusion

This project provides a practical introduction to supervised machine learning by implementing a complete classification pipeline using the K-Nearest Neighbors algorithm. Through preprocessing, model training, hyperparameter tuning, and evaluation, students gain valuable hands-on experience in solving real-world classification problems.

The project also emphasizes that reliable machine learning models should be assessed using comprehensive evaluation metrics such as the Confusion Matrix, Precision, Recall, and F1 Score rather than depending solely on accuracy. Successfully completing this project demonstrates an understanding of the end-to-end machine learning workflow and helps build a strong portfolio for future AI and data science applications.
