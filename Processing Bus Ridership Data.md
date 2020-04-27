### Processing Bus Ridership Data

1. Import pandas and zipfile.

2. Download the 'MBTA Bus Ridership by Trip, Season, Routeline, and Stop' from https://mbta-massdot.opendata.arcgis.com/datasets/mbta-bus-ridership-by-trip-season-route-line-and-stop and import as csv. Call the dataframe `rides.`

3. Import the `bad_buses.csv`

4. Bus ridership information is given for a 'typical' day per route within a season. Subset the rides database for `Fall 2018`.

5. Group the data by `route_id` and then sum `boardings`.

6. Merge the `bad_buses` dataframe with the grouped rides database. Use a left merge and merge on route id. Print the `_merge` indicator to confirm that all records matched.

7. Export the merged dataset as a csv called 'rides_and_reliability.csv'
