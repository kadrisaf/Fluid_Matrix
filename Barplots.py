#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 24 17:33:24 2021

@author: safwen
"""

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns
import requests
import matplotlib.font_manager as font_manager

sns.set()

import pandas as pd
import xlsxwriter
dt1= pd.read_excel("/home/safwen/Documents/Fish_data_Feb_2019/Annotated data/Gills/pathfindR_Results(1)/Gills_path.xlsx", index_col=None) 
dt2= pd.read_excel("/home/safwen/Documents/Fish_data_Feb_2019/Annotated data/Liver/pathfindR_Results/Liver_path.xlsx", index_col=None) 

result=pd.merge(dt2,dt1, on='ID', how='left', sort=False)
result.to_excel("Path intersection.xlsx")  

os.chdir("/home/safwen/Documents/Fish_data_Feb_2019/Intersection graphs")
dt1= pd.read_excel("/home/safwen/Documents/Fish_data_Feb_2019/Intersection graphs/Pathways_graph.xlsx", index_col=0) 
dt4= ['BP enrichement','Liver','Gills']


font_color = '#525252'
hfont = {'fontname':'Calibri'}
facecolor = '#eaeaf2'
color_red = '#fd625e'
color_blue = '#01b8aa'
index = dt1.index
column0 = dt1['Liver']
column1 = dt1['Gill']
title0 = 'Liver'
title1 = 'Gill'

fig, axes = plt.subplots(figsize=(20,5), facecolor=facecolor, ncols=2, sharey=True)

fig.tight_layout()



axes[0].barh(index, column0, align='center', color=color_red, zorder=10)
axes[0].set_title(title0, fontsize=18, pad=15, color=color_red, **hfont)
axes[1].barh(index, column1, align='center', color=color_blue, zorder=10)
axes[1].set_title(title1, fontsize=18, pad=15, color=color_blue, **hfont)

axes[0].invert_xaxis() 

# To show data from highest to lowest
plt.gca().invert_yaxis()

axes[0].set(yticks=dt1.index, yticklabels=dt1.index)
axes[0].yaxis.tick_left()
axes[0].tick_params(axis='y', colors='white') # tick color

for label in (axes[0].get_xticklabels() + axes[0].get_yticklabels()):
    label.set(fontsize=8, color=font_color, **hfont)
for label in (axes[1].get_xticklabels() + axes[1].get_yticklabels()):
    label.set(fontsize=8, color=font_color, **hfont)

plt.subplots_adjust(wspace=0, top=0.85, bottom=0.1, left=0.18, right=0.95)
fig.set_size_inches(20.5, 10.5)



filename = 'Pathway'
plt.savefig(filename+'.png', facecolor=facecolor)

