import pandas as pd
pd.set_option('display.max_columns', 500)
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
import datetime
from datetime import date, timedelta

params = {
    'font.family': 'serif',
    'font.size' : 18, 'axes.titlesize' : 18, 'axes.labelsize' : 18, 'axes.linewidth' : 2,
    # ticks
    'xtick.labelsize' : 18, 'ytick.labelsize' : 18, 'xtick.major.size' : 16, 'xtick.minor.size' : 8,
    'ytick.major.size' : 16, 'ytick.minor.size' : 8, 'xtick.major.width' : 2, 'xtick.minor.width' : 2,
    'ytick.major.width' : 2, 'ytick.minor.width' : 2, 'xtick.direction' : 'in', 'ytick.direction' : 'in',
    # markers
    'lines.markersize' : 12, 'lines.markeredgewidth' : 3, 'errorbar.capsize' : 8, 'lines.linewidth' : 3,
    #'lines.linestyle' : None, 'lines.marker' : None,
    'savefig.bbox' : 'tight', 'legend.fontsize' : 16, 
    'backend': 'Agg', 'mathtext.fontset': 'dejavuserif', 'legend.frameon' : True,
    'figure.facecolor':'w',
    #pad
    'axes.facecolor': 'w',
    'axes.labelpad':12,
    # ticks
    'xtick.major.pad': 6,   'xtick.minor.pad': 6,   
    'ytick.major.pad': 3.5, 'ytick.minor.pad': 3.5,
    # colormap
    #'image.cmap':'viridis'
}
plt.rcParams.update(params)
today = datetime.datetime.now()
print('Current time:', today)