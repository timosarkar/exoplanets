from astroquery.mast import Catalogs
import requests

tic_id = 25155310
tic = Catalogs.query_object(f"TIC {tic_id}", catalog="TIC")
ra = tic[0]['ra']
dec = tic[0]['dec']

print(f"TIC {tic_id}: RA={ra}, Dec={dec}")
file = f"TIC{tic_id}_tess_sector96_5x5_tpf.fits"

url = (f"https://mast.stsci.edu/tesscut/api/v0.1/astrocut?ra={ra}&dec={dec}&x=5&y=5&units=px&product=SPOC&sector=96")

response = requests.get(url)
with open(file, "wb") as f:
    f.write(response.content)

print(f"Saved TPF to ./{file}")
