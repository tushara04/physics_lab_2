import numpy as np
import matplotlib.pyplot as plt
import csv

# Read data from CSV file
frequencies = []
gains = []

with open("C://Users//ASUS//Documents//Programming//College Projects//Lab 2//Exp 1//PL2 Database - rough3.csv", 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader)  # Skip header row if present
    for row in csvreader:
        frequencies.append(float(row[0]))
        gains.append(float(row[1]))

# Convert to numpy arrays
frequencies = np.array(frequencies)
gains = np.array(gains)

# Error in gain (constant for all points)
gain_error = 0.5208

# Create scatter plot with error bars
plt.figure(figsize=(12, 8))
plt.errorbar(frequencies, gains, yerr=gain_error, fmt='o', ecolor="black",
            label='Data points', capsize=5)

# Create polyfit line
log_frequencies = np.log10(frequencies)
coeffs = np.polyfit(log_frequencies, gains, 3)  # Using a 3rd degree polynomial
poly = np.poly1d(coeffs)

# Generate points for smooth curve
x_smooth = np.logspace(np.log10(min(frequencies)), np.log10(max(frequencies)), 1000)
y_smooth = poly(np.log10(x_smooth))

# Plot polyfit line
plt.plot(x_smooth, y_smooth, color='red', label='Polyfit line')

# Set x-axis to log scale
plt.xscale('log')

# Add cutoff frequency line
cutoff_freq = 26703.53756
plt.axvline(x=cutoff_freq, color='green', linestyle='--', label='Cutoff Frequency')

# Labels and title
plt.xlabel('Angular Frequency (rad/s)')
plt.ylabel('Gain (dB)')
plt.title('Gain vs Angular Frequency')

# Add legend
plt.legend()

# Add grid
plt.grid(True, which="both", ls="-", alpha=0.2)

# Set custom x-axis ticks
plt.xticks([4000, 6000, 8000, 10000, 20000, 26703.53756, 40000, 60000], 
           ['4000', '6000', '8000', '10000', '20000', '26703.54\n(cutoff)', '40000', '60000'])

# Show plot
plt.tight_layout()
plt.show()