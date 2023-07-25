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
- [ ] Add the extra geometrical parameters to previous surveys (will add more info on this later) - *Korvin*

## Notes: 
- For triangulation, we will be using AutpCAD Civil 3D (you can get it for free using your student email). Steps are specified further below.
- The tracerCAD file where all the reference points can be found in the repo

## Triangulation Steps
#### This is what needs to be done for each tracer in order to obtain its coordinates: 

1. Click on reference point and write command "circle" - Enter
2. Select the center of the circle (the reference point)
3. Write down the radius (in METERS) - Enter

Repeat process for the other two reference points

4. Write command "PL" (PLINE)
5. Create a triangle with the three vertices being each circle intersection
7. Write command "Region"
8. Select the triangle - Enter
10. Write command "MASSPROP" 
11. Select the triangle - Enter
12. Copy and paste the centroid coordinates

On the spreadsheet: 

11. Past the coordinates
- X: Goes in the EASTING column
- Y: Goes in the NORTHING column

## Appendix: 
Table 1. Coordinates of each marked reference point used during the triangulation process. (Needs to be updated)
| Referemce Point #  | Easting Coordinates (X)  | Northing Coordinates (Y) |
| :----------------: | :----------------------: | :----------------------: |




