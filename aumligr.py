import matplotlib.pyplot as plt
import numpy as np

# Aumligr, the old norse word for Poor.
# ᛅᚢᛘᛚᛁᚴᚱ in Younger Futhark

fig, ax = plt.subplots()

# Plot overlapping lines on the same Axes (ax).
# [x], [y]
ax.plot([3, 3], [6, 1], label="Line 1")  # Stem

ax.plot([4, 2], [5, 4], label="Line 2")  # Second line
ax.plot([2, 4], [5, 4], label="Line 3")  # Second line
ax.plot([4, 3], [4, 3], label="Line 4")  # Second line
ax.plot([4, 4], [2, 4], label="Line 5")  # Second line
ax.plot([3, 4], [3, 2], label="Line 6")  # Second line
ax.plot([0, 6], [0, 0], label="Line 6")  # Second line


plt.show()  # Show the figure.
