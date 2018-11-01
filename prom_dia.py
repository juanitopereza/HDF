import numpy as np
import matplotlib.pyplot as plt
from pyhdf.SD import SD, SDC
import os
#%%
#print(file.info())
# for idx, sds in enumerate(datasest_dic.keys()):
#     print(idx, sds)
# datasest_dic = file.datasets()

dirs = next(os.walk('.'))[1]
data = []
for dir in dirs:
    dirs1 = next(os.walk('./'+dir))[1]
    for dir1 in dirs1:
        archs = [x for x in os.listdir('./'+dir+'./'+dir1) if x.endswith('.hdf')]
        #data = np.zeros((len(archs), 203, 135))
        for ar in archs:
            file = SD('./'+dir+'/'+dir1+'/'+ar, SDC.READ)
            sds_obj = file.select('Optical_Depth_Land_And_Ocean')
            dat = sds_obj.get()
            data.append(dat)
    ODLO = np.array(data)
    ODLO_mean = np.mean(ODLO, axis=0)
    np.savetxt('./'+dir+'/'+'promedio_'+archs[0][10:17]+'.txt', ODLO_mean)

#%%
# plt.imshow(ODLO_mean)
# #plt.gca().invert_yaxis()
# plt.savefig('promedio_001.pdf', dpi=480)
#plt.show()

# plt.imshow(ODLO[0])
# plt.gca().invert_yaxis()
# plt.show()
#
# plt.imshow(ODLO[1])
# plt.gca().invert_yaxis()
# plt.show()
#
# plt.imshow(ODLO[2])
# plt.gca().invert_yaxis()
# plt.show()
