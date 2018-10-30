import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import h5py
import os
#%%
#dirs = np.array([x[1] for x in os.walk('.')])

# dirs = next(os.walk('.'))[1]
# dirs
# for dir in dirs:
#     dirs1 = next(os.walk('./'+dir))[1]
#     for dir1 in dirs1:
#         archs = [x for x in os.listdir('./'+dir+'./'+dir1) if x.endswith('.h5')]
#         data = np.zeros((len(archs), 203, 135))
#         for ar in archs:
#             with h5py.File('./'+dir+'./'+dir1+'./'+ar, "r") as hdf:
#                 items = list(hdf.items())
#                 datos = hdf.get(u'mod04')
#                 datos_items = datos.items()
#                 print(datos_items)
#                 GL_fields = hdf.get("/mod04/Geolocation Fields")
#                 longs = np.array(GL_fields.get(u'Longitude'))
#                 lats = np.array(GL_fields.get(u'Latitude'))
#                 print(GL_fields.items())

with h5py.File(".\2012\001\MYD04_L2.A2012001.1755.061.2018036234841.h5", "r") as hdf:
    items = list(hdf.items())
    datos = hdf.get(u'mod04')
    datos_items = datos.items()
    print(datos_items)
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
