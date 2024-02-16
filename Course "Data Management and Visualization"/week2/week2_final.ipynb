# Import the pandas library with the alias pd
import pandas as pd
# Import the numpy library with the alias np
import numpy as np


# Read the CSV file into a DataFrame, setting standard options like delimiter and memory management
df_craters_csv = pd.read_csv("D:/Data Analyst/Teil2_Visualisieren/marscraters.csv", sep=",", low_memory=False)

# Define variables for the column names for latitude, longitude, and diameter
latitude = "LATITUDE_CIRCLE_IMAGE"
longitude = "LONGITUDE_CIRCLE_IMAGE"
diam = "DIAM_CIRCLE_IMAGE"

# Create a new DataFrame that only contains the required columns
df_craters = df_craters_csv[[latitude, longitude, diam]]

# Define a dictionary to set conditions for each quadrant and special lines that determine whether a crater belongs to it
quadrants = {"Q1": (df_craters[longitude] > 0) & (df_craters[latitude] > 0),
             "Q2": (df_craters[longitude] > 0) & (df_craters[latitude] < 0),
             "Q3": (df_craters[longitude] < 0) & (df_craters[latitude] < 0),
             "Q4": (df_craters[longitude] < 0) & (df_craters[latitude] > 0),
             "Equator": (df_craters[longitude] != 0) & (df_craters[latitude] == 0),
             "Prime Meridian": (df_craters[longitude] == 0) & (df_craters[latitude] != 0)
            }

# Print the headings for the statistics output
print("Quadrant \t\t Number \t Percent \t Avg Crater Area (km²) \t Largest Crater \t Smallest Crater")

# Loop through all quadrants to calculate and print statistics
for quadrant, value in quadrants.items():
    # Calculate the percentage of craters in this quadrant relative to the total number
    percentage = value.sum() / len(df_craters) * 100
    # Calculate the sum of diameters of all craters in this quadrant
    diam_sum = df_craters.loc[quadrants[quadrant], diam].sum() 
    # Calculate the total crater area in this quadrant (assumption: craters are circular)
    area_sum = (diam_sum/2)**2*np.pi
    # Calculate the average crater area in this quadrant
    area_average = area_sum / value.sum()
    # Determine the largest diameter in this quadrant
    biggest_diam = df_craters.loc[quadrants[quadrant], diam]    
    max_value = biggest_diam.max()
    # Determine the smallest diameter in this quadrant
    smallest_diam = df_craters.loc[quadrants[quadrant], diam]    
    min_value = smallest_diam.min()
    # Print the statistics for this quadrant
    print(f"{quadrant:<15} \t {value.sum():<10} \t {percentage:<10.4f} \t {area_average:<15.0f} \t {max_value:<15.2f} \t {min_value:<15.2f}")

