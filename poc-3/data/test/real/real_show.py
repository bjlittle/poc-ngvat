import matplotlib.pyplot as plt
import numpy as np
import pyvista as pv


def event_draw():
    global t
    global sst
    global pdata_sst
    global p

    sst.cell_arrays["faces"] = pdata_sst[t].get_array("faces")
    t = 0 if t == 11 else t + 1


pdata_sst = {t: pv.read(f"pdata_sst_t{t}.vtk") for t in range(12)}
sst = pv.read("pdata_sst_t0.vtk")
sst.set_active_scalars("faces")

t = 0
cmap = "coolwarm"  # colorcet (perceptually accurate) color maps

p = pv.BackgroundPlotter()
p.add_mesh(sst, scalars="faces", show_edges=True, cmap=cmap, scalar_bar_args=dict(nan_annotation=True))
p.add_text(f"C48 SST time-series", font_size=13, shadow=True, font="courier")
p.show_axes()
p.scalar_bar.SetTitle("SST / K")
p.add_callback(event_draw, interval=100)
