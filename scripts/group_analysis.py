import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("data/fake_customer_data.csv", encoding='utf-8-sig')

# Set seaborn style
sns.set(style="whitegrid")

# 1. Average satisfaction per Service Type
service_avg = df.groupby("ServiceType")["SatisfactionRating"].mean().sort_values()

plt.figure(figsize=(8, 5))
sns.barplot(x=service_avg.values, y=service_avg.index, palette="coolwarm")
plt.title("Average Satisfaction by Service Type")
plt.xlabel("Average Satisfaction Rating")
plt.ylabel("Service Type")
plt.tight_layout()
plt.savefig("data/avg_satisfaction_by_service.png")
plt.show()

# 2. Satisfaction by Region
region_avg = df.groupby("Region")["SatisfactionRating"].mean().sort_values()

plt.figure(figsize=(8, 5))
sns.barplot(x=region_avg.values, y=region_avg.index, palette="magma")
plt.title("Average Satisfaction by Region")
plt.xlabel("Average Satisfaction Rating")
plt.ylabel("Region")
plt.tight_layout()
plt.savefig("data/avg_satisfaction_by_region.png")
plt.show()

# 3. Correlation matrix for numeric features
correlation = df[["Age", "SubscriptionLengthMonths", "SatisfactionRating"]].corr()

plt.figure(figsize=(6, 5))
sns.heatmap(correlation, annot=True, cmap="Blues", fmt=".2f")
plt.title("Correlation Matrix")
plt.tight_layout()
plt.savefig("data/correlation_matrix.png")
plt.show()
