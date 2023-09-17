"""
Circle Markers with Radius Dependent Coloring
=============================================

This example shows how to draw circle with the color of the circle scaling with
the radius of the circle

"""
#%%
# Create a signal

import hyperspy.api as hs
import matplotlib.pyplot as plt
import numpy as np

# Create a Signal2D with 2 navigation dimensions
rng = np.random.default_rng(0)
s = hs.signals.Signal2D(np.ones((25, 100, 100)))

#%%
# This first example shows how to draw arrows

# Define the size of the circles
sizes = rng.random((10, )) * 10 + 20

# Define the position of the circles
offsets = rng.random((10, 2)) * 100

m = hs.plot.markers.Circles(
    sizes=sizes,
    offsets=offsets,
    linewidth=2,
    )

s.plot()
s.add_marker(m)

# Set the color of the circles
m.collection.set_array(sizes.ravel() / 2)

# Add corresponding colorbar
cbar = plt.colorbar(m.collection)
cbar.set_label('Circle radius')

# Set animated state of colorbar to support blitting
animated = plt.gcf().canvas.supports_blit
cbar.ax.yaxis.set_animated(animated)
cbar.solids.set_animated(animated)

#%%
# sphinx_gallery_thumbnail_number = 2
