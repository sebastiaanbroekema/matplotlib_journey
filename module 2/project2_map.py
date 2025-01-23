import matplotlib.pyplot as plt
import pandas as pd
import geopandas as gpd
import contextily as cx
import geodatasets

from pypalettes import load_cmap


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
    markersize=5,
)

ax.get_legend().set_title("Price per night ($)")


cx.add_basemap(ax, zoom=13)
ax.axis("off")
ax.set_title("Better Airbnb deals in the north of Manhattan")
plt.tight_layout()


fig.savefig("NY_airbnb_price.png", dpi=500)


# =====

# nyc_neighborhoods
hoods = gpd.read_file(geodatasets.get_path("geoda.nyc_neighborhoods"))


hoods = hoods[["ntaname", "geometry"]]


pie_chart_input = (
    hoods.to_crs(epsg=3857)
    .assign(centroid=lambda x: x.geometry.centroid, geom_left=lambda x: x.geometry)
    .sjoin(gdf, how="right")
    .loc[lambda x: x.neighbourhood_group == "Manhattan"]
    .groupby(["ntaname", "room_type", "centroid","geom_left"])
    .price.count()
    .reset_index()
    .pipe(gpd.GeoDataFrame)
)


cmap = load_cmap('', keep_first_n=3)


fig, ax = plt.subplots()

pie_chart_input.set_geometry("geom_left").plot(color='red', ax=ax)


neighberhoods = pie_chart_input.ntaname.unique()


for hood in neighberhoods:
    hood_data = pie_chart_input.loc[lambda x: x.ntaname == hood].sort_values('room_type')
    label = hood_data.room_type
    values = hood_data.price
    center = (hood_data.centroid.iloc[0].x, hood_data.centroid.iloc[0].y)
# https://stackoverflow.com/questions/56277645/pie-charts-and-geopandas-map
    piecolors = ["tab:purple", "tab:blue", "tab:red"]
    wedges = plt.pie(
        values,
        labels=label,
        colors = piecolors,
        radius= 0.1,)
    for j in range(3):
        print(center)
        ax.scatter([center[0]],[center[1]],marker=(wedges[0][j].get_path().vertices.tolist()),facecolor=piecolors[j], s=800)

plt.show()