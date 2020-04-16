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
lo, hi = 60, 90
tkwargs = dict(value=(lo, hi), scalars="lats", preference="point")

pdata_sst = {t: pv.read(f"pdata_xy_sst_t{t}.vtk").threshold(scalars="faces") for t in range(N_steps)}
sst = pv.read("pdata_xy_sst_t0.vtk").threshold(scalars="faces")
sst.set_active_scalars("faces")

pdata_sst_threshold = {t: pv.read(f"pdata_xy_sst_t{t}.vtk").threshold(scalars="faces").threshold(**tkwargs) for t in range(N_steps)}
sst_threshold = pv.read("pdata_xy_sst_t0.vtk").threshold(scalars="faces").threshold(**tkwargs)
sst_threshold.set_active_scalars("faces")

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
inner_hi = 0.2
inner_lo = 0.4
outer = 1.2
normal = (0, 0, 1)
r_res = 1
c_res = 60
opacity = 0.8
color = "white"

p.subplot(0, 0)
p.add_mesh(sst, show_edges=True, cmap=cmap, show_scalar_bar=True)
p.add_text("C48 time-series", font_size=13, shadow=True, font="courier")
hi_disc = pv.Disc(center=center, inner=inner_hi, outer=outer, normal=normal, r_res=r_res, c_res=c_res)
hi_disc.translate((0, 0, np.cos(np.radians(90-hi))))
hi_disc_actor = p.add_mesh(hi_disc, opacity=opacity, color=color)
lo_disc = pv.Disc(center=center, inner=inner_lo, outer=outer, normal=normal, r_res=r_res, c_res=c_res)
lo_disc.translate((0, 0, np.cos(np.radians(90-lo))))
lo_disc_actor = p.add_mesh(lo_disc, opacity=opacity, color=color)
p.add_checkbox_button_widget(show_lo, value=True, size=20, border_size=2, color_on="green")
p.add_checkbox_button_widget(show_hi, value=True, size=20, border_size=2, color_on="green", position=(10, 33))

p.subplot(0, 1)
p.add_mesh(sst_threshold, show_edges=True, cmap=cmap, scalar_bar_args=sargs, opacity=1.0, show_scalar_bar=True)
p.add_text(f"C48 time-series [{lo}, {hi}]", font_size=15, shadow=True, font="courier")
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
#p.show_grid()
p.scalar_bar.SetTitle("sst / K")
#p.add_scalar_bar(**sargs)
p.add_callback(draw, interval=100)
p.camera_position = "yz"

