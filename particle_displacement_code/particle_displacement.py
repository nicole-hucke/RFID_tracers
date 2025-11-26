

###############################################################
# Importing libraries
import math
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Polygon
import numpy as np
import pandas as pd
import os

################################################################
# Defining some functions

# def do_they_intersect
def do_they_intersect(x1, y1, r1, x2, y2, r2):
    # Distance between both centers
    distance = np.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    tempBool1 = True
    # Do they intersect?
    if distance > (r1 + r2) or distance < abs(r1 - r2):
        tempBool1 = False
       
    return tempBool1

# def get_intersection_area
def get_intersection_area(center1, radius1, center2, radius2):
    d = math.dist(center1, center2)  # Distance between centers
    # Check if the circles do not overlap
    if d >= (radius1 + radius2):
        return 0.0
    # Check if one circle is completely inside the other
    if d <= abs(radius1 - radius2):
        return math.pi * min(radius1, radius2)**2
    
    # Calculate the area of intersection
    r1_sq = radius1**2
    r2_sq = radius2**2
    alpha = math.acos((r1_sq + d**2 - r2_sq) / (2 * radius1 * d)) * 2
    beta = math.acos((r2_sq + d**2 - r1_sq) / (2 * radius2 * d)) * 2
    segment_area1 = 0.5 * r1_sq * (alpha - math.sin(alpha))
    segment_area2 = 0.5 * r2_sq * (beta - math.sin(beta))
    intersection_area = segment_area1 + segment_area2
    
    return intersection_area

# def plot2circles
def plot_two_circles(center1, radius1, center2, radius2, save_results_to=None):
    fig, ax = plt.subplots()
    circle1 = plt.Circle(center1, radius1, fill=False, edgecolor='k', linestyle='-', linewidth=1)
    circle2 = plt.Circle(center2, radius2, fill=False, edgecolor='r', linestyle='-', linewidth=1)
    ax.add_patch(circle1)
    ax.add_patch(circle2)
    ax.plot(center1[0], center1[1], 'ko')  # 'bo' is blue color with 'o' marker
    ax.plot(center2[0], center2[1], 'ro')  # 'ro' is red color with 'o' marker
    ax.plot([center1[0], center2[0]], [center1[1], center2[1]], 'b--')  # 'k--' is black dashed line
    ax.set_aspect('equal', 'box')
    min_x = min(center1[0] - radius1, center2[0] - radius2)
    max_x = max(center1[0] + radius1, center2[0] + radius2)
    min_y = min(center1[1] - radius1, center2[1] - radius2)
    max_y = max(center1[1] + radius1, center2[1] + radius2)
    ax.set_xlim(min_x - 1, max_x + 1)
    ax.set_ylim(min_y - 1, max_y + 1)
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title("Particle displacement")
    plt.grid(True)
    if save_results_to != None:
        plt.savefig(save_results_to, dpi=300)
    plt.show()

# Defining the main function
def get_rock_displacement(location1, location2, radius1, radius2):
    # Calculating the distance betweeen both
    distance = np.sqrt(np.sum((location1 - location2)**2))
    
    # Checking intersection
    intersect = do_they_intersect(location1[0], location1[1], radius1,
                                  location2[0], location2[1], radius2)

    # Calculations depending on whether circles intersect or not
    if intersect == True:
        tempCalc1 = distance + (radius1 + radius2)
        maxD = tempCalc1
        minD = 0
        tempCalc1 = np.pi*radius1**2
        tempCalc2 = np.pi*radius2**2
        tempCalc3 = get_intersection_area(location1, radius1, location2, radius2)
        ratio_minA = tempCalc3/np.min((tempCalc1, tempCalc2))
        ratio_maxA = tempCalc3/np.max((tempCalc1, tempCalc2))
        intersection_area = tempCalc3
    else:
        tempCalc1 = distance + (radius1 + radius2)
        tempCalc2 = distance - (radius1 + radius2)
        maxD = tempCalc1
        minD = np.max((tempCalc2, 0))
        ratio_minA = 0
        ratio_maxA = 0
        intersection_area = 0

    return distance, intersect, maxD, minD, intersection_area, ratio_minA, ratio_maxA

