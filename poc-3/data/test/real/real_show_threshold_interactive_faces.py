import matplotlib.pyplot as plt
import numpy as np
import pyvista as pv


sst = pv.read("pdata_xy_sst_t0.vtk")

cmap = "coolwarm"  # colorcet (perceptually accurate) color maps
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
actor = p.add_mesh_threshold(sst, scalars="faces", invert=True, title="SST / K", show_edges=True, cmap=cmap, scalar_bar_args=sargs, show_scalar_bar=True)
p.add_text("C48 Sea Surface Temperature", font_size=10, shadow=True, font="courier")

p.show_axes()
#p.show_grid()
p.scalar_bar.SetTitle("sst / K")
#p.add_scalar_bar(**sargs)
p.camera_position = "yz"

