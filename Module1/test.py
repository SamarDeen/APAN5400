import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data_path = '/Users/sd/Documents/APAN5400/data/companies.csv'

# Load the data
df = pd.read_csv(data_path)

print(df.columns)

# Print the data
print(df.shape)
print(df.head())

# 1. Sort by revenue
print(df[['revenue','employees']])
df = df.astype({'revenue': int, 'employees': int})
df = df.sort_values(by='revenue', ascending=False)
print("Sorted by revenue")
print(df[['revenue','employees']])

# Plot numeric columns from companies.csv
# x axis employees in 000s, y axis revenue in 000s
plt.scatter(pd.to_numeric(df['revenue']),pd.to_numeric(df['employees']) / 1000000)
plt.ylabel('Employees (millions)')
plt.xlabel('Revenue')
plt.title('Company employees vs revenue')
plt.show()

# 2. Fit a first-degree polynomial (a line) to log(x) and y
# This finds the slope (m) and intercept (c) for the equation: y = m * log(x) + c
slope, intercept = np.polyfit(np.log(df['revenue']), df['employees'], 1)

# 3. Calculate the predicted Y values for the fit line
y_fit = slope * np.log(df['revenue']) + intercept

#print(y_fit,df['revenue'])

# 4. Create the plot
plt.figure(figsize=(8, 5))

# Plot the original scatter points
plt.scatter(df['revenue'], df['employees'], color='darkorange', alpha=0.7, label='Data Points')

# Plot the logarithmic trend line
plt.plot(df['revenue'], y_fit, color='royalblue', linewidth=2.5, label=f'Log Fit: y = {slope:.2f}*ln(x) + {intercept:.2f}')

# Formatting
plt.title("Scatter Plot with Logarithmic Fit Line", fontsize=14)
plt.xlabel("Revenue", fontsize=12)
plt.ylabel("Employees (million)", fontsize=12)
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)

# Display the chart
plt.show()
