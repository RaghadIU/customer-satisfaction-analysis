import pandas as pd
import random
from faker import Faker
import os

# Initialize faker
fake = Faker()

# Define possible values
genders = ['Male', 'Female']
regions = ['Riyadh', 'Jeddah', 'Dammam', 'Abha', 'Mecca']
services = ['Internet', 'Calls', 'Full Packages', 'Customer Support']
sample_comments = [
    "Excellent service", "Internet is sometimes slow", "Customer support is great",
    "Prices are too high", "Needs better coverage", "", "", ""
]

# Create list to hold data
data = []

# Generate 100 fake entries
for i in range(100):
    row = {
        "CustomerID": i + 1,
        "Age": random.randint(18, 65),
        "Gender": random.choice(genders),
        "Region": random.choice(regions),
        "ServiceType": random.choice(services),
        "SubscriptionLengthMonths": random.randint(1, 60),
        "SatisfactionRating": random.randint(1, 5),
        "Comments": random.choice(sample_comments)
    }
    data.append(row)

# Convert to DataFrame
df = pd.DataFrame(data)

# Create data folder if it doesn't exist
os.makedirs("data", exist_ok=True)

# Save to CSV
df.to_csv("data/fake_customer_data.csv", index=False, encoding='utf-8-sig')

print(" customer data generated and saved to data/customer_data.csv")
