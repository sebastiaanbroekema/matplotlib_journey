import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import geoplot as gplt
import mapclassify as mc
import geoplot.crs as gcrs

df = (
    pd.read_parquet("data/CBSdata3.parquet")
    .groupby("laadPC4gem")
    .zendingAantal.sum()
    .reset_index()
)


pc6 = gpd.read_file("data/cbs_pc6_2023_v1.gpkg")

pc4: gpd.GeoDataFrame
pc4 = (
    pc6[["postcode6", "geometry", "aantal_inwoners"]]
    .assign(
        postcode4=lambda x: x.postcode6.str[:4],
        aantal_inwoners=lambda x: x.aantal_inwoners.replace(-99997, np.nan).astype(
            pd.Int32Dtype()
        ),
    )
    .drop("postcode6", axis=1)
    .dissolve("postcode4", aggfunc="sum")
)

pc4.to_parquet("data/pc4.parquet")


plot_frame = (
    pc4.reset_index()
    .assign(laadPC4gem=lambda x: "PC4" + x.postcode4)
    .merge(df, how="inner", on="laadPC4gem")
    .loc[lambda x: x.geom_type != "MultiPolygon"]
    .to_crs("EPSG:4326")
)
scheme = mc.Quantiles(plot_frame["zendingAantal"], k=5)


# fig, ax = plt.subplots()

ax = gplt.cartogram(
    plot_frame,
    scale="zendingAantal",
    projection=gcrs.WebMercator(),
    limits=(0.5, 1),
    hue="zendingAantal",
    linewidth=0.5,
    legend=True,
    # legend_kwargs={"loc": "lower right"},
    # legend_var="zendingAantal",
)

gplt.polyplot(plot_frame, facecolor="lightgray", edgecolor="k", ax=ax)


plt.show()
