import matplotlib.pyplot as plt
import pandas as pd
import geopandas as gpd
import contextily as cx


url = "https://raw.githubusercontent.com/JosephBARBIERDARNAL/data-matplotlib-journey/refs/heads/main/newyork-airbnb/newyork-airbnb.csv"
df = pd.read_csv(url)



gdf = gpd.GeoDataFrame(
    df, geometry=gpd.points_from_xy(df.longitude, df.latitude), crs="EPSG:4326"
).to_crs(epsg=3857)


fig, ax = plt.subplots(figsize=(10, 9))

gdf.loc[lambda x: x.neighbourhood_group == "Manhattan"].plot(
    column="price",
    ax=ax,
    alpha=0.2,
    legend=True,
    scheme="Quantiles",
    classification_kwds={"k": 10},
    categorical=True,
    markersize=5
)

ax.get_legend().set_title("Price per night ($)")


cx.add_basemap(ax, zoom=13)
ax.axis("off")
ax.set_title('Better Airbnb deals in the north of Manhattan')
plt.tight_layout()
# plt.show(block=False)

fig.savefig("NY_airbnb_price.png", dpi=500)
