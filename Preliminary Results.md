### Results

The preliminary results of this analysis were generated with **figures.py** and **Routes and Census Tract Earnings.png**.

#### Building the figures

1. Import pandas, matplotlib.pyplot, and seaborn.

2. Read in the csv file that was created by bus_ridership.py.

3. Create a new dataframe with only the columns used to build the figures: `gtfs_route_id`, `pct_reliable`, `boardings`, and `route_indicator`.

4. Use seaborn barplot to graph the reliability and ridership for each bus line. Remember to sort values by `pct_reliable` to more easily read the graph. Save the figure as 'Reliability and Boardings by Route'.

5. Use plot to graph reliability and ridership on the same graph. This will help identify those routes that overlap in these key areas. Save the figure as 'ReliabilityxBoardings'.

#### Building the map

1. Using QGIS, build a base map of the state of MA and its census tracts.

2. Using the **collect_tract_earnings.py** script, collect and process census tract level earning data and add it to the map. Use a graduated color scheme to show the different levels of earnings in Greater Boston.

3. Using shapefiles from MassGIS data (https://docs.digital.mass.gov/dataset/massgis-data-mbta-bus-routes-and-stops) add the bus routes to map.

4. Join the bad_buses.csv generated earlier to the bus routes map and filter the MassGIS file to just the buses we are investigating.

#### Visual Analysis

The visual analysis of these two figures shows that there is a significant difference in both reliability between the worst performing bus routes and the key bus routes. The worst performing regular route (the 434) was on time half as often as the worst performing key bus route (the 116). However, the ridership figure shows that these non-key bus routes also have very low ridership.

The ReliabilityxBoardings figure shows where ridership and reliability overlap. As expected, the 434 was at the lowest end of the list with ridership that is barely detectable on the graph. On the other end of the axis, some of the best performing lines (the 71 and 73) have relatively low ridership. The lines where ridership appears to be exceeding reliability are the 1, 66, and 28.

Filtering the map to just show the 71, 73, 1, 66, and 28 buses, we see that the 71 and 73 buses essentially share a route and run through relatively higher-income census tracts. The 1, 66, and 28, however, run through relatively lower-income census tracts. The 28 appears to be a feeder bus to the 66, also from lower-income areas.

#### Recommendations

Based on this initial analysis, the MBTA should look into the 1, 66, and 28 for further investigation. All three routes have high levels of ridership and low levels of reliability. They also run through lower-income areas where residents are less likely to own or have access to a private vehicle.

Further analysis is required to refine these results. First, street-level congestion data should be used to determine whether there are specific areas of each route that are more likely to cause delays. The 1 and the 66 run along Mass. Ave., a major thoroughfare and source of congestion during peak hours. Second, directional data should be incorporated to consider implementing variable-bus only lanes. It is likely that the majority of ridership flows in one direction in the morning and the opposite in the evening. In this case, a variable-direction bus only lane might be an appropriate solution.
