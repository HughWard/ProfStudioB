import geoplot as gplt
import geopandas as gpd
from geopandas_view import view
import geoplot.crs as gcrs
import imageio
import pandas as pd
import pathlib
import matplotlib.pyplot as plt
import mapclassify as mc
import numpy as np

postcode_raw = pd.read_csv('australian_postcodes.csv')
postcode_locality = postcode_raw[['postcode', 'locality', 'state']]
is_nsw = postcode_locality['state'] == 'NSW'
postcodes = postcode_locality[is_nsw]

scores = pd.read_excel("education_occupation_score.xlsx")
print(scores)

localities = gpd.read_file("shape_data/nsw_localities.shp")
print(localities)
for ind, val in localities.iteritems():
    print(ind)
localities['LOC_NAME'] = localities['LOC_NAME'].str.upper()

localities = localities.rename(columns={'LOC_NAME': 'locality'})

combined = pd.merge(localities, postcodes, left_on='locality', right_on='locality')
print(combined)
combined = pd.merge(combined, scores, left_on='postcode', right_on='postcode')

print(combined)
plot = combined.explore(column='Score',cmap='Set2')
view(combined)