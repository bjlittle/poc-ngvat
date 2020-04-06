import matplotlib.pyplot as plt
import numpy as np
import pyvista as pv


def draw():
    global t
    global sst
    global ugrid_sst
    global p
    global N_panels

    for p in range(N_panels):
        sst[p].cell_arrays["faces"] = ugrid_sst[t][p].get_array("faces")
    t = 0 if t == 11 else t + 1


N_panels = 6
N_steps = 12

ugrid_sst = {t: [pv.read(f"ugrid_sst_t{t}_panel{p}.vtk") for p in range(N_panels)] for t in range(N_steps)}

for t in range(N_steps):
    ugrid_sst[t][0].translate((-1, 0, 0))
    ugrid_sst[t][1].translate((0, -1, 0))
    ugrid_sst[t][2].translate((+1, 0, 0))
    ugrid_sst[t][3].translate((0, +1, 0))
    ugrid_sst[t][4].translate((0, 0, -1))
    ugrid_sst[t][5].translate((0, 0, +1))

sst = []
t = 0
for p in range(N_panels):
    sst.append(ugrid_sst[t][p].copy(deep=True))

cmap = "coolwarm"  # colorcet (perceptually accurate) color maps

bp = pv.BackgroundPlotter(shape=(2, 3))

bp.subplot(0, 0)
bp.add_text("C48 Panel 0", font_size=10, shadow=True)
bp.add_text("Equatorial - Europe & Africa", position="lower_left", font_size=8, shadow=True)
bp.add_mesh(sst[0], scalars="faces", show_edges=True, cmap=cmap, show_scalar_bar=False)

bp.subplot(0, 1)
bp.add_text("C48 Panel 4", font_size=10, shadow=True)
bp.add_text("North - Polar", position="lower_left", font_size=8, shadow=True)
bp.add_mesh(sst[4], scalars="faces", show_edges=True, cmap=cmap, show_scalar_bar=False)

bp.subplot(0, 2)
bp.add_text("C48 Panel 1", font_size=10, shadow=True)
bp.add_text("Equatorial - Asia & West Australia", position="lower_left", font_size=8, shadow=True)
bp.add_mesh(sst[1], scalars="faces", show_edges=True, cmap=cmap, show_scalar_bar=False)

bp.subplot(1, 0)
bp.add_text("C48 Panel 2", font_size=10, shadow=True)
bp.add_text("Equatorial - East Australia", position="lower_left", font_size=8, shadow=True)
bp.add_mesh(sst[2], scalars="faces", show_edges=True, cmap=cmap, show_scalar_bar=False)

bp.subplot(1, 1)
bp.add_text("C48 Panel 5", font_size=10, shadow=True)
bp.add_text("South - Antarctica", position="lower_left", font_size=8, shadow=True)
bp.add_mesh(sst[5], scalars="faces", show_edges=True, cmap=cmap, show_scalar_bar=False)

bp.subplot(1, 2)
bp.add_text("C48 Panel 3", font_size=10, shadow=True)
bp.add_text("Equatorial - Americas", position="lower_left", font_size=8, shadow=True)
bp.add_mesh(sst[3], scalars="faces", show_edges=True, cmap=cmap, show_scalar_bar=False)

bp.show_axes_all()
bp.link_views()
bp.add_callback(draw, interval=100)
bp.camera_position = "yz"
