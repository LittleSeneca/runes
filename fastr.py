import matplotlib.pyplot as plt
import numpy as np

# fastr, the old norse word for holdfast.
# ᚠᛅᛋᛏᚱ in Younger Futhark

fig, ax = plt.subplots()

# Plot overlapping lines on the same Axes (ax).
# [x], [y]
ax.plot([3, 3], [6.5, 0.5], label="Line 1")  # Stem
ax.plot([3, 3.5], [5, 5.5], label="Line 1")  # First Line
ax.plot([3, 4], [4.5, 5.5], label="Line 1")  # Second Line
ax.plot([2, 3], [3.5, 4.5], label="Line 1")  # Third Line
ax.plot([2, 2], [3.5, 5.5], label="Line 1")  # Fourth Line
ax.plot([3, 4], [4.5, 3.5], label="Line 1")  # Fifth Line
ax.plot([4, 3], [3.5, 2.5], label="Line 1")  # Sixth Line
ax.plot([3, 4], [2.5, 1.5], label="Line 1")  # Seventh Line

ax.plot([0, 6], [0, 0], label="Line 6")  # Underline line


plt.show()  # Show the figure.
