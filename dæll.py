import matplotlib.pyplot as plt
import numpy as np

# Dæll, the old norse word for gentle.
# ᛏᛅᛚᛚ in Younger Futhark

fig, ax = plt.subplots()

# Plot overlapping lines on the same Axes (ax).
# [x], [y]
ax.plot([3, 3], [6, 1], label="Line 1")  # Stem

ax.plot([4, 2], [5, 4], label="Line 2")  # Second line
ax.plot([3, 4], [4.5, 4], label="Line 2")  # Third line
ax.plot([3, 4], [3.5, 3], label="Line 2")  # Third line
ax.plot([3, 4], [2.5, 2], label="Line 2")  # Third line

ax.plot([0, 6], [0, 0], label="Line 6")  # Underline line


plt.show()  # Show the figure.
