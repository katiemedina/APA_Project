### Initial Analysis of Bus Rapid Transit Locations in Boston, MA

#### Summary

This analysis completes the initial stages of identifying which existing MBTA bus route could benefit from bus rapid transit interventions in Greater Boston. To identify potential areas, this analysis looks at existing routes that currently have low levels of reliability but high levels of ridership. It then conducts a preliminary spatial analysis of the location of the identified routes. The goal is to identify bus routes that the Massachusetts Bay Transit Authority (MBTA) should further examine for BRT interventions.

#### Input Data

There are two input data files for this analysis, both of which come from the MBTA's open data portal. The first is **MBTA Commuter Rail, Bus, & Rapid Transit Reliability** data which can be accessed here: https://mbta-massdot.opendata.arcgis.com/datasets/mbta-commuter-rail-bus-rapid-transit-reliability. This dataset contains the basis of the MBTA's reliability metric, separated as the on time percentage numerator and denominator.

The second is **MBTA Bus Ridership by Trip, Season, Route/Line, and Stop** which can be accessed here: https://mbta-massdot.opendata.arcgis.com/datasets/mbta-bus-ridership-by-trip-season-route-line-and-stop. This dataset contains the typical number of boardings per bus route in each direction in a given season.

#### Data Processing

Instructions for processing the datasets can be found in:
- Processing Bus Reliability Data with the code in bus_reliability_2018.py
- Processing Bus Ridership Data with the code in bus_ridership.py

#### Maps

Data collection and processing for the maps can be found in collect_tract_hhincome.py and collect_tract_population.py.
