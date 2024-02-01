import pandas as pd

# Load the CSV file
file_path = 'TrackSurface_Wider_downSample.csv'
df = pd.read_csv(file_path, header=None)

# Open a file to write the output
output_file = 'ConvertedTrackData.txt'
with open(output_file, 'w') as f:
    # Write the preamble
    f.write('ListModel {\n')

    # Iterate over the DataFrame and write each element
    for row in range(df.shape[0]):
        for col in range(df.shape[1]):
            f.write(f'    ListElement {{ row: {row}; column: {col}; value: {df.iloc[row, col]} }}\n')

    # Write the closing tag
    f.write('}')

# Print a success message
print("Conversion complete. Output saved to:", output_file)
