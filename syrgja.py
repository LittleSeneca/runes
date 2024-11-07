import matplotlib.pyplot as plt
import numpy as np

# syrgja, the old norse word for Mourn.
# ᛋᚢᚱᚴᛁᛅ in Younger Futhark

fig, ax = plt.subplots()

# Plot overlapping lines on the same Axes (ax).
# [x], [y]
ax.plot([3, 3], [6.5, 1], label="Line 1")  # Stem

ax.plot([4, 2], [5, 4], label="Line 2")  # Second line
ax.plot([2, 2], [4, 6], label="Line 2")  # Third line
ax.plot([3, 4], [4.5, 4], label="Line 2")  # Fourth line
ax.plot([4, 4], [4, 2], label="Line 2")  # Fifth line
ax.plot([4, 3], [4, 3], label="Line 2")  # Sixth line
ax.plot([3, 4], [3, 2], label="Line 2")  # Seventh line

ax.plot([0, 6], [0, 0], label="Line 6")  # Underline line


plt.show()  # Show the figure.
