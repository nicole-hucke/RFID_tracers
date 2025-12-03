
###############################################################
# Importing libraries
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Polygon
import numpy as np

################################################################
# Defining some functions

# Defining a function to know if two circles intersect
def do_they_intersect(x1, y1, r1, x2, y2, r2):
    # Distance between both centers
    distance = np.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    tempBool1 = True
    # Do they intersect?
    if distance > (r1 + r2) or distance < abs(r1 - r2):
        tempBool1 = False
    return tempBool1

# Getting circle intersections
def get_circle_intersection(x1, y1, r1, x2, y2, r2):
    # Distance between both centers
    distance = np.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    a = (r1**2 - r2**2 + distance**2) / (2 * distance)
    h = np.sqrt(r1**2 - a**2)
    x3 = x1 + a * (x2 - x1) / distance
    y3 = y1 + a * (y2 - y1) / distance

    p1_x = x3 + h * (y2 - y1) / distance
    p1_y = y3 - h * (x2 - x1) / distance

    p2_x = x3 - h * (y2 - y1) / distance
    p2_y = y3 + h * (x2 - x1) / distance

    tempCalc1 = np.array([[p1_x, p1_y],
                            [p2_x, p2_y]])
    return tempCalc1

# Getting closest points between two circles
def get_circle_closest(x1, y1, r1, x2, y2, r2):
    # Distance between both centers
    distance = np.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    
    if distance < abs(r1 - r2):  # One circle is inside the other
        if r1 > r2:
            x1, y1, r1, x2, y2, r2 = x2, y2, r2, x1, y1, r1  # Ensure r1 is the smaller circle
        
        # Point on the circumference of the smaller circle
        x_inner = x1 - r1 * (x2 - x1) / distance
        x_outer = x2 - r2 * (x2 - x1) / distance
    
        y_inner = y1 - r1 * (y2 - y1) / distance
        y_outer = y2 - r2 * (y2 - y1) / distance
    
        tempCalc1 = np.array([[x_inner, y_inner],
                            [x_outer, y_outer]])
        return tempCalc1
    else:
        a1 = r1 / distance
        a2 = r2 / distance

        p1_x = x1 + a1 * (x2 - x1)
        p1_y = y1 + a1 * (y2 - y1)
        p2_x = x2 - a2 * (x2 - x1)
        p2_y = y2 - a2 * (y2 - y1)

        tempCalc1 = np.array([[p1_x, p1_y],
                            [p2_x, p2_y]])
    return tempCalc1

