# Track Surface Analysis

## Overview
"Track Surface Analysis" is a Python script designed to process track data from a CSV file and create a matrix representation of a track surface. The script maps a path defined by geographical coordinates (latitude, longitude) and elevation data (meters above sea level) to a matrix. It also provides functionality to set a specific width for the track and visualize the height variations along the track.

## Data Format
The input data is expected to be in a CSV file named `sem_2023_us.csv`. This file should contain the following columns:
- `Latitude`: Latitude of the track points in decimal degrees.
- `Longitude`: Longitude of the track points in decimal degrees.
- `Metres above sea level`: Elevation of the track points in meters above sea level.

The script reads this data and converts the geographical coordinates into a two-dimensional matrix representation, where each point corresponds to a specific location on the track.

## Features
- **Conversion of Coordinates**: Converts latitude and longitude to meters to create a spatially accurate matrix.
- **Track Width Customization**: Allows setting a specific width for the track in the matrix representation.
- **Height Visualization**: Visualizes the height of the track, making it easier to observe elevation changes and terrain features.
- **Amplification of Height Differences**: Amplifies height differences to make variations in elevation more noticeable.
- **Margin Addition**: Adds margins to the matrix for better visualization and analysis.

## Usage
To use the script, ensure that the `sem_2023_us.csv` file is in the same directory as the script or provide the correct file path. Run the script to generate the matrix representation of the track, which is then saved to a CSV file named `TrackSurface_Wider.csv`.

## Author
[Ines Alejandro Garcia Mosqueda]

