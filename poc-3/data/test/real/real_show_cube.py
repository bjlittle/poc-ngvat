import matplotlib.pyplot as plt
import numpy as np
import pyvista as pv


def draw():
    global t
    global actor
    global sst
    global ugrid_sst
    global p

    if actor is None:
        actor = p.add_text(f"C48 time-series", font_size=10)

    sst.cell_arrays["faces"] = ugrid_sst[t].get_array("faces")
    t = 0 if t == 11 else t + 1


ugrid_sst = {t: pv.read(f"ugrid_cube_sst_t{t}.vtk") for t in range(12)}
sst = pv.read("ugrid_cube_sst_t0.vtk")
sst.set_active_scalars("faces")
t = 0
actor = None

cmap = "coolwarm"  # colorcet (perceptually accurate) color maps

sargs = dict(
#             interactive=True,
#             title_font_size=8,
#             label_font_size=6,
             shadow=True,
             n_labels=5,
             italic=False,
             fmt="%.1f",
             font_family="arial",
             nan_annotation=True,
             vertical=True,
)

p = pv.BackgroundPlotter()
p.add_mesh(sst, scalars="faces", show_edges=True, cmap=cmap, scalar_bar_args=sargs)
#p.add_scalar_bar("hello", **sargs, cmap=cmap)
p.show_axes()
#p.show_grid()
p.scalar_bar.SetTitle("sst / K")
#p.add_scalar_bar(**sargs)
p.add_callback(draw, interval=100)
