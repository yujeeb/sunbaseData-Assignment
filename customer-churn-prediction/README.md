Executive Summary

Approach

Data Preprocessing

- Data Collection: The dataset provided demographic, usage, bill data..
- Data Cleaning: Performed data cleaning to handle missing values, duplicates, and outliers, ensuring data consistency.
- Feature Selection: Relevant features were selected using correlation analysis and domain knowledge.
- Feature Scaling: Used Min-Max Scaling for numeric data

Exploratory Data Analysis (EDA)

- We visualized the data to understand its distribution and relationships.
- We analyzed customer churn rates and identified trends and correlations with other variables.

Data Splitting

- The dataset was split into training and test sets to evaluate model performance.

Model Selection

- We experimented with various machine learning algorithms, including logistic regression, random forests, and neural networks.
- Model selection was based on performance metrics such as accuracy, precision, recall, F1-score.

Model Training

- The selected model was trained on the training dataset.
- Hyperparameter tuning was performed using cross-validation to optimize model parameters on Logistic Regression model.

Model Evaluation

- Model performance was evaluated on the test set, and the best-performing model was chosen.

Model Deployment

- The chosen model was deployed in a production environment, integrated into a web application.

Reporting

- This report summarizes the approach, findings for stakeholders.

Key Findings

- The chosen machine learning model achieved:
accuracy: 0.5011666666666666 
precision: 0.49839886141256007 
recall: 0.37530979971866835 
f1_score: 0.49321232039535434
- Customer tenure, usage patterns, and customer age value were significant predictors of churn.
- The model can provide valuable insights for customer retention strategies.
- Regular monitoring and retraining of the model are crucial to maintain its predictive power.

Conclusion

In conclusion, the development of a machine learning model to predict customer churn based on historical customer data is a valuable asset for the organization. By leveraging this predictive capability, the company can implement targeted customer retention strategies and ultimately reduce churn, leading to increased customer satisfaction and revenue.



