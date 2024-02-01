
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# Function to read the matrix from a CSV file
def read_matrix(file_path):
    return np.loadtxt(file_path, delimiter=',')

# Function to normalize the matrix values to 0-255
def normalize_matrix(matrix):
    normalized_matrix = 255 * (matrix - np.min(matrix)) / (np.max(matrix) - np.min(matrix))
    return normalized_matrix.astype(np.uint8)

# Function to save the normalized matrix as a heightmap image
def save_heightmap(matrix, output_file_path):
    image = Image.fromarray(matrix)
    image.save(output_file_path)

# Main code
if __name__ == '__main__':
    input_file_path = 'TrackSurface_Wider.csv' # Change to your input file path
    output_file_path = 'TrackSurface_Wider_downSample_heightmap.png' # Change to your desired output file path
    
    matrix = read_matrix(input_file_path)
    normalized_matrix = normalize_matrix(matrix)
    save_heightmap(normalized_matrix, output_file_path)
    print("height map done...")
