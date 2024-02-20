import numpy as np
def is_gray(color, threshold):
    """Check if a color is considered gray.

    Args:
        color: A tuple representing the RGB values of the color.
        threshold: The threshold for considering the color as gray.

    Returns:
        True if the color is considered gray, False otherwise.
    """
    return all(abs(color[i] - color[(i + 1) % 3]) < threshold for i in range(3))

def convert_image_to_cells(image, cell_size):
    """Converts an image to cells based on color.

    Args:
        image: A NumPy array representing the image.
        cell_size: The size of each cell in pixels.

    Returns:
        A NumPy array representing the cells, where each element is the average color
        of the corresponding cell in the original image.
    """

    # Check if the image is a 3-channel BGR image
    if len(image.shape) != 3 or image.shape[2] != 3:
        raise ValueError("Image must be a 3-channel BGR image.")

    height, width = image.shape[:2]  # Unpack the width and height
    cells = np.zeros((height // cell_size, width // cell_size, 3), dtype=np.uint8)

    for i in range(height // cell_size ):
        for j in range(width // cell_size):
            # Get the slice of the image corresponding to the current cell
            cell_image = image[i * cell_size : (i + 1) * cell_size,
                               j * cell_size : (j + 1) * cell_size]

            # Calculate the average color of the cell
            cell_color = np.mean(cell_image, axis=(0, 1))

            # Define the threshold values for each color
            green_threshold = 100
            black_threshold = 150
            red_threshold = 100

            # Check if the average color falls within the threshold ranges
            if (cell_color[0] <= black_threshold and
                cell_color[1] <= black_threshold and
                cell_color[2] <= black_threshold):
                # If the color is close to black, assign black
                cell_color = [0, 0, 0]
            elif (cell_color[0] < red_threshold and
                  cell_color[1] > green_threshold and 
                  cell_color[2] < red_threshold):
                # If the color is close to green, assign green
                cell_color = [6, 252, 6]
            elif (cell_color[0] < red_threshold and
                  cell_color[1] < green_threshold and 
                  cell_color[2] > red_threshold - 80):
                # If the color is close to red, assign red
                cell_color = [4, 4, 252]
            else:
                # If the color does not match any of the specified colors, assign white
                cell_color = [255, 255, 255]

            # Assign the color to the corresponding cell in the output array
            cells[i, j] = cell_color

    return cells

import cv2


# Load the image
image = cv2.imread('Test2.bmp')

# Convert the image to cells
cells = convert_image_to_cells(image, cell_size=4)

# Save the cells to a file (optional)
cv2.imwrite("cells_Test.bmp", cells)

print(cells.shape)
