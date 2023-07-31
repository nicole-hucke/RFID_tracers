# RFID tracer particles - La Jara Creek #
#### This repo is where we store all the RFID tracer data during the summer 2023 field season ####
<img src="https://cdn.discordapp.com/attachments/696204356650926092/1128012453360435272/fe3dcdee-4847-463b-8237-37354e3496a1.png" alt="Alt Text" width="600" height="250">

## Things to do: 
- [x] Add the last tracer survey from last spring (2023) - *Nicole*
- [x] Add the first tracer survey from this summer - *Nicole*
- [x] Identify and quantify how many particles were lost/burried/not found during the summer - *Nicole* 
      
      Once we both add the csv listings of both surveys, we need to know what particle ID's were lost
      We then will look into what size class they correspond to and see how many of what size class were lost
      It would also be useful to quantify the percentage of the total amount and each size class difference as well
      This should be done by each patch of particles

- [x] Measure the B axis of the retrieved rocks from the site (separate by each size class) - *Korvin*

      We don't have a gravelometer, so will have to do by hand. Take 3 measurements and average them out
      
- [x] Get colored spray paint, acrylic and a brush (at metzgers I guess?) and paint each particle with it's respective size class - *Korvin and Nicole*
- [x] Will paint on new ID's and add them to the list of tracers - *Nicole*
- [x] Add these to the stream and record their locations - *Korvin and Nicole*

#### Once all these are done and we have a bit more down time, these are the following tasks:
- [ ] Triangulate all particles from this summer survey - *Korvin and Nicole*
      
      This is the list of surveys (in chronological order):
      1. 03/28/22
      2. 07/06/22
      3. 08/06/22
      4. 08/09/22
      5. 08/24/22
      6. 03/24/23
      7. 06/17/23
     
- [ ] Add the extra geometrical parameters to previous surveys - *Korvin*

      These new parameters are:
      - Heights of the triangle we calculate the centroid for
      - Depending on how the circles intersect, we also want the dimensions of A, B and C (see image below).
      - The composite error for these should be expressed as the following:

# $\sqrt[3]{a^2+b^2+c^2}$

Here is an example of different cases you will encounter when triangulating: 

<img src="https://cdn.discordapp.com/attachments/696204356650926092/1135697238044184716/image.png" alt="Alt Text" width="800" height="550">

## Triangulation Steps
#### This is what needs to be done for each tracer in order to obtain its coordinates and geometric properties: 

1. Click on reference point and write command "circle" - Enter
2. Select the center of the circle (the reference point)
3. Write down the radius (in METERS) - Enter

Repeat process for the other two reference points

4. Write command "PL" (PLINE)
5. Create a triangle with the three vertices being each circle intersection
6. Write command "Region"
7. Select the triangle - Enter
8. Write command "MASSPROP" 
9. Select the triangle - Enter
10. Copy and paste the centroid coordinates
11. Paste the coordinates on the spreadsheet:
- X: Goes in the EASTING column
- Y: Goes in the NORTHING column
12. Copy and paste the Area and Perimeter of the triangle on the spreadsheet

#### For Triangle heights: 
1. Write command line and select a vertice
2. Right click and snap "perpendicular"
3. There is a little green icon where the angle is perpendicular on the adjacent leg of the triangle. Line should be placed there. 
4. Select the line and view it's properties. There you should be able to see the length (in meters)
5. If you do not see the green icon after the perpendicular snap, it means your height is outside the triangle. 
    For this, you must do command "lengthen" and make the triangle leg longer. Repeat step 3 and 4 when icon appears.

## Notes: 
- For triangulation, we will be using AutpCAD Civil 3D (you can get it for free using your student email and creating an AutoDesk account). 
- The tracerCAD file where all the reference points can be found in the repository.
- For the geometric parameters (A, B and C) you can just create lines and write down their lengths (by looking at the properties tab). 

## Appendix: 
Table 1. Coordinates of each marked reference point used during the triangulation process.
| Reference Point #  | Easting Coordinates (X)  | Northing Coordinates (Y) |
| :----------------: | :----------------------: | :----------------------: |
|         1          |        475287.725        |        539899.896        |
|         2          |        475288.527        |        539899.682        |
|         3          |        475288.898        |        539899.235        |
|         4          |        475290.192        |        539899.113        |
|         5          |        475292.210        |        539900.157        |
|         6          |        475291.970        |        539901.968        |
|         7          |        475292.783        |        539901.734        |
|         8          |        475292.993        |        539901.185        |
|         10         |        475292.771        |        539903.950        |
|         11         |        475293.945        |        539903.572        |
|         12         |        475294.397        |        539903.999        |
|         13         |        475294.997        |        539903.589        |
|         14         |        475229.425        |        539952.654        |
|         15         |        475231.508        |        539951.970        |
|         16         |        475231.721        |        539954.740        |
|         17         |        475233.636        |        539954.306        |
|         18         |        475235.383        |        539956.440        |
|         19         |        475235.780        |        539957.610        |
|         20         |        475234.816        |        539959.693        |
|         21         |        475236.501        |        539958.827        |
|         22         |        475236.686        |        539960.687        |
|         23         |        475235.559        |        539962.693        |
|         24         |        475238.078        |        539964.461        |
|         26         |        475239.084        |        539966.237        |
|         27         |        475239.649        |        539967.106        |
|         28         |        475237.945        |        539968.781        |
|         29         |        475240.373        |        539968.088        |
|         30         |        475238.303        |        539970.257        |
|         31         |        475239.538        |        539970.683        |
