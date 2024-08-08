
###############################################################
# Importing libraries
import math
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Polygon
import numpy as np
import pandas as pd
import os

###############################################################
# def plot2circles
def plot_two_circles(center1, radius1, center2, radius2, ax, color="k", alpha=0.1):
    circle1 = plt.Circle(center1, radius1, fill=False, edgecolor=color, linestyle='-', linewidth=1, alpha=alpha)
    circle2 = plt.Circle(center2, radius2, fill=False, edgecolor=color, linestyle='-', linewidth=1, alpha=alpha)
    ax.add_patch(circle1)
    ax.add_patch(circle2)
    ax.scatter(center1[0], center1[1], s=1, c=color)  # 'bo' is blue color with 'o' marker
    ax.scatter(center2[0], center2[1], s=1, c=color)  # 'ro' is red color with 'o' marker
    #ax.plot([center1[0], center2[0]], [center1[1], center2[1]], 'b--')  # 'k--' is black dashed line
    ax.annotate('', xy=(center2[0], center2[1]), xytext=(center1[0], center1[1]),
            arrowprops=dict(arrowstyle="->", lw=1, color=color))
    #ax.set_xlim(min_x - 1, max_x + 1)
    #ax.set_ylim(min_y - 1, max_y + 1)
###############################################################

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
filename0 = "./particleID_sizes.csv"
filenamex = "./ref_points.csv"
filenameg = "./particleID_groups.csv"
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
dataframe0 = pd.read_csv(filename0)
dataframeg = pd.read_csv(filenameg)

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
dataframe0.index = dataframe0["particleID"].astype(np.int64)
dataframeg.index = dataframeg["ParticleID"].astype(np.int64)

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
dataframe0 = dataframe0.sort_index()
dataframeg = dataframeg.sort_index()

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
dataframe0 = dataframe0.reindex(full_index)
dataframeg = dataframeg.reindex(full_index)

# Getting data
indices = np.array(full_index)

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

# Grain size and reference points
grain_size = np.array(dataframe0["gravelometer_size"])
ref_points = pd.read_csv(filenamex)
ref_points_x = ref_points["Easting Coordinates (X)"]
ref_points_y = ref_points["Northing Coordinates (Y)"]
ref_points_labels = np.array(ref_points["Reference Point #"])

# Assigning grain colors
bin_colors = ["thistle", "pink", "deepskyblue", "gold", "limegreen", "magenta", "red", "darkorange"]
grain_colors = np.ones_like(indices)*7
grain_colors[grain_size < 128] = 6
grain_colors[grain_size < 90] = 5
grain_colors[grain_size < 64] = 4
grain_colors[grain_size < 45] = 3
grain_colors[grain_size < 32] = 2
grain_colors[grain_size < 22.6] = 1
grain_colors[grain_size < 16] = 0

#################### PLOT :D
#for j in range(len(dates)-1):
group = "up1"
j = 4
x_min = np.nanmin((location_x[dataframeg["group"] == group, j], location_x[dataframeg["group"] == group, j + 1]))
x_max = np.nanmax((location_x[dataframeg["group"] == group, j], location_x[dataframeg["group"] == group, j + 1]))
y_min = np.nanmin((location_y[dataframeg["group"] == group, j], location_y[dataframeg["group"] == group, j + 1]))
y_max = np.nanmax((location_y[dataframeg["group"] == group, j], location_y[dataframeg["group"] == group, j + 1]))
fig, ax = plt.subplots()
for i in range(len(indices)):
    index = indices[i]
    loc1 = np.array([location_x[i,j], location_y[i,j]])
    loc2 = np.array([location_x[i,j+1], location_y[i,j+1]])
    rad1 = radius[i,j]
    rad2 = radius[i,j+1]
    color1 = bin_colors[grain_colors[i]]
    group1 = dataframeg["group"][i]
    distance = math.dist(loc2, loc1)
    if (distance - grain_size[i]/1000) > (rad1 + rad2) and group1 == group:
        plot_two_circles(loc1, rad1, loc2, rad2, ax, color=color1)
        ax.annotate(f'{i}', (loc1[0], loc1[1]), textcoords="offset points", xytext=(0,8), ha='center', color=color1)
legend_labels = np.unique(grain_size)[0:-1].astype(int).astype(str)
for color, label in zip(bin_colors, legend_labels):
    ax.plot([], [], color=color, label=label, marker="o")
for x, y, text in zip(ref_points_x, ref_points_y, ref_points_labels):
    ax.scatter(x, y, marker="D", c="black", s=3)  # Plot the point
    ax.annotate(f'{text}', (x, y), textcoords="offset points", xytext=(0,8), ha='center')
ax.set_xlim(x_min, x_max)
ax.set_ylim(y_min, y_max)
ax.legend(title="Grain size (mm)")
ax.set_aspect('equal', 'box')
plt.xlabel("Easting (m)")
plt.ylabel("Northing (m)")
plt.title("Particle displacement.\nGroup "+str(group))
plt.grid(True)
plt.show()

