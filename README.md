# Binary-Classification-Machine-Learning-Model
A Binary Classification Machine Learning Model developed to use provided information about an individual to predict with 87.33% accuracy whether he will accept a vehicle insurance offer.

![image](https://github.com/ottoman9/Binary-Classification-Machine-Learning-Model/assets/84887898/3fde31e2-f440-4ebe-93e5-990a6788c9dd)

## **🛠️ Steps and Techniques:**
>🧹 **Data Preparation:**

  🔧 Scaling: Applied StandardScaler and MinMaxScaler to standardize and normalize numerical features, ensuring they contribute proportionally during model training.
  
  🔠 Encoding: Used One-Hot Encoding for categorical features to transform them into a binary matrix, preserving all possible categories and avoiding ordinal misrepresentation.
  
>🤔 **Model Selection:**

![image](https://github.com/ottoman9/Binary-Classification-Machine-Learning-Model/assets/84887898/4126313a-0e34-482b-ad01-ddd3d367e699)


📊 Initial Trials: Considered various models including Logistic Regression, Random Forest, XGBoost, and LightGBM.

🏆 Final Choice: Selected CatBoost for its inherent handling of categorical features, efficient training, and high accuracy.

>🎛️ **Hyperparameter Tuning:**

Performed GridSearchCV with a range of hyperparameters to find the best combination for maximizing AUC.
Adjusted parameters like depth, learning rate, and iterations for optimal performance.

>🏋️** Model Training and Evaluation:**

Trained the model using cross-validation to validate its performance and avoid overfitting.
Achieved a mean validation AUC of 0.8670, with further tuning aimed at improving this score.

### 📈 **Results:**

Finalized the model with the best hyperparameters obtained from GridSearchCV.
Evaluated the model on the test data, recording the predicted probabilities.

## **🔍 Performance Analysis:**

Highlighted the model's strengths in handling mixed data types and achieving high accuracy.
Compared CatBoost's performance to other models, emphasizing its advantages in this project.
💡 Key Insights:
📏 Data Scaling: Essential for ensuring numerical features are on the same scale, aiding in faster convergence and better model performance.
🔢 One-Hot Encoding: Chosen for its ability to handle non-ordinal categorical features without introducing bias.
🚀 CatBoost: Selected for its efficiency, ease of use, and superior handling of categorical data, leading to high performance in our binary classification task.

## 🎉 Conclusion:
This project successfully developed a robust binary classification model using CatBoost, demonstrating the importance of appropriate data preprocessing, model selection, and hyperparameter tuning. The final model can be further optimized to reach the desired AUC score of 0.90.
