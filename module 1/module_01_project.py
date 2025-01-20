import pandas as pd
import matplotlib.pyplot as plt
import squarify


url = "https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2021/2021-05-25/records.csv"
df_mario = pd.read_csv(url)


# track time bar chart
track_time = (
    df_mario.loc[lambda x: (x.type == "Three Lap") & (x.shortcut == "No")]
    .groupby("track")
    .time.min()
    .sort_values(ascending=True)
    .reset_index()
)

fig, ax = plt.subplots()

ax.barh(y=track_time["track"], width=track_time["time"])
ax.set_title("Shortest complete race time without shortcuts")
ax.set_xlabel("Time in seconds")
ax.set_ylabel("Track")

fig.tight_layout()

fig.savefig("shortest_complete_track_time.png")
plt.show()


# loli pop chart
# shortest lap time with or without short cuts

track_time = (
    df_mario.loc[lambda x: (x.type == "Three Lap")]
    .groupby(["track", "shortcut"])
    .time.min()
    .sort_values(ascending=True)
    .unstack()
    .dropna()
    .reset_index()
    .sort_values(by="No")
)


fig, ax = plt.subplots(figsize=(10, 10))

ax.hlines(
    y=track_time.track,
    xmin=track_time["Yes"],
    xmax=track_time["No"],
    color="grey",
    alpha=0.4,
)

# points
ax.scatter(
    track_time["Yes"], track_time.track, zorder=2, color="red", label="With shortcuts"
)
ax.scatter(
    track_time["No"],
    track_time.track,
    zorder=2,
    color="green",
    label="Without shortcuts",
)

ax.set_title("Difference in shortest race time shortcuts vs noshortcuts")
ax.set_xlabel("Time in seconds")
ax.set_ylabel("Track")

ax.legend(loc=4)
fig.tight_layout()

fig.savefig("shortest_complete_track_time_with_or_without_shortcuts.png")
plt.show()

# time series

# calculate time series
rainbow_road_overtime = (
    df_mario.loc[
        lambda x: (x.track == "Rainbow Road")
        & (x.shortcut == "No")
        & (x.type == "Three Lap")
    ]
    .assign(data=lambda x: pd.to_datetime(x.date))
    .sort_values(by="date")
)


fig, ax = plt.subplots()


ax.set_title("Evolution of shortest full track time without shortcuts rainbow road")
ax.plot(rainbow_road_overtime.date, rainbow_road_overtime.time)

ax.tick_params(axis="x", labelrotation=90)
ax.set_xlabel("Date")
ax.set_ylabel("Time in seconds")
ax.set_ylim(0, 400)

fig.tight_layout()
fig.savefig("Evolution of shortest full track time without shortcuts rainbow road")
plt.show()



# Tree map distribution of records per player players

records_per_player = (
    df_mario.groupby("player")
    .track.count()
    .sort_values()
    .reset_index()
    .loc[lambda x: x.track > 20]
)


fig, ax = plt.subplots(figsize=(15, 10))


ax.set_axis_off()
squarify.plot(
    sizes=records_per_player["track"],
    label=records_per_player["player"]
    + "\n records: "
    + records_per_player["track"].astype(str),
    text_kwargs={"color": "white"},
    pad=True,
    ax=ax,
)
ax.set_title("Players with more than 20 records")
fig.tight_layout()
fig.savefig("Players with more than 20 records")
plt.show()


# record duration boxplot
# pirate plot?

fig, ax = plt.subplots()


violins = ax.violinplot(
    # [
    #     df_mario[df_mario["track"] == category]["record_duration"]
    #     for category in df_mario["track"].unique()
    # ]
    df_mario.record_duration
)


ax.set_xticks([])

ax.set_ylabel("Record duration in days")
ax.set_title("Distribution of record duration")
fig.tight_layout()

fig.savefig("distribution of record duration violin plot")
plt.show()


# histogram

fig, ax = plt.subplots()

ax.hist(df_mario.record_duration, bins=200)
ax.set_title("Distribution of record duration")
ax.set_ylabel("Record duration in days")
fig.tight_layout()
fig.savefig("distribution of record duration histogram")
plt.show()

## piechart different systems

systems_played = df_mario.system_played.value_counts().reset_index()

fig, ax = plt.subplots()

ax.pie(systems_played["count"], labels=systems_played.system_played)
ax.set_title("Proportion of records by system played")
fig.savefig("Proportion of records by system played.png")
ax.axis("equal")

plt.show()
