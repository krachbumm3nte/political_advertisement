# %%

import pandas as pd
import json
import matplotlib.pyplot as plt


# dataset = pd.read_csv("google_political_ads_germany_2024_02_15.csv")
dataset = pd.read_csv("google_political_ads_2024_02_15.csv")
# %%
print(dataset["advertiser_legal_name"].value_counts())
print(dataset.columns)

# remove unused columns
dataset = dataset[
    [
        "creative_page_url",
        "ad_format_type",
        "advertiser_disclosed_name",
        "advertiser_location",
        "region_stats",
        "audience_selection_approach_info",
        "topic",
    ]
]
# %%
# integrate json-stringified columns into the df

col = "audience_selection_approach_info"
print(col)
df_temp = pd.DataFrame([json.loads(e)[col] for e in dataset[col]])
dataset = pd.concat([dataset, df_temp], axis=1)
dataset = dataset.drop(columns=col)

# %%

col = "region_stats"
print(col)
region_ar = []
for e in dataset[col]:
    foo = json.loads(e)[col]
    first_shown = [bar["first_shown"] for bar in foo]
    for bar in foo:
        print(bar["first_shown"], bar["region_code"])
    print(len(foo), len(set(first_shown)))
    print("---------------------------------\n\n")
df_temp = pd.DataFrame(region_ar)

# %%
dataset = pd.concat([dataset, df_temp], axis=1)
dataset = dataset.drop(columns=col)

# %%
