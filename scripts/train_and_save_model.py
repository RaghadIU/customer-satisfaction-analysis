import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import joblib 


df = pd.read_csv("data/fake_customer_data.csv", encoding='utf-8-sig')


le_gender = LabelEncoder()
le_region = LabelEncoder()
le_service = LabelEncoder()

df["Gender"] = le_gender.fit_transform(df["Gender"])
df["Region"] = le_region.fit_transform(df["Region"])
df["ServiceType"] = le_service.fit_transform(df["ServiceType"])


X = df[["Age", "SubscriptionLengthMonths", "Gender", "Region", "ServiceType"]]
y = df["SatisfactionRating"]


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)


joblib.dump(model, "data/model.pkl")
joblib.dump(le_gender, "data/le_gender.pkl")
joblib.dump(le_region, "data/le_region.pkl")
joblib.dump(le_service, "data/le_service.pkl")

print("Model and encoders saved successfully!")