# Function to build a polygon
def get_polygon(rep_points12, rep_points13, rep_points23, intersect_bool12, intersect_bool13, intersect_bool23):
    # Calculating distances between representative points
    p1a_to_p2a = np.sqrt((rep_points12[0,0] - rep_points13[0,0])**2 + (rep_points12[0,1] - rep_points13[0,1])**2)
    p1a_to_p2b = np.sqrt((rep_points12[0,0] - rep_points13[1,0])**2 + (rep_points12[0,1] - rep_points13[1,1])**2)
    p1b_to_p2a = np.sqrt((rep_points12[1,0] - rep_points13[0,0])**2 + (rep_points12[1,1] - rep_points13[0,1])**2)
    p1b_to_p2b = np.sqrt((rep_points12[1,0] - rep_points13[1,0])**2 + (rep_points12[1,1] - rep_points13[1,1])**2)

    p1a_to_p3a = np.sqrt((rep_points12[0,0] - rep_points23[0,0])**2 + (rep_points12[0,1] - rep_points23[0,1])**2)
    p1a_to_p3b = np.sqrt((rep_points12[0,0] - rep_points23[1,0])**2 + (rep_points12[0,1] - rep_points23[1,1])**2)
    p1b_to_p3a = np.sqrt((rep_points12[1,0] - rep_points23[0,0])**2 + (rep_points12[1,1] - rep_points23[0,1])**2)
    p1b_to_p3b = np.sqrt((rep_points12[1,0] - rep_points23[1,0])**2 + (rep_points12[1,1] - rep_points23[1,1])**2)

    p2a_to_p3a = np.sqrt((rep_points13[0,0] - rep_points23[0,0])**2 + (rep_points13[0,1] - rep_points23[0,1])**2)
    p2a_to_p3b = np.sqrt((rep_points13[0,0] - rep_points23[1,0])**2 + (rep_points13[0,1] - rep_points23[1,1])**2)
    p2b_to_p3a = np.sqrt((rep_points13[1,0] - rep_points23[0,0])**2 + (rep_points13[1,1] - rep_points23[0,1])**2)
    p2b_to_p3b = np.sqrt((rep_points13[1,0] - rep_points23[1,0])**2 + (rep_points13[1,1] - rep_points23[1,1])**2)
    
    # Deciding which of the two points is closer to the group of points
    polygon = np.zeros((3,2))
    polygon[0] = rep_points12[0]
    polygon[1] = rep_points13[0]
    polygon[2] = rep_points23[0]

    tempCalc1 = p1a_to_p2a + p1a_to_p2b + p1a_to_p3a + p1a_to_p3b
    tempCalc2 = p1b_to_p2a + p1b_to_p2b + p1b_to_p3a + p1b_to_p3b
    tempCalc3 = p1a_to_p2a + p1b_to_p2a + p2a_to_p3a + p2a_to_p3b
    tempCalc4 = p1a_to_p2b + p1b_to_p2b + p2b_to_p3a + p2b_to_p3b
    tempCalc5 = p1a_to_p3a + p1b_to_p3a + p2a_to_p3a + p2b_to_p3a
    tempCalc6 = p1a_to_p3b + p1b_to_p3b + p2a_to_p3b + p2b_to_p3b

    # Choosing the point that is closer to the group
    if tempCalc1 > tempCalc2:
        polygon[0] = rep_points12[1]
    if tempCalc3 > tempCalc4:
        polygon[1] = rep_points13[1]
    if tempCalc5 > tempCalc6:
        polygon[2] = rep_points23[1]

    # If circles do not intersect, choose the middle point between both rep points
    if intersect_bool12 == False:
        polygon[0] = np.mean(rep_points12, axis=0)
    if intersect_bool13 == False:
        polygon[1] = np.mean(rep_points13, axis=0)
    if intersect_bool23 == False:
        polygon[2] = np.mean(rep_points23, axis=0)
    
    return polygon

# Function to plot circles
def plot_circle(ax, x, y, r, label):
    circle = plt.Circle((x, y), r, fill=False, label=label)
    ax.add_patch(circle)
    ax.plot(x, y, 'yo')  # Plot center
    ax.annotate(label, (x, y), textcoords="offset points", xytext=(10,10), ha='center')
def plot3circles(centers, radii, rep_points=None, polygon=None, CM=None, confidence=None):
    labels = ["Ref 1", "Ref 2", "Ref 3"]
    fig, ax = plt.subplots()
    ax.set_aspect('equal', 'box')
    for (x, y), r, label in zip(centers, radii, labels):
        plot_circle(ax, x, y, r, label)
    cols = ["red", "green", "blue"]
    if isinstance(rep_points, list):
        for i in range(3):
            ax.scatter(rep_points[i][:,0], rep_points[i][:,1], color=cols[i])
    if isinstance(polygon, np.ndarray):
        polygon_fig = Polygon(polygon, closed=True, edgecolor="purple", fill=None)
        ax.add_patch(polygon_fig)
    if isinstance(CM, np.ndarray):
        ax.scatter(CM[0], CM[1], color="gold", marker="x")
    if confidence != None:
        filled_circle = Circle((CM[0], CM[1]), confidence, edgecolor="gold", linestyle='--', 
                        facecolor="none", alpha=0.5, linewidth=2)
        ax.add_patch(filled_circle)
    #plt.legend()
    plt.grid(True)
    plt.title("Reference points and rock position")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.show()

