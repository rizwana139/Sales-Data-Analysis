import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load CSV file
df = pd.read_csv(r"C:\Users\USER\Downloads\sales.csv")

# Display basic info
print("First 5 rows:\n", df.head())
print("\nSummary:\n", df.describe())

# Group by Product
product_sales = df.groupby('Product')['Sales'].sum()
print("\nTotal Sales by Product:\n", product_sales)

# Group by Region
region_sales = df.groupby('Region')['Sales'].sum()
print("\nTotal Sales by Region:\n", region_sales)

# Plotting
product_sales.plot(kind='bar', title='Sales by Product', color='skyblue')
plt.ylabel("Sales")
plt.grid(True)
plt.tight_layout()
plt.show()

region_sales.plot(kind='bar', title='Sales by Region', color='salmon')
plt.ylabel("Sales")
plt.grid(True)
plt.tight_layout()
plt.show()

