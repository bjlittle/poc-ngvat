import matplotlib.pyplot as plt
import numpy as np
import pyvista as pv


def draw():
    global t
    global sst
    global pdata_sst
    global sst_cube
    global ugrid_sst_cube
    global p

    sst.cell_arrays["faces"] = pdata_sst[t].get_array("faces")
    sst_cube.cell_arrays["faces"] = ugrid_sst_cube[t].get_array("faces")
    t = 0 if t == 11 else t + 1


N_steps = 12
    
pdata_sst = {t: pv.read(f"pdata_sst_t{t}.vtk").threshold() for t in range(N_steps)}
sst = pv.read("pdata_sst_t0.vtk").threshold()

ugrid_sst_cube = {t: pv.read(f"ugrid_cube_sst_t{t}.vtk").threshold() for t in range(N_steps)}
sst_cube = pv.read("ugrid_cube_sst_t0.vtk").threshold()

t = 0
cmap = "coolwarm"  # colorcet (perceptually accurate) color maps

p = pv.BackgroundPlotter(shape=(1, 2))

p.subplot(0, 0)
p.add_text("C48 SST time-series (cube-sphere)", font_size=10, shadow=True, font="courier")
p.add_mesh(sst, scalars="faces", show_edges=True, cmap=cmap, show_scalar_bar=False)

p.subplot(0, 1)
p.add_text("C48 SST time-series (cube)", font_size=10, shadow=True, font="courier")
p.add_mesh(sst_cube, scalars="faces", show_edges=True, cmap=cmap, show_scalar_bar=True, scalar_bar_args=dict(nan_annotation=True))
p.scalar_bar.SetTitle("SST / K")

p.show_axes_all()
p.link_views()
p.add_callback(draw, interval=200)
p.camera_position = "yz"
