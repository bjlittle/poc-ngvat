import pyvista as pv
from pyvista import examples


def callback_slider(value):
    global p
    global mesh
    global display
    
    factor = value * 1e-6
    print(factor)
    result = mesh.warp_by_scalar(factor=factor)
    display.points = result.points


mesh = examples.download_topo_global()

mesh.compute_normals(inplace=True)
display = mesh.copy()
cmap = "CET_D13"

p = pv.BackgroundPlotter()
p.add_mesh(display, cmap=cmap, show_scalar_bar=False)

p.add_slider_widget(callback_slider, rng=(0, 50), value=0, title="Warp Factor")
p.add_text("Altitude Warping", font_size=13, shadow=True, font="courier")

p.add_axes()
p.show()

