import geopandas as gpd
import matplotlib.pyplot as plt
import pandas as pd

# Load shapefile of Indiana counties
indiana_counties = gpd.read_file("indiana_boundary_uscb_2020_tl_2020_18_state20.shx")

# Load redistricting data
redistricting_data = pd.read_csv("path/to/redistricting_data.csv")

# Merge shapefile with redistricting data
merged_data = indiana_counties.merge(redistricting_data, on="county_id")

# Plot chloropleth map for algorithmic/optimal redistricting
fig, ax = plt.subplots(1, 1)
merged_data.plot(column="congressional_district", cmap="viridis", linewidth=0.5, ax=ax, edgecolor="0.8")
ax.axis("off")
ax.set_title("Algorithmic/Optimal Redistricting")
plt.show()

# Plot chloropleth map for actual redistricting
fig, ax = plt.subplots(1, 1)
merged_data.plot(column="actual_congressional_district", cmap="viridis", linewidth=0.5, ax=ax, edgecolor="0.8")
ax.axis("off")
ax.set_title("Actual Redistricting")
plt.show()
