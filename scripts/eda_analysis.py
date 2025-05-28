import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("data/fake_customer_data.csv", encoding='utf-8-sig')

# Set visual style
sns.set(style="whitegrid")

# 1. Preview the data
print("First 5 rows:")
print(df.head())

# 2. Basic info
print("\n Dataset info:")
print(df.info())

# 3. Descriptive statistics
print("\n Descriptive statistics:")
print(df.describe())

# 4. Value counts for categorical columns
print("\n Gender distribution:")
print(df["Gender"].value_counts())

print("\n Region distribution:")
print(df["Region"].value_counts())

print("\n Service Type distribution:")
print(df["ServiceType"].value_counts())

# 5. Distribution of satisfaction ratings
plt.figure(figsize=(8, 5))
sns.countplot(x='SatisfactionRating', data=df, palette="viridis")
plt.title("Distribution of Satisfaction Ratings")
plt.xlabel("Rating (1 = Very Poor, 5 = Excellent)")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("data/satisfaction_rating_distribution.png")
plt.show()

# 6. Age distribution
plt.figure(figsize=(8, 5))
sns.histplot(df["Age"], bins=10, kde=True, color='skyblue')
plt.title("Customer Age Distribution")
plt.xlabel("Age")
plt.ylabel("Number of Customers")
plt.tight_layout()
plt.savefig("data/age_distribution.png")
plt.show()
