# import numpy as np
# import matplotlib.pyplot as plt
# import csv

# # Define grid parameters
# latitude_start = 15.0
# latitude_end = 18.0
# longitude_start = 78.0
# longitude_end = 81.0
# row_step = 0.08333000
# col_step = 0.08333000

# # Read values from CSV file
# values = []
# with open('revarse.csv', 'r') as file:
#     reader = csv.reader(file)
#     for i, row in enumerate(reader):
#         if i < 37:  # Exclude the last row
#             if row: 
#                 values.extend(map(float, row[0].split()))  

# # Adjust the number of steps
# num_steps = 37
# latitudes = np.linspace(latitude_start, latitude_end, num_steps)
# longitudes = np.linspace(longitude_start, longitude_end, num_steps)

# # Create meshgrid
# lon_grid, lat_grid = np.meshgrid(longitudes, latitudes)

# # Plot grid points with values
# plt.figure(figsize=(15, 10))
# for lat, lon, val in zip(lat_grid.flatten(), lon_grid.flatten(), values):
#     plt.scatter(lon, lat, color='red', zorder=5)  # scatter points with lower zorder
#     plt.annotate(f'{val:.5f}', (lon, lat), textcoords="offset points", xytext=(0,10), ha='center', fontsize=8, color='black')
# plt.xlabel('Longitude')
# plt.ylabel('Latitude')
# plt.title('Grid Points Visualization with Values')
# plt.grid(True)
# plt.show()


import numpy as np
import matplotlib.pyplot as plt
import csv

# Define grid parameters
latitude_start = 15.0
latitude_end = 18.0
longitude_start = 78.0
longitude_end = 81.0
row_step = 0.08333000
col_step = 0.08333000

# Read values from CSV file
values = []
with open('revarse.csv', 'r') as file:
    reader = csv.reader(file)
    for i, row in enumerate(reader):
        if i < 37:  # Exclude the last row
            if row: 
                values.extend(map(float, row[0].split()))  

# Adjust the number of steps
num_steps = 37
latitudes = np.linspace(latitude_start, latitude_end, num_steps)
longitudes = np.linspace(longitude_start, longitude_end, num_steps)

# Create meshgrid
lon_grid, lat_grid = np.meshgrid(longitudes, latitudes)

# Reshape values to match lat_grid and lon_grid shape
values = np.array(values).reshape(lat_grid.shape)

# Plot heatmap
plt.figure(figsize=(15, 10))
plt.imshow(values, extent=[longitude_start, longitude_end, latitude_start, latitude_end], cmap='hot', aspect='auto', origin='lower')
plt.colorbar(label='Values')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.title('Heatmap Visualization')
plt.grid(True)

# Add annotations

plt.savefig('geoid.png')
# plt.show()
