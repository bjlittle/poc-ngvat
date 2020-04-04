import matplotlib.pyplot as plt
import numpy as np
import pyvista as pv


def draw():
    global t
    global actor
    global sst
    global ugrid_sst
    global p

    #if actor is not None:
    #    p.remove_actor(actor)
    if actor is None:
        actor = p.add_text(f"C48 SST global time-series")
    sst.cell_arrays["faces"] = ugrid_sst[t].get_array("faces")
    #print(f"hello {t}")
    
    t = 0 if t == 11 else t + 1


ugrid_sst = {t: pv.read(f"ugrid_sst_t{t}.vtk") for t in range(12)}
sst = pv.read("ugrid_sst_t0.vtk")
sst.set_active_scalars("faces")
t = 0
actor = None

cmap = "coolwarm"  # colorcet (perceptually accurate) color maps

#p = pv.Plotter(shape=(2, 6))
#R, C = 2, 6
#for r in range(R):
#    for c in range(C):
#        p.subplot(r, c)
#        t = (r*C) + c
#        p.add_text(f"C48 SST t{t}")
#        sst = ugrid_sst[t]
#        p.add_mesh(sst, scalars=sst.get_array("faces"), show_edges=True, cmap=cmap)
#p.show_axes_all()
#p.link_views()
#cpos = np.array([(0.0, -5.0, 0.0), (0.0, 0.0, 0.0), (0.0, 0.0, 1.0)])
#p.show()

p = pv.BackgroundPlotter()
p.add_mesh(sst, scalars="faces", show_edges=True, cmap=cmap)
p.show_axes()
p.show_grid()
p.add_callback(draw, interval=100)
