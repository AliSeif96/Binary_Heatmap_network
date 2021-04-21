# Binary_Heatmap_network
Binary Heatmap to connect nodes in the network


[![plotly](https://www.vectorlogo.zone/logos/plot_ly/plot_ly-ar21.svg)](https://plotly.com//)




<p align="center">
 <img src="https://github.com/aliseif321/Binary_Heatmap_network/blob/main/Pictures/Binary%20Heatmap.png?raw=true" >
 </p>

__________________________________

# Binary_Heatmap_network_red_article



```ruby
import numpy as np
import matplotlib.pyplot as plt
b, a = np.meshgrid(np.linspace(25, 1025, 21), np.linspace(5, 505, 51))
with open("asd.txt") as textFile:
    c = [np.float_(line.split()) for line in textFile]

with open("x.txt") as textFile:
    x = [np.float_(line.split()) for line in textFile]    
with open("y.txt") as textFile:
    y = [np.float_(line.split()) for line in textFile]    

l_a=a.min()
r_a=a.max()
l_b=b.min()
r_b=b.max()

l_c,r_c  = np.abs(c).min(), np.abs(c).max()

figure, axes = plt.subplots()

c = axes.pcolormesh(b, a, c, cmap='hot', vmin=l_c, vmax=r_c)

axes.set_title('Heatmap')
axes.set_ylabel('Inter spike intervals')
axes.set_xlabel('Number of neurons')

axes.axis([ l_b, r_b,l_a, r_a])
figure.colorbar(c)

plt.plot(x,y, linewidth=2, color='silver')

#plt.show()

plt.savefig("myplot.png", dpi = 1000)

``` 

<p align="center">
 <img src="https://github.com/aliseif321/Binary_Heatmap_network/blob/main/Heatmap%20red%20article/myplot.png?raw=true" >
 </p>
