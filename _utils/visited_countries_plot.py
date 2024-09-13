import geopandas as gpd
import matplotlib.pyplot as plt

# Path to your local shapefile
# Downloaded from: https://www.naturalearthdata.com/downloads/10m-cultural-vectors/10m-admin-0-countries/
shapefile_path = "./ne_10m_admin_0_countries/ne_10m_admin_0_countries.shp"

# Load the local shapefile
world = gpd.read_file(shapefile_path)

visited_countries = [
    "CAN",
    "USA",
    "MEX",
    "GTM",
    "BRA",
    "DOM",
    "GBR",
    "FRA",
    "ESP",
    "MCO",
    "ITA",
    "DEU",
    "CZE",
    "AUS",
    "NZL",
    "KOR",
    "THA",
    "VNM",
    "TUR",
    "GRC",
    "VAT",
]

# Create a new column 'visited' to mark visited countries
world["visited"] = world["ADM0_A3"].apply(
    lambda x: "Visited" if x in visited_countries else "Not Visited"
)

# Plot the map
fig, ax = plt.subplots(1, 1, figsize=(15, 10))
world.boundary.plot(ax=ax, linewidth=1, color="black")  # Country borders
world[world["visited"] == "Visited"].plot(
    ax=ax, color="lightblue", legend=True
)  # Shade visited countries

# Add title
ax.set_title("Countries I've Visited", fontsize=16)

# Save the map as a PNG file
plt.savefig(
    "../assets/images/2024-09-05-countries-i-ve-travelled-to/visited_countries.png",
    bbox_inches="tight",
    dpi=300,
)