# Defining the big function
def get_rock_coordinates(ref_points, ref_to_rock):
    # Checking if circles intersect
    intersect_bool12 = do_they_intersect(ref_points[0,0], ref_points[0,1], ref_to_rock[0], 
                                        ref_points[1,0], ref_points[1,1], ref_to_rock[1])
    intersect_bool13 = do_they_intersect(ref_points[0,0], ref_points[0,1], ref_to_rock[0],
                                        ref_points[2,0], ref_points[2,1], ref_to_rock[2])
    intersect_bool23 = do_they_intersect(ref_points[1,0], ref_points[1,1], ref_to_rock[1],
                                        ref_points[2,0], ref_points[2,1], ref_to_rock[2])
    
    # Getting the representative points for each pair of circles
    if intersect_bool12 == True:
        rep_points12 = get_circle_intersection(ref_points[0,0], ref_points[0,1], ref_to_rock[0],
                                            ref_points[1,0], ref_points[1,1], ref_to_rock[1])
    else:
        rep_points12 = get_circle_closest(ref_points[0,0], ref_points[0,1], ref_to_rock[0],
                                        ref_points[1,0], ref_points[1,1], ref_to_rock[1])
    if intersect_bool13 == True:
        rep_points13 = get_circle_intersection(ref_points[0,0], ref_points[0,1], ref_to_rock[0],
                                            ref_points[2,0], ref_points[2,1], ref_to_rock[2])
    else:
        rep_points13 = get_circle_closest(ref_points[0,0], ref_points[0,1], ref_to_rock[0],
                                        ref_points[2,0], ref_points[2,1], ref_to_rock[2])
    if intersect_bool23 == True:
        rep_points23 = get_circle_intersection(ref_points[1,0], ref_points[1,1], ref_to_rock[1],
                                            ref_points[2,0], ref_points[2,1], ref_to_rock[2])
    else:
        rep_points23 = get_circle_closest(ref_points[1,0], ref_points[1,1], ref_to_rock[1],
                                        ref_points[2,0], ref_points[2,1], ref_to_rock[2])
    rep_points = [rep_points12, rep_points13, rep_points23]

    # Getting the polygon defined by the most representative points
    polygon = get_polygon(rep_points12, rep_points13, rep_points23, intersect_bool12, intersect_bool13, intersect_bool23)
    CM = np.mean(polygon, axis=0)

    # Getting the confidence radius for the measurements
    tempCalc1 = np.sqrt((polygon[0][0] - CM[0])**2 + (polygon[0][1] - CM[1])**2)
    tempCalc2 = np.sqrt((polygon[1][0] - CM[0])**2 + (polygon[1][1] - CM[1])**2)
    tempCalc3 = np.sqrt((polygon[2][0] - CM[0])**2 + (polygon[2][1] - CM[1])**2)
    confidence_radius = np.max((tempCalc1, tempCalc2, tempCalc3))

    return CM, rep_points, confidence_radius, polygon

#################################################################
# Performing the analysis

####### GOOD EXAMPLE #######
# Defining xyz coordinates fo the reference points
ref_points = np.array([[475291.97, 539901.968], # 6
                        [475292.783, 539901.734], # 7
                        [475292.771, 539903.95]]) # 10
# Distances from reference points to rock X
ref_to_rock = np.array([2.3,
                        1.65,
                        1.92]) # 105
# Estimating rock position
CM, rep_points, confidence_radius, polygon = get_rock_coordinates(ref_points, ref_to_rock)
plot3circles(ref_points, ref_to_rock, rep_points=rep_points, polygon=polygon, CM=CM, confidence=confidence_radius)
print("Rock position: ", CM)

####### BAD EXAMPLE - NO INTERSECTION #######
# Defining xyz coordinates fo the reference points
ref_points = np.array([[475234.816, 539959.693], # 20
                        [475236.501, 539958.827], # 21
                        [475236.686, 539960.687]]) # 22
# Distances from reference points to rock X
ref_to_rock = np.array([0.75,
                        1.49,
                        1.35]) # 2
# Estimating rock position
CM, rep_points, confidence_radius, polygon = get_rock_coordinates(ref_points, ref_to_rock)
plot3circles(ref_points, ref_to_rock, rep_points=rep_points, polygon=polygon, CM=CM, confidence=confidence_radius)
print("Rock position: ", CM)