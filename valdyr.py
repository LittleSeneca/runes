import matplotlib.pyplot as plt
from PIL import Image


# Function to generate the bind rune
def generate_bind_rune():
    # Updated colors
    bright_blue = "#7078FF"  # Brighter blue color
    bright_pink = "#FF69B4"  # Bright pink color for the circles
    bright_green = "#39FF14"
    reddish_purple = "#8B008B"

    fig, ax = plt.subplots()

    # Set the figure and axes background to be transparent
    fig.patch.set_alpha(0)
    ax.patch.set_alpha(0)

    # Original x-values range
    x_min = 1.0
    x_max = 3.0
    x_center = (x_min + x_max) / 2  # 2.0

    # Original y-values range
    y_min = 1.3  # Approximate value considering vertical_offset
    y_max = 6.0

    # Calculate scaling factor to equalize width and height
    height = y_max - y_min  # 4.7
    width = x_max - x_min  # 2.0
    scale_factor = 0.8 * height / width  # 2.35

    # Scaling function for x-coordinates
    def scale_x(x):
        return x_center + (x - x_center) * scale_factor

    # Shift x-values to center the drawing within new x-axis limits
    # No need for x_shift now since scaling centers the plot

    # Plot the rune lines with adjusted x-coordinates
    ax.plot([scale_x(3), scale_x(3)], [5.5, 3.0], color=bright_blue, linewidth=6)
    ax.plot([scale_x(2), scale_x(3)], [6, 5.5], color=bright_blue, linewidth=6)
    ax.plot([scale_x(1.2), scale_x(2.8)], [4, 5], color=bright_blue, linewidth=6)
    ax.plot([scale_x(2), scale_x(2.8)], [4.5, 4.0], color=reddish_purple, linewidth=6)
    ax.plot([scale_x(1.5), scale_x(2)], [3.45, 3.8], color=bright_blue, linewidth=6)
    ax.plot([scale_x(1), scale_x(2)], [5.0, 4.5], color=reddish_purple, linewidth=6)
    ax.plot([scale_x(1), scale_x(1)], [5.0, 1.5], color=reddish_purple, linewidth=6)
    ax.plot(
        [scale_x(2), scale_x(2.8)], [4.5, 4.0], color=reddish_purple, linewidth=6
    )  # Duplicate line removed
    ax.plot([scale_x(2.8), scale_x(2)], [4.0, 3.0], color=reddish_purple, linewidth=6)
    ax.plot([scale_x(2), scale_x(2.8)], [3, 2], color=bright_blue, linewidth=6)

    # Common Stem (shared by all runes)
    ax.plot([scale_x(2), scale_x(2)], [5.98, 2], color=bright_blue, linewidth=9)

    # Dot size reduction (25% of original size)
    dot_size = 60  # Adjusted size for better visibility with bolder lines

    # Vertical offset for the dots
    vertical_offset = 0.2  # Adjust the vertical offset as needed

    # Plot the circles (dots) **after** the lines so they appear on top
    # Add zorder to ensure dots appear above lines
    ax.scatter(
        scale_x(2), 1.9 - vertical_offset, color=bright_green, s=dot_size, zorder=3
    )
    ax.scatter(scale_x(2), 6.20 - vertical_offset, color=bright_green, s=120, zorder=3)
    ax.scatter(scale_x(2), 4.70 - vertical_offset, color=bright_green, s=300, zorder=3)
    ax.scatter(scale_x(2), 4.00 - vertical_offset, color=bright_green, s=200, zorder=3)
    ax.scatter(scale_x(2), 3.20 - vertical_offset, color=bright_green, s=200, zorder=3)
    ax.scatter(
        scale_x(2.78), 4.20 - vertical_offset, color=bright_pink, s=120, zorder=3
    )

    ax.scatter(
        scale_x(3), 2.9 - vertical_offset, color=bright_green, s=dot_size, zorder=3
    )
    ax.scatter(
        scale_x(3), 5.7 - vertical_offset, color=bright_green, s=dot_size, zorder=3
    )

    ax.scatter(
        scale_x(1), 1.4 - vertical_offset, color=bright_pink, s=dot_size, zorder=3
    )
    ax.scatter(scale_x(1), 5.19 - vertical_offset, color=bright_pink, s=90, zorder=3)

    # Set limits and make aspect ratio equal

    ax.set_xlim(-0.75, 4.75)
    ax.set_ylim(0.75, 6.25)

    ax.set_aspect("equal", "box")

    # Remove axis for aesthetic purposes
    ax.axis("off")

    # Save the figure in different formats and sizes

    # Set the figure size to be square
    fig.set_size_inches(5, 5)

    plt.savefig(
        "bind_rune.png",
        format="png",
        dpi=1000,
        transparent=True,
        bbox_inches="tight",
        pad_inches=0,
    )
    plt.savefig(
        "bind_rune.svg",
        format="svg",
        transparent=True,
        bbox_inches="tight",
        pad_inches=0,
    )

    # WebP format
    plt.savefig(
        "bind_rune.webp",
        format="webp",
        dpi=1000,
        transparent=True,
        bbox_inches="tight",
        pad_inches=0,
    )

    plt.close(fig)  # Close the figure to free memory

    # Open the saved image and save it without resizing
    img = Image.open("bind_rune.png")

    # Export favicon.ico (requires multiple sizes)
    img.save("favicon.ico", format="ICO", sizes=[(16, 16), (32, 32), (48, 48)])

    # Save other sizes without resizing the original image
    sizes = [(192, 192), (257, 265), (16, 16), (32, 32), (150, 150)]
    for size in sizes:
        img_resized = img.resize(size, Image.Resampling.LANCZOS)
        img_resized.save(f"bind_rune_{size[0]}x{size[1]}.png", format="png")


# Generate the bind rune and export in various formats and sizes
generate_bind_rune()
