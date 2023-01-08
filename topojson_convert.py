import topojson
import pandas as pd

# Read in geojson file
with open("counties.geojson", "r") as f:
    geojson = f.read()

# Convert geojson to topojson
topo = topojson.Topology(geojson)

# Read in dataframe
county_data = pd.read_csv("county_data.csv")

# Merge data from dataframe into topojson object
for county in topo["objects"]["counties"]["geometries"]:
    county_name = county["properties"]["name"]
    county_pop = county_data[county_data["county"] == county_name]["population"].values[0]
    county["properties"]["population"] = county_pop

# Save topojson object to file
with open("counties_pop.topojson", "w") as f:
    f.write(topo.to_json())