#################################################################
# Performing the analysis

# Checking environment and working directory
os.getcwd()
working_directory = "C:/Users/bern9483/Documents/Nicole/tracers_data/"
os.chdir(working_directory)

# Filenames and directories
filename1 = "./triangulated_tracer_survey_03_28_2022.csv"
filename2 = "./triangulated_tracer_survey_07_06_2022.csv"
filename3 = "./triangulated_tracer_survey_08_06_2022.csv"
filename4 = "./triangulated_tracer_survey_08_09_2022.csv"
filename5 = "./triangulated_tracer_survey_08_24_2022.csv"
filename6 = "./triangulated_tracer_survey_03_24_2023.csv"
filename7 = "./triangulated_tracer_survey_06_17_2023.csv"
filename8 = "./triangulated_tracer_survey_07_31_2023.csv"
filename9 = "./triangulated_tracer_survey_09_20_2023.csv"
results_directory = "./results/"
dates = ["03_28_2022", "07_06_2022", "08_06_2022", "08_09_2022", "08_24_22", "03_24_2023", "06_17_2023", "07_31_2023", "09_20_2023"]

# Reading files
dataframe1 = pd.read_csv(filename1)
dataframe2 = pd.read_csv(filename2)
dataframe3 = pd.read_csv(filename3)
dataframe4 = pd.read_csv(filename4)
dataframe5 = pd.read_csv(filename5)
dataframe6 = pd.read_csv(filename6)
dataframe7 = pd.read_csv(filename7)
dataframe8 = pd.read_csv(filename8)
dataframe9 = pd.read_csv(filename9)

# Changing the indices
dataframe1.index = dataframe1["ParticleID"].astype(np.int64)
dataframe2.index = dataframe2["ParticleID"].astype(np.int64)
dataframe3.index = dataframe3["ParticleID"].astype(np.int64)
dataframe4.index = dataframe4["ParticleID"].astype(np.int64)
dataframe5.index = dataframe5["ParticleID"].astype(np.int64)
dataframe6.index = dataframe6["ParticleID"].astype(np.int64)
dataframe7.index = dataframe7["ParticleID"].astype(np.int64)
dataframe8.index = dataframe8["ParticleID"].astype(np.int64)
dataframe9.index = dataframe9["ParticleID"].astype(np.int64)

# Dropping duplicates JUST FO RTHE EXAMPLE
# dataframe1 = dataframe1.drop_duplicates(subset="ParticleID")
# dataframe2 = dataframe2.drop_duplicates(subset="ParticleID")
# dataframe3 = dataframe3.drop_duplicates(subset="ParticleID")
# dataframe4 = dataframe4.drop_duplicates(subset="ParticleID")
# dataframe5 = dataframe5.drop_duplicates(subset="ParticleID")
# dataframe6 = dataframe6.drop_duplicates(subset="ParticleID")
# dataframe7 = dataframe7.drop_duplicates(subset="ParticleID")
# dataframe8 = dataframe8.drop_duplicates(subset="ParticleID")
# dataframe9 = dataframe9.drop_duplicates(subset="ParticleID")

# Sorting them
dataframe1 = dataframe1.sort_index()
dataframe2 = dataframe2.sort_index()
dataframe3 = dataframe3.sort_index()
dataframe4 = dataframe4.sort_index()
dataframe5 = dataframe5.sort_index()
dataframe6 = dataframe6.sort_index()
dataframe7 = dataframe7.sort_index()
dataframe8 = dataframe8.sort_index()
dataframe9 = dataframe9.sort_index()

# Resetting the indices and filling it up
full_index = range(0, 1100)

dataframe1 = dataframe1.reindex(full_index)
dataframe2 = dataframe2.reindex(full_index)
dataframe3 = dataframe3.reindex(full_index)
dataframe4 = dataframe4.reindex(full_index)
dataframe5 = dataframe5.reindex(full_index)
dataframe6 = dataframe6.reindex(full_index)
dataframe7 = dataframe7.reindex(full_index)
dataframe8 = dataframe8.reindex(full_index)
dataframe9 = dataframe9.reindex(full_index)

