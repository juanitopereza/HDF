import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import h5py
#%%
with h5py.File("MYD04_3K.A2015006.1900.061.2018046042234.h5", "r") as hdf:
    items = list(hdf.items())
    datos = hdf.get(u'mod04')
    datos_items = datos.items()
    print(datos_items[0])
    GL_fields = hdf.get("/mod04/Geolocation Fields")
    longs = np.array(GL_fields.get(u'Longitude'))
    lats = np.array(GL_fields.get(u'Latitude'))
    print(GL_fields.items())
#%%
longs.shape
lats.shape
#%%
plt.scatter(longs, lats)
plt.show()
