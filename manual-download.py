# WORKS: download lightcurves and targetpixelfiles manually from a given TESS candidace TIC
from astroquery.mast import Observations
obs_table = Observations.query_object("TIC 25155310", radius="0.02 deg")
products = Observations.get_product_list(obs_table)
tpfs = Observations.filter_products(products, productType="SCIENCE", extension="fits")

# works:
# *_lc.fits: lightcurves
# *_tp.fits: target pixel files
# *_dvt.fits: irrelevant
for row in tpfs:
    print(row['dataURI'])


"""

tpfs = [
    'mast:TESS/product/tess2024353092137-s0087-0000000025155310-0284-s_tp.fits',
    'mast:TESS/product/tess2025014115807-s0088-0000000025155310-0285-s_tp.fits',
    'mast:TESS/product/tess2025071122000-s0090-0000000025155310-0287-s_tp.fits',
    'mast:TESS/product/tess2025154050500-s0093-0000000025155310-0290-s_tp.fits',
    'mast:TESS/product/tess2025180145000-s0094-0000000025155310-0291-s_tp.fits'
]

# Download each TPF
for uri in tpfs:
    print(f"Downloading {uri} ...")
    Observations.download_file(uri)
"""
