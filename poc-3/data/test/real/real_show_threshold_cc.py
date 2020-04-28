import matplotlib.pyplot as plt
import numpy as np
import pyvista as pv


def draw():
    global t
    global sst
    global pdata_sst
    global sst_threshold
    global pdata_sst_threshold
    global p

    sst.cell_arrays["faces"] = pdata_sst[t].get_array("faces")
    sst_threshold.cell_arrays["faces"] = pdata_sst_threshold[t].get_array("faces")
    
    t = 0 if t == 11 else t + 1

    
def show_lo(status):
    global lo_disc_actor
    status = int(status)
    lo_disc_actor.SetVisibility(status)


def show_hi(status):
    global hi_disc_actor
    status = int(status)
    hi_disc_actor.SetVisibility(status)


def show_lo_threshold(status):
    global lo_disc_threshold_actor
    status = int(status)
    lo_disc_threshold_actor.SetVisibility(status)


def show_hi_threshold(status):
    global hi_disc_threshold_actor
    status = int(status)
    hi_disc_threshold_actor.SetVisibility(status)
    

N_steps = 12
lo, hi = 30, 60
tkwargs = dict(value=(np.cos(np.radians(90-lo)), np.cos(np.radians(90-hi))), scalars="clats", preference="point")

pdata_sst = {t: pv.read(f"pdata_xy_sst_t{t}.vtk").threshold(scalars="faces") for t in range(N_steps)}
sst = pv.read("pdata_xy_sst_t0.vtk").threshold(scalars="faces")
sst.set_active_scalars("faces")
sst_cc = sst.cell_centers()
sst.cell_arrays["clats"] = np.array(sst_cc.points[:, 2])

pdata_sst_threshold = {}
for t in range(N_steps):
    mesh = pv.read(f"pdata_xy_sst_t{t}.vtk").threshold(scalars="faces")
    mesh.cell_arrays["clats"] = np.array(sst_cc.points[:, 2])
    pdata_sst_threshold[t] = mesh.threshold(**tkwargs)
#pdata_sst_threshold = {t: pv.read(f"pdata_xy_sst_t{t}.vtk").threshold(**tkwargs) for t in range(N_steps)}


#sst_threshold = pv.read("pdata_xy_sst_t0.vtk").threshold(**tkwargs)
sst_threshold = pv.read("pdata_xy_sst_t0.vtk").threshold(scalars="faces")
sst_threshold.set_active_scalars("faces")
sst_threshold_cc = sst_threshold.cell_centers()
sst_threshold.cell_arrays["clats"] = np.array(sst_threshold_cc.points[:, 2])
sst_threshold = sst_threshold.threshold(**tkwargs)
sst_threshold_cc.cell_arrays["clats"] = np.array(sst_threshold_cc.points[:, 2])
sst_threshold_cc = sst_threshold_cc.threshold(**tkwargs)

t = 0
cmap = "coolwarm"  # colorcet (perceptually accurate) color maps
sargs = dict(
             shadow=True,
             n_labels=5,
             italic=False,
             fmt="%.1f",
             font_family="ariel",
             nan_annotation=True,
             vertical=False,
)

p = pv.BackgroundPlotter(shape=(1, 2))

center= (0, 0, 0)
inner_hi = 0.4
inner_lo = 0.6
outer = 1.2
normal = (0, 0, 1)
r_res = 1
c_res = 60
opacity = 0.8
color = "white"

p.subplot(0, 0)
p.add_mesh(sst, show_edges=True, cmap=cmap, show_scalar_bar=True)
p.add_mesh(sst_cc, color="green", point_size=3.0, render_points_as_spheres=True)
p.add_text("C48 SST time-series", font_size=13, shadow=True, font="courier")
hi_disc = pv.Disc(center=center, inner=inner_hi, outer=outer, normal=normal, r_res=r_res, c_res=c_res)
hi_disc.translate((0, 0, np.cos(np.radians(90-hi))))
hi_disc_actor = p.add_mesh(hi_disc, opacity=opacity, color=color)
lo_disc = pv.Disc(center=center, inner=inner_lo, outer=outer, normal=normal, r_res=r_res, c_res=c_res)
lo_disc.translate((0, 0, np.cos(np.radians(90-lo))))
lo_disc_actor = p.add_mesh(lo_disc, opacity=opacity, color=color)
p.add_checkbox_button_widget(show_lo, value=True, size=20, border_size=2, color_on="green")
p.add_checkbox_button_widget(show_hi, value=True, size=20, border_size=2, color_on="green", position=(10, 33))

p.subplot(0, 1)
p.add_mesh(sst_threshold, show_edges=True, cmap=cmap, scalar_bar_args=sargs, show_scalar_bar=True)
p.add_mesh(sst_threshold_cc, color="green", point_size=3.0, render_points_as_spheres=True)
p.add_text(f"C48 SST time-series [{lo}, {hi}] (cell centers)", font_size=15, shadow=True, font="courier")
hi_disc_threshold = pv.Disc(center=center, inner=inner_hi, outer=outer, normal=normal, r_res=r_res, c_res=c_res)
hi_disc_threshold.translate((0, 0, np.cos(np.radians(90-hi))))
hi_disc_threshold_actor = p.add_mesh(hi_disc_threshold, opacity=opacity, color=color)
lo_disc_threshold = pv.Disc(center=center, inner=inner_lo, outer=outer, normal=normal, r_res=r_res, c_res=c_res)
lo_disc_threshold.translate((0, 0, np.cos(np.radians(90-lo))))
lo_disc_threshold_actor = p.add_mesh(lo_disc_threshold, opacity=opacity, color=color)
p.add_checkbox_button_widget(show_lo_threshold, value=True, size=20, border_size=2, color_on="green")
p.add_checkbox_button_widget(show_hi_threshold, value=True, size=20, border_size=2, color_on="green", position=(10, 33))

p.show_axes_all()
p.link_views()
p.scalar_bar.SetTitle("SST / K")
p.add_callback(draw, interval=100)
p.camera_position = "yz"