group = "up1"
j = 3
x_min = np.nanmin((location_x[dataframeg["group"] == group, j], location_x[dataframeg["group"] == group, j + 1]))
x_max = np.nanmax((location_x[dataframeg["group"] == group, j], location_x[dataframeg["group"] == group, j + 1]))
y_min = np.nanmin((location_y[dataframeg["group"] == group, j], location_y[dataframeg["group"] == group, j + 1]))
y_max = np.nanmax((location_y[dataframeg["group"] == group, j], location_y[dataframeg["group"] == group, j + 1]))

fig, (ax1, ax2) = plt.subplots(1, 2)
for i in range(len(indices)):
    index = indices[i]
    loc1 = np.array([location_x[i,j], location_y[i,j]])
    rad1 = radius[i,j]
    color1 = bin_colors[grain_colors[i]]
    group1 = dataframeg["group"][i]
    if group1 == group:
        plot_two_circles(loc1, rad1, loc1, rad1, ax1, color=color1)
        ax1.annotate(f'{i}', (loc1[0], loc1[1]), textcoords="offset points", xytext=(0,8), ha='center', color=color1)
for i in range(len(indices)):
    index = indices[i]
    loc2 = np.array([location_x[i,j+1], location_y[i,j+1]])
    rad2 = radius[i,j+1]
    color1 = bin_colors[grain_colors[i]]
    group1 = dataframeg["group"][i]
    if group1 == group:
        plot_two_circles(loc2, rad2, loc2, rad2, ax2, color=color1)
        ax2.annotate(f'{i}', (loc2[0], loc2[1]), textcoords="offset points", xytext=(0,8), ha='center', color=color1)
legend_labels = np.unique(grain_size)[0:-1].astype(int).astype(str)
for color, label in zip(bin_colors, legend_labels):
    ax1.plot([], [], color=color, label=label, marker="o")
    ax2.plot([], [], color=color, label=label, marker="o")
ax1.legend(title="Grain size (mm)")
ax1.set_aspect('equal', 'box')
ax2.legend(title="Grain size (mm)")
ax2.set_aspect('equal', 'box')
ax1.set_title("Location 1")
ax1.set_xlabel("Easting (m)")
ax1.set_ylabel("Northing (m)")
ax1.set_xlim(x_min, x_max)
ax1.set_ylim(y_min, y_max)
ax2.set_title("Location 2")
ax2.set_xlabel("Easting (m)")
ax2.set_ylabel("Northing (m)")
ax2.set_xlim(x_min, x_max)
ax2.set_ylim(y_min, y_max)
plt.tight_layout()
plt.title("Particle displacement.\nGroup "+str(group))
#plt.grid(True)
plt.show()

# for x, y, text in zip(ref_points_x, ref_points_y, ref_points_labels):
#     ax.scatter(x, y, marker="D", c="black", s=3)  # Plot the point
#     ax.annotate(f'{text}', (x, y), textcoords="offset points", xytext=(0,8), ha='center')

group = "up2"
x_min = np.nanmin((location_x[dataframeg["group"] == group, :]))
x_max = np.nanmax((location_x[dataframeg["group"] == group, :]))
y_min = np.nanmin((location_y[dataframeg["group"] == group, :]))
y_max = np.nanmax((location_y[dataframeg["group"] == group, :]))
fig, ax = plt.subplots()
for j in range(len(dates)-1):
    for i in range(len(indices)):
        index = indices[i]
        loc1 = np.array([location_x[i,j], location_y[i,j]])
        loc2 = np.array([location_x[i,j+1], location_y[i,j+1]])
        rad1 = radius[i,j]
        rad2 = radius[i,j+1]
        color1 = bin_colors[grain_colors[i]]
        group1 = dataframeg["group"][i]
        distance = math.dist(loc2, loc1)
        if (distance - grain_size[i]/1000) > (rad1 + rad2) and group1 == group:
            plot_two_circles(loc1, rad1, loc2, rad2, ax, color=color1)
            ax.annotate(f'{i}', (loc1[0], loc1[1]), textcoords="offset points", xytext=(0,8), ha='center', color=color1)
legend_labels = np.unique(grain_size)[0:-1].astype(int).astype(str)
for color, label in zip(bin_colors, legend_labels):
    ax.plot([], [], color=color, label=label, marker="o")
# for x, y, text in zip(ref_points_x, ref_points_y, ref_points_labels):
#     ax.scatter(x, y, marker="D", c="black", s=3)  # Plot the point
#     ax.annotate(f'{text}', (x, y), textcoords="offset points", xytext=(0,8), ha='center')
ax.set_xlim(x_min, x_max)
ax.set_ylim(y_min, y_max)
ax.legend(title="Grain size (mm)")
ax.set_aspect('equal', 'box')
plt.xlabel("Easting (m)")
plt.ylabel("Northing (m)")
plt.title("Particle displacement.\nGroup "+str(group))
plt.grid(True)
plt.show()