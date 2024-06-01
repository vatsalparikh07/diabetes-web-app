# Predictive Modeling for Personalized Diabetes Care

![1 - Copy](https://github.com/vatsalparikh07/diabetes-web-app/assets/65659649/b85b5703-ddb1-4eaf-ae5f-523e39f4a625)

## Overview
Diabetes mellitus, marked by elevated blood sugar levels, is a persistent condition with the potential for various complications. Projected data for 2040 suggests a significant rise in global diabetic cases, with an estimated 642 million individuals affected, underscoring the urgency of addressing this health issue. In response to the escalating morbidity, modern technology, particularly machine learning, has found applications in the healthcare domain. This study employs Support Vector Machine (SVM), Random Forest (RF), Logistic Regression (LR), XGBoost Classifier, and Artificial Neural Network (ANN) algorithms for diabetes prediction. The dataset utilized originates from the Behavioral Risk Factor Surveillance System (BRFSS), encompassing information about individuals’ health statistics, lifestyle, and diabetes diagnoses across 21 attributes. The research encompasses various data mining techniques such as data cleaning, pre-processing, decision-making, machine learning, classification, and correlation analysis, employing advanced algorithms. Classification facilitates grouping individuals based on their diabetes risk, offering a structured approach to personalized healthcare. Correlation analysis delves into the relationships between health indicators, shedding light on underlying risk factors. The ultimate goal is to develop predictive models and a web-based application for early diabetes detection based on user inputs. The findings reveal that the Artificial Neural Network (ANN) achieved the highest accuracy (ACC = 0.7547) among the predictive models.

## Methods

### Data Collection
Our project involves the acquisition of data from the Behavioral Risk Factor Surveillance System (BRFSS), a comprehensive health survey conducted by the Centers for Disease Control and Prevention (CDC). This data contains 21 features on 70,692 subjects.

### Exploratory Data Analysis and Visualization
The dataset offered a diverse array of health-related indicators such as age, high BP, high Chol, smoker, mental health, etc. Data cleaning was performed, where duplicate rows were deleted, and missing values were addressed. EDA was performed on the data and the variables were studied using various visualizations.

### Predictive Modelling
The data was split into a 20-80 test-train ratio and machine learning classifiers namely SVM, LR, RF, XG Boost, Voting Classifier, and ANN were used to build the model. Evaluation metrics such as accuracy, sensitivity, specificity, ROC curves, AUC value, and confusion matrix were utilized.

### Web-based Application Development
The development of our web-based application utilized Streamlit, a powerful framework known for its simplicity and efficiency in building interactive data applications. The application uses custom inputs from the user based on the features included in the dataset and predicts the possibility of having diabetes based on the machine learning model used.

## Results

### Correlation Analysis
![image](https://github.com/vatsalparikh07/diabetes-web-app/assets/65659649/529fde2f-4e0b-4bf1-932d-4549482ff233)

### General Health Count Plot
![image](https://github.com/vatsalparikh07/diabetes-web-app/assets/65659649/67870920-7a90-45b0-aac3-1ae6742a89ac)

### BMI Categorized Plot
![image](https://github.com/vatsalparikh07/diabetes-web-app/assets/65659649/e98c5e3b-fd0c-40a2-96ca-4811867ea5e8)

### Age Distribution by Diabetes Class
![image](https://github.com/vatsalparikh07/diabetes-web-app/assets/65659649/38473b08-afc0-4db8-8703-89b68727309f)

### Model Comparison
![image](https://github.com/vatsalparikh07/diabetes-web-app/assets/65659649/afb60b46-f636-4a5d-9312-d8af2ce09f71)

### Training vs Validation Accuracy Curve (ANN)
![image](https://github.com/vatsalparikh07/diabetes-web-app/assets/65659649/678dea27-1e50-46bc-a4fa-d0de8a04aabc)

### Training vs Validation Loss Curve (ANN)
![image](https://github.com/vatsalparikh07/diabetes-web-app/assets/65659649/36706aef-669b-4814-8cd2-abd48593dca2)

### Web Application Interface
![image](https://github.com/vatsalparikh07/diabetes-web-app/assets/65659649/d4fd9fee-084c-4584-a627-602ae0af7e41)

![image](https://github.com/vatsalparikh07/diabetes-web-app/assets/65659649/25af395f-7e51-42f7-adc9-c802e5217d45)
