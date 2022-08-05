# %%
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from ipywidgets import SliderStyle, interact

# %%
# df_898 = pd.read_csv("../hyperopt_898.csv")
# df_898.head()

# %%
def plot(a):
    x = np.linspace(0, 100, 1000)
    y = a * x
    plt.plot(x, y)
    plt.ylim(0, 1000)
    plt.xlim(0, 100)
    plt.show()


# %%
interact(plot, a=(1, 5))

# %%
