import pandas as pd
import matplotlib.pyplot as plt
import os

print("Current working directory:", os.getcwd())

try:
    data = pd.read_csv("sales_data.csv")
    print("CSV loaded successfully.")
except FileNotFoundError:
    print(f"Error: file not found at 'sales_data.csv'")
    exit()

print(data.head())

# Correct datetime conversion
data['Date'] = pd.to_datetime(data['Date'])

# Plotting
plt.figure(figsize=(10, 5))
plt.plot(data['Date'], data['Sales'], marker='o', linestyle='-', color='blue')
plt.title('Sales Over Time')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.grid(True)
plt.tight_layout()
plt.show()
