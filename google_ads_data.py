#%%

import pandas as pd
import json
import matplotlib.pyplot as plt


dataset = pd.read_csv("all_political_ads_germany.csv")
# %%
print(dataset["advertiser_legal_name"].value_counts())
print(dataset.columns)

#remove unused columns
dataset= dataset["creative_page_url",'ad_format_type',
       'advertiser_disclosed_name','advertiser_location', 'region_stats',
       'audience_selection_approach_info', 'topic']
#%%

for e in dataset["audience_selection_approach_info"]:
    print(e)
    print(json.loads(e))
    print("________________________________\n")


foo = pd.DataFrame([json.loads(e)["audience_selection_approach_info"] for e in dataset["audience_selection_approach_info"]])
foo



# %%

print(dataset["advertiser_legal_name"].value_counts().to_string())

pd.concat([dataset, foo], axis=1)
# %%
