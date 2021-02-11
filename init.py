import pandas as pd
pd.set_option('display.max_columns', 500)
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
import datetime
from datetime import date, timedelta
import matplotlib
from matplotlib.lines import Line2D
from matplotlib.patches import Patch
import matplotlib.cm as cm

params = {
    'font.family': 'serif',
    'font.size' : 16, 'axes.titlesize' : 16, 'axes.labelsize' : 16, 'axes.linewidth' : 2,
    # ticks
    'xtick.labelsize' : 16, 'ytick.labelsize' : 16, 'xtick.major.size' : 8, 'xtick.minor.size' : 4,
    'ytick.major.size' : 8, 'ytick.minor.size' : 4, 'xtick.major.width' : 1, 'xtick.minor.width' : 1,
    'ytick.major.width' : 1, 'ytick.minor.width' : 1, 'xtick.direction' : 'in', 'ytick.direction' : 'in',
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
    'axes.facecolor': 'white'   # axes background color
}
plt.rcParams.update(params)

from matplotlib import rcParams
rcParams['font.family'] = 'sans-serif'
rcParams['font.sans-serif'] = 'PF Din Text Cond Pro'
#rcParams['font.sans-serif'] = 'Exo-2'
rcParams['font.size'] = 20
rcParams['font.weight'] = '500'
rcParams['axes.labelsize'] = 20
rcParams['axes.labelweight'] = '700'
rcParams['axes.titleweight'] = '700'
rcParams['axes.titlesize'] = 22
rcParams['xtick.labelsize'] = 20
rcParams['ytick.labelsize'] = 20
rcParams['legend.fontsize'] = 20
rcParams['figure.titlesize'] = 24

today = datetime.datetime.now()
print('Current time:', today)