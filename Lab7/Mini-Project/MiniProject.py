
import numpy as np
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeRegressor, plot_tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, r2_score

# Sample student dataset
# Features: Study Hours and Attendance (%)
X = np.array([
    [1, 50], [2, 55], [2, 60], [3, 65],
    [3, 70], [4, 70], [4, 75], [5, 80],
    [5, 85], [6, 80], [6, 90], [7, 85],
    [7, 90], [8, 95], [8, 90], [9, 95],
    [9, 98], [10, 98], [4, 60], [6, 75]
])

# Target: Student marks
y = np.array([
    35, 40, 45, 48, 55, 58, 62, 65, 70, 72,
    76, 78, 82, 85, 88, 90, 93, 96, 50, 68
])

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train Decision Tree model
model = DecisionTreeRegressor(max_depth=3, random_state=42)
model.fit(X_train, y_train)

# Evaluate model
predictions = model.predict(X_test)

print("STUDENT PERFORMANCE PREDICTION SYSTEM")
print("-------------------------------------")
print("Mean Absolute Error:", round(mean_absolute_error(y_test, predictions), 2))
print("R2 Score:", round(r2_score(y_test, predictions), 2))

# Take user input
print("\nEnter student details:")
study_hours = float(input("Study hours per day: "))
attendance = float(input("Attendance percentage: "))

student_data = np.array([[study_hours, attendance]])
predicted_marks = model.predict(student_data)[0]

print("\nPredicted Marks:", round(predicted_marks, 2))

if predicted_marks >= 75:
    print("Performance: Excellent")
elif predicted_marks >= 50:
    print("Performance: Average")
else:
    print("Performance: Needs Improvement")

# Visualize decision tree
plt.figure(figsize=(14, 8))
plot_tree(
    model,
    feature_names=["Study Hours", "Attendance"],
    filled=True,
    rounded=True
)
plt.title("Student Performance Prediction - Decision Tree")
plt.savefig("Lab7/Mini-Project/DecisionTree.png")
plt.show()

print("\nDecision tree graph saved successfully!")
