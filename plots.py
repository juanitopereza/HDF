import numpy as np
import matplotlib.pyplot as plt
import os
# %%

archs = [x for x in os.listdir('.') if x.endswith('.txt')]
for each in archs:
    datos = np.loadtxt(each)
    plt.imshow(datos)
    #plt.gca().invert_yaxis()
    plt.savefig(each[0:-4]+'.pdf', dpi=300)
