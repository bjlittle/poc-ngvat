import matplotlib.pyplot as plt
import numpy as np
import pyvista as pv


sst = pv.read("pdata_xy_sst_t0.vtk")

cmap = "fire"  # colorcet (perceptually accurate) color maps
sargs = dict(
             shadow=True,
             n_labels=5,
             italic=False,
             fmt="%.1f",
             font_family="courier",
#             nan_annotation=True,
             vertical=True,
)

p = pv.BackgroundPlotter()
#p.add_mesh(sst, scalars="faces", show_edges=True, cmap=cmap, show_scalar_bar=True)
p.add_mesh_threshold(sst, scalars="lats", invert=True, title="latitude", cmap=cmap, show_edges=True, show_scalar_bar=True, scalar_bar_args=sargs)
p.add_text("C48 Latitude Threshold", font_size=10, shadow=True, font="courier")

p.show_axes()
#p.show_grid()
p.scalar_bar.SetTitle("Latitude")
#p.add_scalar_bar(**sargs)
p.camera_position = "yz"

