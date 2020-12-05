#!/usr/bin/env python
# coding: utf-8

# In[335]:
#/************************************************************************************************/
#/*** Topic: Binary_Heatmap_network                                                            ***/
#/***                                                                         Ali-Seif         ***/
#/*** Version Release 17.12 rev 11256                                                          ***/
#/*** Date: 12/5/2020                                                                          ***/
#/*** Code implemented in CodeBlocks C++ compiler (v. 17.12),                                  ***/
#/*** MSI: PX60 6QD/ DDR4                                                                      ***/
#/*** Run under a Intel® Core™ i7-6700HQ CPU @ 2.60GHz × 64 based processor with 16 GB RAM     ***/
#/************************************************************************************************/

import igraph as ig
import plotly.graph_objects as go
import json
with open("bineryprint.txt") as textFile:
    lines = [line.split() for line in textFile]
N=len(lines[0])
a=[]
for x in range(1, N+1):
    a=a+["A"+str(x)] 
layout = go.Layout(
    
         title="Erdos-Renyi network 40 nodes and connection probability 0.4 (Binary Heatmap)" ,
         width=600,
         height=600,
         showlegend=False,
    hovermode='closest',
        font=dict(
            size=10
            ),
    annotations=[
           dict(
           showarrow=False,
               
 text="Data source: <a href='https://github.com/aliseif321/Binary_Heatmap_network'>[1] https://github.com/aliseif321/Binary_Heatmap_network</a>",            xref='paper',
            yref='paper',
            x=-0.1,
            y=-0.18,
            xanchor='left',
            yanchor='bottom',
            font=dict(
            size=15
            )
            )
        
        ],    )    
    
    
    
fig = go.Figure(data=go.Heatmap(
                   z=lines,
                   x=a,
                   y=a),layout=layout)


fig.show()
fig.write_html("file.html")


# In[ ]:





# In[ ]:




