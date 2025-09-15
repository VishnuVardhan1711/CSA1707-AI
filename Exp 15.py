# Import necessary libraries
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn.metrics import accuracy_score

# Load the Iris dataset
iris = load_iris()
X = iris.data
y = iris.target

# Split the dataset into training and testing sets (70% training, 30% testing)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Initialize the Decision Tree Classifier
clf = DecisionTreeClassifier(criterion='gini', max_depth=3, random_state=42)

# Train the model
clf.fit(X_train, y_train)

# Make predictions on the test set
y_pred = clf.predict(X_test)

# Display the structure of the decision tree
tree_rules = export_text(clf, feature_names=iris.feature_names)
print("Decision Tree Structure:\n")
print(tree_rules)

# Calculate and print the accuracy
accuracy = accuracy_score(y_test, y_pred)
print("\nAccuracy of the Decision Tree Classifier:", accuracy)
