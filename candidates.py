# WORKS: get a list of stars that might contain exoplanets transiting the star thats easy to detect
from astroquery.mast import Catalogs

# Query TIC for bright, small, cool stars
tic_candidates = Catalogs.query_criteria(
    catalog='TIC',
    Tmag=[None, 12],
    Teff=[None, 4000],
    rad=[None, 0.7],
    objType='STAR'
)

# Print top 5 TIC IDs
for row in tic_candidates[:5]:
    print(row['ID'], row['Tmag'], row['Teff'], row['rad'])
