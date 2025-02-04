import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
from umap import UMAP
from sklearn.preprocessing import StandardScaler
from highlight_text import ax_text

from pypalettes import load_cmap

cmap = load_cmap("Alkalay2")
colors = cmap.colors


url_nut = "https://raw.githubusercontent.com/Barabasi-Lab/GroceryDB/refs/heads/main/data/GroceryDB_training_dataset_SRFNDSS_2001_2018_NOVA123_multi_compositions_12Nutrients.csv"
url_food = "https://raw.githubusercontent.com/Barabasi-Lab/GroceryDB/refs/heads/main/data/GroceryDB_foods.csv"

food_nutrients = pd.read_csv(url_nut, index_col=0)
# Index(['Food code', 'Main food description', 'version SR', 'year FNDDS',
#        'novaclass', 'Protein', 'Total Fat', 'Carbohydrate', 'Sugars, total',
#        'Fiber, total dietary', 'Calcium', 'Iron', 'Sodium', 'Vitamin C',
#        'Cholesterol', 'Fatty acids, total saturated', 'Total Vitamin A'],


# FPRO higher is more processed
# https://www.nature.com/articles/s41467-023-37457-1/figures/2
foods = pd.read_csv(url_food, index_col=0)

# ['name', 'store', 'harmonized single category', 'brand', 'f_FPro',
#        'f_FPro_P', 'f_min_FPro', 'f_std_FPro', 'f_FPro_class', 'price',
#        'price percal', 'package_weight', 'has10_nuts',
#        'is_Nuts_Converted_100g', 'Protein', 'Total Fat', 'Carbohydrate',
#        'Sugars, total', 'Fiber, total dietary', 'Calcium', 'Iron', 'Sodium',
#        'Vitamin C', 'Cholesterol', 'Fatty acids, total saturated',
#        'Total Vitamin A'],


reducer = UMAP()

nuts = foods[
    # [
    #     "Protein",
    #     "Total Fat",
    #     "Carbohydrate",
    #     "Sugars, total",
    #     "Fiber, total dietary",
    #     "Calcium",
    #     "Iron",
    #     "Sodium",
    #     "Vitamin C",
    #     "Cholesterol",
    #     "Fatty acids, total saturated",
    #     "Total Vitamin A",
    # ]
    [
        'f_FPro', 'f_min_FPro', 'f_std_FPro', 'f_FPro_class',"Protein",
        # "Total Fat",
        # "Carbohydrate",
        # "Sugars, total",
        # "Fiber, total dietary",
    ]
]


scaled_foods = StandardScaler().fit_transform(nuts.fillna(-1))

embedding = reducer.fit_transform(scaled_foods)
# embedding = reducer.fit_transform(nuts.fillna(-1))


fig, ax = plt.subplots()

ax.scatter(embedding[:, 0], embedding[:, 1], c=foods.f_FPro, cmap=cmap, alpha=0.5, s=5)
ax.set_xlabel("")
ax.set_ylabel("")
ax.set_title("")
ax.axis("off")
plt.show()


text = (
    foods["harmonized single category"]
    .to_frame()
    .assign(
        dim_0=embedding[:, 0],
        dim_1=embedding[:, 1],
    )
    .groupby("harmonized single category")
    .mean()
    .reset_index()
)


fig, ax = plt.subplots()

# ax.scatter(embedding[:, 0], embedding[:, 1], c=foods.f_FPro, cmap=cmap, alpha=0.5, s=5)

c = foods["harmonized single category"].apply(lambda x: colors[0] if x.str.contains('snack') else colors[-1])
ax.scatter(embedding[:, 0], embedding[:, 1], c=c, alpha=0.5, s=5)
ax.axis("off")

# for i,j in text.iterrows():
#     ax_text(j["dim_0"],j["dim_1"], j["harmonized single category"])

plt.show()

# baby-food
# baking
# bread
# breakfast
# cakes
# canned-goods
# cereal
# cheese
# coffee-beans-wf
# cookies-biscuit
# culinary-ingredients
# dairy-yogurt-drink
# dressings
# drink-coffee
# drink-juice
# drink-juice-wf
# drink-shakes-other
# drink-soft-energy-mixes
# drink-tea
# drink-water-wf
# eggs-wf
# ice-cream-dessert
# jerky
# mac-cheese
# meat-packaged
# meat-poultry-wf
# milk-milk-substitute
# muffins-bagels
# nuts-seeds-wf
# pasta-noodles
# pastry-chocolate-candy
# pizza
# prepared-meals-dishes
# produce-beans-wf
# produce-packaged
# pudding-jello
# rice-grains-packaged
# rice-grains-wf
# rolls-buns-wraps
# salad
# sauce-all
# sausage-bacon
# seafood
# seafood-wf
# snacks-bars
# snacks-chips
# snacks-dips-salsa
# snacks-mixes-crackers
# snacks-nuts-seeds
# snacks-popcorn
# soup-stew
# spices-seasoning
# spread-squeeze
