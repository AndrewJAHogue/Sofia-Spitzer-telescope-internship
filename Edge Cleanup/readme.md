This branch deals with masking the edges of the sofia data.

hdu[1] = variance map (not quite sure what to do with the variance map, but it was in my notes so I wrote it down)
hdu[2] = exposure times

mask the edges with exposure times, where if exposure time is < n*t_max where n is some scalar less than 1 and t_max is the max exposure time for most of the map (0.4~0.45).

In the final processed maps, the edges of the sofia data become exasperated.
To clean up the final maps, the edges must be masked before any processessing is done, to make things easier.

There is a variance point and exposure time for every data point in the image.
Go through and check the exposure times for each data point, following the aforementioned rules, and set the edges to np.nans