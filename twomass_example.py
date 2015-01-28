from moastro.twomass import PSC
from astropy.io import fits


psc = PSC(server='marvin')

stars = psc.find({"j_m-k_m": {"$gt": 0.9}},
                 fields=["coord", "j_m", "k_m"],
                 center=(13., 41.),
                 radius=2.)


stars = psc.find({"j_m-k_m": {"$gt": 0.9}},
                 fields=["coord", "j_m", "k_m"],
                 header=fits.getheader(fits_path, 0))
