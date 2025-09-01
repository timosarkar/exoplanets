from astroquery.mast import Catalogs, Tesscut
from astropy.coordinates import SkyCoord
import astropy.units as u
import requests, zipfile, io, os

# --- Step 1: Resolve TIC to coordinates ---
tic_id = input("Input your TIC <ID>: ")
tic = Catalogs.query_object(f"TIC {tic_id}", catalog="TIC")
ra, dec = tic[0]['ra'], tic[0]['dec']
coord = SkyCoord(ra=ra*u.deg, dec=dec*u.deg)

print(f"TIC {tic_id}: RA={ra}, Dec={dec}")

# --- Step 2: Find available sectors ---
sectors = Tesscut.get_sectors(coordinates=coord)
if len(sectors) == 0:
    raise ValueError(f"No TESS sectors found for TIC {tic_id}")
sector = sectors["sector"].max()  # pick latest available sector
print(f"Using sector {sector}")

# --- Step 3: Build Tesscut URL ---
url = (
    f"https://mast.stsci.edu/tesscut/api/v0.1/astrocut?"
    f"ra={ra}&dec={dec}&x=5&y=5&units=px&product=SPOC&sector={sector}"
)

# --- Step 4: Download and extract FITS from ZIP ---
response = requests.get(url)
response.raise_for_status()
with zipfile.ZipFile(io.BytesIO(response.content)) as z:
    fits_filename = z.namelist()[0]
    output_file = f"TIC{tic_id}_sector{sector}_5x5_tpf.fits"
    z.extract(fits_filename, path=".")
    os.rename(fits_filename, output_file)

print(f"Saved TPF to ./{output_file}")

