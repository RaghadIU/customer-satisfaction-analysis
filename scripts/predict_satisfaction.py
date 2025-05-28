import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.preprocessing import LabelEncoder

# Load dataset
df = pd.read_csv("data/fake_customer_data.csv", encoding='utf-8-sig')

# Label Encoding for categorical features
le = LabelEncoder()
df["Gender"] = le.fit_transform(df["Gender"])
df["Region"] = le.fit_transform(df["Region"])
df["ServiceType"] = le.fit_transform(df["ServiceType"])

# Features and target
X = df[["Age", "SubscriptionLengthMonths", "Gender", "Region", "ServiceType"]]
y = df["SatisfactionRating"]

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Evaluate
print("Classification Report:")
print(classification_report(y_test, y_pred))

print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))
