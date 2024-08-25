import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Load the data
music_data = pd.read_csv('IPL_Matches_2008-2020.csv')

# Drop columns that are not needed
x = music_data.drop(columns=['winner', 'id', 'city', 'date', 'player_of_match', 'venue', 'neutral_venue', 'result', 'result_margin', 'eliminator', 'method', 'umpire1', 'umpire2'])

# Handle missing values in x
x = x.dropna()

# Align y with x by using the index of x
y = music_data['winner'].loc[x.index]

# Drop any remaining NaN values in y
y = y.dropna()

# Ensure x and y have consistent indices
x = x.loc[y.index]

# Encode categorical variables
x = pd.get_dummies(x)

# Split the data into training and testing sets
X_train, X_test, Y_train, Y_test = train_test_split(x, y, test_size=0.5)

# Train the model
model = DecisionTreeClassifier()
model.fit(X_train, Y_train)

# Create a sample prediction input and encode it
sample_data = pd.DataFrame([{
    'team1': 'Kolkata Knight Riders',
    'team2': 'Chennai Super Kings'
}])
sample_data = pd.get_dummies(sample_data)

# Ensure sample_data has the same columns as X_train
sample_data = sample_data.reindex(columns=X_train.columns, fill_value=0)

# Make a prediction
prediction = model.predict(sample_data)
print(prediction)

# Optional: Evaluate the model on the test set
predictions_test = model.predict(X_test)
score = accuracy_score(Y_test, predictions_test)
print(f"Accuracy: {score}")
