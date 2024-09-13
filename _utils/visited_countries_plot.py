import os
import random

import geopandas as gpd
import matplotlib.pyplot as plt
import seaborn as sns

# Path to your local shapefile
shapefile_path = "./ne_10m_admin_0_countries/ne_10m_admin_0_countries.shp"

# Load the local shapefile
world = gpd.read_file(shapefile_path)

# List of visited countries (ISO 3166-1 alpha-3 country codes)
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

# Create a unique color for each visited country
# Get a seaborn palette with enough colors for the visited countries
palette = sns.color_palette("Set2", len(visited_countries))

# Assign each visited country a color from the palette
visited_colors = {country: palette[i] for i, country in enumerate(visited_countries)}

# Create a new column to assign colors to visited countries
world["color"] = world["ADM0_A3"].apply(
    lambda x: visited_colors.get(x, "#fafafa")
)  # Default non-visited countries to gray

# Plot the map
fig, ax = plt.subplots(1, 1, figsize=(15, 10))

# Plot country borders
world.boundary.plot(ax=ax, linewidth=1, color="black")

# Plot visited countries with their assigned colors
world.plot(ax=ax, color=world["color"], edgecolor="black", legend=True)

# Add title
ax.set_title("Countries I've Visited", fontsize=16)
ax.axis("off")

output_image_path = (
    "assets/images/2024-09-05-countries-i-ve-travelled-to/visited_countries.png"
)
# Save the map as a PNG file
plt.savefig(
    os.path.join("../", output_image_path),
    bbox_inches="tight",
    dpi=300,
)

import pycountry


def country_info_from_code(country_code_alpha3):
    """
    Converts an ISO alpha-3 country code to its corresponding flag emoji and country name.

    :param country_code_alpha3: ISO alpha-3 country code (e.g., "USA" for United States)
    :return: A tuple containing the flag emoji and the country name, or (None, None) if the country code is not valid
    """
    try:
        # Get the country object using alpha-3 code
        country = pycountry.countries.get(alpha_3=country_code_alpha3)

        # Convert the alpha-2 code to the flag emoji and get the country name
        if country:
            alpha2_code = country.alpha_2
            flag_emoji = chr(ord(alpha2_code[0]) + 127397) + chr(
                ord(alpha2_code[1]) + 127397
            )
            country_name = country.name
            return flag_emoji, country_name
        else:
            return None, None
    except KeyError:
        return None, None


country_info = [country_info_from_code(x) for x in visited_countries]

emoji_output = ""
for i in range(len(country_info)):
    e, n = country_info[i]
    emoji_output += f"## {e} {n}\n"

# Now create the markdown content
markdown_content = f"""---
title: "Countries I've Travelled To"
tags:
  - Adventures
header:
  teaser: /{output_image_path}
  og_image: /{output_image_path}
toc: true
toc_sticky: true
---

![PIC](/{output_image_path})

{emoji_output}

This is how I created the above graphic:

```python
# Path to your local shapefile
# Downloaded from: https://www.naturalearthdata.com/downloads/10m-cultural-vectors/10m-admin-0-countries/
shapefile_path = "./ne_10m_admin_0_countries/ne_10m_admin_0_countries.shp"

# Load the local shapefile
world = gpd.read_file(shapefile_path)

visited_countries = [
    "CAN", "USA", "MEX", "GTM", "BRA", "DOM", "GBR", "FRA", "ESP", "MCO",
    "ITA", "DEU", "CZE", "AUS", "NZL", "KOR", "THA", "VNM", "TUR", "GRC", "VAT"
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
ax.axis("off")

# Save the map as a PNG file
plt.savefig(
    "../assets/images/2024-09-05-countries-i-ve-travelled-to/visited_countries.png",
    bbox_inches="tight",
    dpi=300,
)
```
"""

with open("../_posts/2024-09-05-countries-i-ve-travelled-to.md", "w") as file:
    file.write(markdown_content)
