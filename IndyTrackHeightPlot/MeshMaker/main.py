"""
Track Surface Analysis
Author: [Ines Alejandro Garcia Mosqueda]

This script processes a dataset of geographical coordinates (latitude, longitude) and elevation data
to create a matrix representation of a track surface. It includes functionality for converting
geographical coordinates to meters, setting a wider track width, amplifying height differences,
and adding margins to the matrix. The final matrix represents the surface of the track with
height values and is saved to a CSV file.

The script uses the Haversine formula to calculate distances, applies a ground tolerance value
for areas without track data, and allows customization of track width and height amplification.
"""

import pandas as pd
import numpy as np
from scipy.ndimage import gaussian_filter

def haversine(lat1, lon1, lat2, lon2):
    """
    Calculate the great circle distance in meters between two points 
    on the earth (specified in decimal degrees).

    Parameters:
    lat1 (float): Latitude of the first point.
    lon1 (float): Longitude of the first point.
    lat2 (float): Latitude of the second point.
    lon2 (float): Longitude of the second point.

    Returns:
    float: Distance between the two points in meters.
    """

    # Convert decimal degrees to radians 
    lat1, lon1, lat2, lon2 = map(np.radians, [lat1, lon1, lat2, lon2])
    # Haversine formula 
    dlat = lat2 - lat1 
    dlon = lon2 - lon1 
    a = np.sin(dlat/2)**2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon/2)**2
    c = 2 * np.arcsin(np.sqrt(a)) 
    r = 6371000  # Radius of earth in meters
    return c * r

def set_track_width_height(matrix, track_width):
    """
    Set the height along the track width.

    Parameters:
    matrix (np.ndarray): Matrix representing the track surface.
    track_width (int): Width of the track in matrix units.

    Returns:
    np.ndarray: Modified matrix with the track width set.
    """
    height_matrix = np.full_like(matrix, np.nan)
    rows, cols = matrix.shape
    for y in range(rows):
        for x in range(cols):
            if not np.isnan(matrix[y, x]):
                for i in range(-track_width//2, track_width//2 + 1):
                    for j in range(-track_width//2, track_width//2 + 1):
                        if 0 <= y + i < rows and 0 <= x + j < cols:
                            height_matrix[y + i, x + j] = matrix[y, x]
    return height_matrix

def amplify_height_differences(matrix, amplification_factor):
    """
    Amplify the height differences in the matrix.

    Parameters:
    matrix (np.ndarray): Matrix representing the track surface.
    amplification_factor (float): Factor by which to amplify height differences.

    Returns:
    np.ndarray: Matrix with amplified height differences.
    """
    min_height = np.nanmin(matrix)
    amplified_matrix = (matrix - min_height) * amplification_factor + min_height
    return amplified_matrix

# Ground tolerance and margins
gnd_tol = 2
margin_rows = 150  # Number of additional rows for margin
margin_cols = 150  # Number of additional columns for margin

# Load the data from the file
file_path = 'sem_2023_us.csv'  # Replace with your file path
data = pd.read_csv(file_path)

# Get minimum latitude and longitude
min_lat, min_lon = data['Latitude'].min(), data['Longitude'].min()

# Convert all coordinates to meters from the minimum point
data['X_meters'] = data.apply(lambda row: haversine(min_lat, min_lon, min_lat, row['Longitude']), axis=1)
data['Y_meters'] = data.apply(lambda row: haversine(min_lat, min_lon, row['Latitude'], min_lon), axis=1)

# Create a matrix with margins and map the coordinates to height values
max_x, max_y = int(data['X_meters'].max()), int(data['Y_meters'].max())
track_matrix = np.full((max_y + 1 + margin_rows, max_x + 1 + margin_cols), np.nan)  # Initialize with NaNs and margins
for _, row in data.iterrows():
    x, y, height = int(row['X_meters']), int(row['Y_meters']), row['Metres above sea level']
    track_matrix[y + margin_rows//2, x + margin_cols//2] = height  # Adjust for margin offset

# Set a wider track width in meters (example: 100 meters)
track_width = 60

# Set the height along the wider track width
wider_track_matrix = set_track_width_height(track_matrix, track_width)

# Set height for areas without track data
min_height = data['Metres above sea level'].min() - gnd_tol
wider_track_matrix[np.isnan(wider_track_matrix)] = min_height

# Amplification factor for height differences
height_amplification_factor = 35  # Adjust this factor to increase/decrease the exaggeration

# Amplify height differences in the track matrix
amplified_track_matrix = amplify_height_differences(wider_track_matrix, height_amplification_factor)

# Save the updated matrix with wider track to a CSV file
output_file_path = 'TrackSurface_Wider.csv'  # Change the path as needed
np.savetxt(output_file_path, amplified_track_matrix, delimiter=',', fmt='%.4f')
