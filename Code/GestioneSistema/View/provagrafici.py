import matplotlib.pyplot as plt
import numpy as np

import matplotlib as mpl


fig, ax = plt.subplots(figsize=(5, 2.7), layout='constrained')
categories = ['turnips', 'rutabaga', 'cucumber', 'pumpkins']
valori = [1, 10, 100, 50]

ax.bar(categories, valori)
plt.show()