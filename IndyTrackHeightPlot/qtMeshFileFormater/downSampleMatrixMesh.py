import numpy as np
import pandas as pd

def compress_matrix(input_file, output_file, compression_factor=4):
    # Load the matrix from the input CSV file
    matrix = pd.read_csv(input_file, header=None).values

    # Get the dimensions of the matrix
    rows, cols = matrix.shape

    # Calculate the dimensions of the compressed matrix
    compressed_rows = rows // compression_factor + (rows % compression_factor > 0)
    compressed_cols = cols // compression_factor + (cols % compression_factor > 0)

    # Initialize the compressed matrix
    compressed_matrix = np.zeros((compressed_rows, compressed_cols))

    # Compress the matrix
    for i in range(compressed_rows):
        for j in range(compressed_cols):
            row_start = i * compression_factor
            row_end = min((i + 1) * compression_factor, rows)
            col_start = j * compression_factor
            col_end = min((j + 1) * compression_factor, cols)
            block = matrix[row_start:row_end, col_start:col_end]
            compressed_matrix[i, j] = np.mean(block)

    # Write the compressed matrix to the output CSV file
    pd.DataFrame(compressed_matrix).to_csv(output_file, header=False, index=False)

# Example usage
input_file = 'TrackSurface_Wider.csv'  # Replace with the path to your input file
output_file = 'TrackSurface_Wider_downSample.csv'  # Replace with the path to your output file
compress_matrix(input_file, output_file)
print(f"Downsampled matrix saved to {output_file}")