# Getting data
indices = np.array(full_index)

# location1 = np.column_stack((dataframe1["X"].to_numpy(), dataframe1["Y"].to_numpy()))
# location2 = np.column_stack((dataframe2["X"].to_numpy(), dataframe2["Y"].to_numpy()))
# location3 = np.column_stack((dataframe3["X"].to_numpy(), dataframe3["Y"].to_numpy()))
# location4 = np.column_stack((dataframe4["X"].to_numpy(), dataframe4["Y"].to_numpy()))
# location5 = np.column_stack((dataframe5["X"].to_numpy(), dataframe5["Y"].to_numpy()))

# radius1 = dataframe1["ConfidenceRadius"].to_numpy()
# radius2 = dataframe2["ConfidenceRadius"].to_numpy()
# radius3 = dataframe3["ConfidenceRadius"].to_numpy()
# radius4 = dataframe4["ConfidenceRadius"].to_numpy()
# radius5 = dataframe5["ConfidenceRadius"].to_numpy()

location_x = np.column_stack((dataframe1["X"].to_numpy(), 
                              dataframe2["X"].to_numpy(), 
                              dataframe3["X"].to_numpy(), 
                              dataframe4["X"].to_numpy(), 
                              dataframe5["X"].to_numpy(),
                              dataframe6["X"].to_numpy(),
                              dataframe7["X"].to_numpy(),
                              dataframe8["X"].to_numpy(),
                              dataframe9["X"].to_numpy()))

location_y = np.column_stack((dataframe1["Y"].to_numpy(), 
                              dataframe2["Y"].to_numpy(), 
                              dataframe3["Y"].to_numpy(), 
                              dataframe4["Y"].to_numpy(), 
                              dataframe5["Y"].to_numpy(),
                              dataframe6["Y"].to_numpy(),
                              dataframe7["Y"].to_numpy(),
                              dataframe8["Y"].to_numpy(),
                              dataframe9["Y"].to_numpy()))

radius = np.column_stack((dataframe1["ConfidenceRadius"].to_numpy(), 
                          dataframe2["ConfidenceRadius"].to_numpy(),
                          dataframe3["ConfidenceRadius"].to_numpy(),
                          dataframe4["ConfidenceRadius"].to_numpy(),
                          dataframe5["ConfidenceRadius"].to_numpy(),
                          dataframe6["ConfidenceRadius"].to_numpy(),
                          dataframe7["ConfidenceRadius"].to_numpy(),
                          dataframe8["ConfidenceRadius"].to_numpy(),
                          dataframe9["ConfidenceRadius"].to_numpy()))

# Creating a small dataframe to store results
column_names = ["ID", "Date1", "Date2", "DistanceD", "intersect?", "MaxD", "MinD", "intersection_Area", "Ratio_MinA", "Ratio_MaxA"]
#results = pd.DataFrame(columns=column_names)
tempCalc1 = {"ID": indices}
results = pd.DataFrame(tempCalc1)
temp_results = pd.DataFrame(columns=column_names)

# Going through each rock in each timestep
for j in range(len(dates)-1):
    for i in range(len(indices)):
        index = indices[i]
        loc1 = np.array([location_x[i,j], location_y[i,j]])
        loc2 = np.array([location_x[i,j+1], location_y[i,j+1]])
        rad1 = radius[i,j]
        rad2 = radius[i,j+1]
        # Calculating displacement
        distance, intersect, maxD, minD, intersection_area, ratio_minA, ratio_maxA = get_rock_displacement(loc1, loc2, rad1, rad2)
        # Storing results
        temp_results.loc[i] = [index, dates[j], dates[j+1], distance, intersect, maxD, minD, intersection_area, ratio_minA, ratio_maxA]
    results = pd.concat([results, temp_results], axis=1)

# Saving results
results.to_csv("results2.csv", index=False, header=True, sep=',')

