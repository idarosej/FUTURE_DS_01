import pandas as pd

# Sample sales data
data = {
    "Product": ["Laptop", "Phone", "Chair", "Table"],
    "Sales": [50000, 30000, 10000, 15000]
}

# Create DataFrame
df = pd.DataFrame(data)

# Calculate total revenue
total_revenue = df["Sales"].sum()

print("Business Sales Analysis")
print("-----------------------")
print(df)
print("\nTotal Revenue:", total_revenue)
import pandas as pd
import matplotlib.pyplot as plt

# Product Sales
products = ["Laptop", "Phone", "Table", "Chair"]
sales = [50000, 30000, 15000, 10000]

# Bar Chart
plt.figure(figsize=(6,4))
plt.bar(products, sales)
plt.title("Top Selling Products")
plt.xlabel("Products")
plt.ylabel("Sales")
plt.show()
