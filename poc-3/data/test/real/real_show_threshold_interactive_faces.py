import matplotlib.pyplot as plt
import numpy as np
import pyvista as pv


sst = pv.read("pdata_sst_t0.vtk")
cmap = "coolwarm"  # colorcet (perceptually accurate) color maps

p = pv.BackgroundPlotter()
actor = p.add_mesh_threshold(sst, scalars="faces", invert=True, title="SST / K", show_edges=True, cmap=cmap)
p.add_text("C48 SST (cell threshold)", font_size=10, shadow=True, font="courier")

p.show_axes()
p.scalar_bar.SetTitle("SST / K")
p.camera_position = "yz"

