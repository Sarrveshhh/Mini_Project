from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
import pandas as pd
import  joblib
# Load the data from a CSV file into a DataFrame
df = pd.read_csv('dataset.csv')
X = df.iloc[:, :7]
X.columns = ['n','p','k','temperture','humidity','ph','rainfall']
y = df.iloc[:, -1]
# Extract the label data into a separate variable
 # assuming the label is in the 7th column

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Train a decision tree classifier on the training data
clf = DecisionTreeClassifier()
clf.fit(X_train.values, y_train.values)

# Evaluate the classifier on the testing data
accuracy = clf.score(X_test.values, y_test.values)
print("Accuracy:", accuracy)

joblib.dump(clf, 'clf_model')


# Accept user input
# input_data = []
# for feature in X.columns.values:
#     input_data.append(float(input("Enter the value for {}:".format(feature))))

# # Use the classifier to make a prediction on the user input
# prediction = clf.predict([input_data])

# # Output the result
# print("Based on the input data, the best crop to cultivate is:", prediction[0])