# WORKS: get a list of stars that might contain exoplanets transiting the star thats easy to detect
from astroquery.mast import Catalogs

tic_candidates = Catalogs.query_criteria(
    catalog="TIC",
    objType="STAR",
    Tmag=[9, 11],      # brightness
    Teff=[2800, 3600], # temperature
    rad=[None, 0.5],   # radius
)


# around 1570 stars
for row in tic_candidates:
    print(row['ID'])

