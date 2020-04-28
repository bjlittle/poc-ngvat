import matplotlib.pyplot as plt
import numpy as np
import pyvista as pv


def draw():
    global t
    global sst
    global pdata_sst
    global p
    global N_panels

    for p in range(N_panels):
        sst[p].cell_arrays["faces"] = pdata_sst[t][p].get_array("faces")
    t = 0 if t == 11 else t + 1


N_panels = 6
N_steps = 12

pdata_sst = {t: [pv.read(f"pdata_sst_t{t}_panel{p}.vtk").threshold() for p in range(N_panels)] for t in range(N_steps)}

factor = 1.41425

for t in range(N_steps):
    pdata_sst[t][0].translate((-1, -0.5*factor, 0))
    
    pdata_sst[t][1].translate((0, -1, 0))
    pdata_sst[t][1].rotate_z(-90)
    pdata_sst[t][1].translate((0, 0.5*factor, 0))

    pdata_sst[t][2].translate((+1, 0, 0))
    pdata_sst[t][2].rotate_z(180)
    pdata_sst[t][2].translate((0, 1.5*factor, 0))
    
    pdata_sst[t][3].translate((0, +1, 0))
    pdata_sst[t][3].rotate_z(90)
    pdata_sst[t][3].translate((0, -1.5*factor, 0))
    
    pdata_sst[t][4].translate((0, 0, -1))
    pdata_sst[t][4].rotate_y(90)
    pdata_sst[t][4].translate((0, -0.5*factor, factor))
    
    pdata_sst[t][5].translate((0, 0, 1))
    pdata_sst[t][5].rotate_y(-90)
    pdata_sst[t][5].translate((0, -0.5*factor, -factor))

sst = []
t = 0
for p in range(N_panels):
    sst.append(pdata_sst[t][p].copy(deep=True))

cmap = "coolwarm"  # colorcet (perceptually accurate) color maps

bp = pv.BackgroundPlotter()
show_edges = True

bp.add_text("C48 SST time-series (unfolded)", font_size=10, shadow=True, font="courier")
bp.add_mesh(sst[0], scalars="faces", show_edges=show_edges, cmap=cmap, show_scalar_bar=False)
bp.add_mesh(sst[1], scalars="faces", show_edges=show_edges, cmap=cmap, show_scalar_bar=False)
bp.add_mesh(sst[2], scalars="faces", show_edges=show_edges, cmap=cmap, show_scalar_bar=False)
bp.add_mesh(sst[3], scalars="faces", show_edges=show_edges, cmap=cmap, show_scalar_bar=False)
bp.add_mesh(sst[4], scalars="faces", show_edges=show_edges, cmap=cmap, show_scalar_bar=False)
bp.add_mesh(sst[5], scalars="faces", show_edges=show_edges, cmap=cmap, show_scalar_bar=True)
bp.scalar_bar.SetTitle("SST / K")

bp.show_axes_all()
bp.link_views()
bp.add_callback(draw, interval=100)
bp.camera_position = "yz"
