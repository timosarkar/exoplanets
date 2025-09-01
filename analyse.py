import lightkurve as lk
import matplotlib.pyplot as plt

tpf = lk.TessTargetPixelFile("./TIC25155310_sector96_5x5_tpf.fits")
lc = tpf.to_lightcurve().remove_nans().normalize()
lc.plot()
plt.show()
