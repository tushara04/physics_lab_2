import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Read the CSV file
data = pd.read_csv(r"C:\Users\ASUS\Documents\Programming\College Projects\Lab 2\Exp 2\PL2 Database - rough.csv")

# Print column names and first few rows
print(data.columns)
print(data.head())

# Assuming the first column is length and the second is period
length_column = data.columns[0]
period_column = data.columns[1]

# Convert data to numeric type and extract length and period data
length = pd.to_numeric(data[length_column], errors='coerce')
period = pd.to_numeric(data[period_column], errors='coerce')

# Remove any NaN values that might have resulted from the conversion
mask = ~(np.isnan(length) | np.isnan(period))
length = length[mask]
period = period[mask]

# Create scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(length, period, color='blue', label='Data points')

# Perform polynomial fit (degree 1 for a straight line)
coeffs = np.polyfit(length, period, 1)
poly = np.poly1d(coeffs)

# Create x values for the fit line
x_fit = np.linspace(length.min(), length.max(), 100)

# Plot the fit line
plt.plot(x_fit, poly(x_fit), color='red', label='Polynomial fit')

# Set labels and title
plt.xlabel(f'{length_column} (cm)')
plt.ylabel(f'{period_column} (s)')
plt.title(f'{period_column} vs {length_column}')
plt.legend()

# Show the plot
plt.grid(True)
plt.show()