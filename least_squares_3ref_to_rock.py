
###############################################################
# Importing libraries
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.optimize import least_squares

# xyz coordinates of reference points
reference_points = np.array([
    [475287.725, 539899.896, 0], # 1
    [475288.527, 539899.682, 0], # 2
    [475288.898, 539899.235, 0], # 3
    [475290.192, 539899.113, 0], # 4 
    [475292.210, 539900.157, 0], # 5
    [475291.970, 539901.968, 0], # 6
    [475292.783, 539901.734, 0], # 7
    [475292.993, 539901.185, 0], # 8
    [475292.771, 539903.950, 0], # 10
    [475293.945, 539903.572, 0], # 11
    [475294.397, 539903.999, 0], # 12
    [475294.997, 539903.589, 0], # 13
    [475229.425, 539952.654, 0], # 14
    [475231.508, 539951.970, 0], # 15
    [475231.721, 539954.740, 0], # 16
    [475233.636, 539954.306, 0], # 17
    [475235.383, 539956.440, 0], # 18
    [475235.780, 539957.610, 0], # 19
    [475234.816, 539959.693, 0], # 20
    [475236.501, 539958.827, 0], # 21
    [475236.686, 539960.687, 0], # 22
    [475235.559, 539962.693, 0], # 23
    [475238.078, 539964.461, 0], # 24
    [475239.084, 539966.237, 0], # 25
    [475239.649, 539967.106, 0], # 26
    [475237.945, 539968.781, 0], # 27
    [475240.373, 539968.088, 0], # 28
    [475238.303, 539970.257, 0], # 29
    [475239.538, 539970.683, 0], # 30
    ]) 

def trilaterate(p1, p2, p3, r1, r2, r3):
    # need to define an error function that calculates the difference between
    # the measured distances and the distances from an estimated position
    def error_func(pos, p1, p2, p3, r1, r2, r3):
        return [
            np.linalg.norm(pos - p1) - r1,  # Difference for the first point
            np.linalg.norm(pos - p2) - r2,  # Difference for the second point
            np.linalg.norm(pos - p3) - r3   # Difference for the third point
        ]
    # initial guess for the position: the centroid of the three reference points
    initial_guess = np.mean([p1, p2, p3], axis=0)
    # use least squares optimization to minimize the error function
    result = least_squares(error_func, initial_guess, args=(p1, p2, p3, r1, r2, r3))
    # return the optimized position
    return result.x

survey = pd.read_csv('tracer_surveys.csv')  
# prepare to store the results
results = []

for idx, row in survey.iterrows():
    particle_id = row['ParticleID'] # extract the particle ID for the current row
    ref_idx_a, ref_idx_b, ref_idx_c = row['Ref1'], row['Ref2'], row['Ref3'] # extract the indices of the reference points for the current particle  
    r1, r2, r3 = row['Dist1'], row['Dist2'], row['Dist3'] # extract the distances from the particle to each of the reference points
    
    # get the (x, y) coordinates of each reference point from the reference_points array
    # subtract 1 from the indices since Python arrays are zero-indexed
    p1 = reference_points[ref_idx_a - 1][:2]
    p2 = reference_points[ref_idx_b - 1][:2]
    p3 = reference_points[ref_idx_c - 1][:2]
    # use the trilateration function to calculate the (x, y) coordinates of the particle
    x, y = trilaterate(p1, p2, p3, r1, r2, r3)
    # append the particle ID and its calculated coordinates to the results list
    results.append((particle_id, x, y))

# convert the results list to a DataFrame
results_df = pd.DataFrame(results, columns=['ParticleID', 'X', 'Y'])

# plotting stuff
plt.figure(figsize=(8, 6))
unique_ids = results_df['ParticleID'].unique()
colors = plt.cm.viridis(np.linspace(0, 1, len(unique_ids)))  # Generate colors for each unique particle ID

for i, pid in enumerate(unique_ids):
    data_pid = results_df[results_df['ParticleID'] == pid]
    plt.scatter(data_pid['X'], data_pid['Y'], label=f'Particle {pid}', color=colors[i], alpha=0.8)
    for x, y, id in zip(data_pid['X'], data_pid['Y'], data_pid['ParticleID']):
        plt.text(x, y, str(id), fontsize=8, ha='center', va='bottom')

plt.xlabel('X-coordinate')
plt.ylabel('Y-coordinate')
plt.title('Trilateration Results')
plt.legend()
plt.grid(True)
plt.show()