import numpy as np
import matplotlib.pyplot as plt

# Set the style to default
plt.style.use('default')

# Generate time array (slightly longer to avoid cutoff)
t = np.linspace(0, 4.001, 1001)

# Generate square wave (shifted up and increased amplitude)
square_wave = np.where((t % 1) < 0.5, 2.0, 0.0)

# Generate triangle wave (shifted down and phase-shifted)
triangle_wave = 2 * np.abs(2 * ((t + 0.5) % 1) - 1) - 2

# Create the plot
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(t, square_wave, color='yellow', linewidth=2)
ax.plot(t, triangle_wave, color='lightblue', linewidth=2)

# Set the plot style to resemble the oscilloscope
ax.grid(True, linestyle=':', color='white', alpha=0.5)

# Remove axis labels
ax.set_xlabel('')
ax.set_ylabel('')

# Set axis limits
ax.set_xlim(0, 4)
ax.set_ylim(-2.5, 2.5)

# Add title to match the oscilloscope display
ax.set_title('M Pos: 0.000s', loc='right', color='white', fontsize=10)

# Remove ticks and labels
ax.tick_params(axis='both', which='both', length=0, labelbottom=False, labelleft=False)

# Add x and y axes in the middle
ax.axhline(y=0, color='white', linewidth=0.5)
ax.axvline(x=2, color='white', linewidth=0.5)

# Set the background color to dark
ax.set_facecolor('black')

# Remove the frame
for spine in ax.spines.values():
    spine.set_visible(False)

# Set the figure background to match the axes
fig.patch.set_facecolor('black')

# Show the plot
plt.show()
