import numpy as np
import pyvista as pv

from utils import coastline


def button_stop(status):
    global stop
    global run
    global rep_run
    
    stop = status
    if not stop:
        if not run:
            rep_run.SetState(1)
            run = True


def button_run(status):
    global run
    run = status


def event_draw():
    global NP
    global N_panel
    global i
    global mesh
    global p
    global actors
    global clim
    global add
    global stop
    global run
    global rep_run

    if run:
        if add:
            idx = [np*N_panel+i for np in range(NP)]
            cells = mesh.extract_cells(idx)
            actors.append(p.add_mesh(cells, scalars="faces", show_edges=True,
                                     cmap="coolwarm", clim=clim, show_scalar_bar=False))
        else:
            actor = actors.pop(0)
            p.remove_actor(actor)
        
        i += 1
        if i == N_panel:
            add = not add
            i = 0
            if stop:
                rep_run.SetState(0)
                run = False


def add_text(p, depth=0.1, opacity=1.0, color="tan"):
    x, y, z = 0, 1, 2
    scale = 0.5
    offset = 1.0 + depth/2
    
    def center(pts, scale):
        pts[:, x] -= np.min(pts[:, x])
        pts[:, y] -= np.min(pts[:, y])
        xmin, xmax = np.min(pts[:, x]), np.max(pts[:, x])
        pts[:, x] -= ((xmax - xmin) / 2)
        ymin, ymax = np.min(pts[:, y]), np.max(pts[:, y])
        pts[:, y] -= (ymax - ymin) / 2
        zmin, zmax = np.min(pts[:, z]), np.max(pts[:, z])
        pts[:, z] -= (zmax - zmin) / 2
        pts *= scale
        
    # panel: 1
    t = pv.Text3D("1", depth=depth)
    pts = t.points
    center(pts, scale)
    t.rotate_x(90)
    t.rotate_z(90)
    t.translate((offset, 0, 0))
    p.add_mesh(t, color=color, opacity=opacity)
    
    # panel: 2
    t = pv.Text3D("2", depth=depth)
    pts = t.points
    center(pts, scale)
    t.rotate_x(90)
    t.rotate_z(180)
    t.translate((0,  offset, 0))
    p.add_mesh(t, color=color, opacity=opacity)
    
    # panel: 3
    t = pv.Text3D("3", depth=depth)
    pts = t.points
    center(pts, scale)
    t.rotate_x(90)
    t.rotate_z(-90)
    t.translate((-offset, 0, 0))
    p.add_mesh(t, color=color)

    # panel: 4
    t = pv.Text3D("4", depth=depth)
    pts = t.points
    center(pts, scale)
    t.rotate_x(90)
    t.translate((0, -offset, 0))
    p.add_mesh(t, color=color, opacity=opacity)

    # panel: 5
    t = pv.Text3D("5", depth=depth)
    pts = t.points
    center(pts, scale)
    t.rotate_z(180)
    t.translate((0, 0, offset))
    p.add_mesh(t, color=color, opacity=opacity)

    # panel: 6
    t = pv.Text3D("6", depth=depth)
    pts = t.points
    center(pts, scale)
    t.rotate_y(180)
    t.translate((0, 0, -offset))
    p.add_mesh(t, color=color, opacity=opacity)
    
        
mesh = pv.read("synthetic/pdata_C12_synthetic.vtk")

NP = 6 
N = mesh.n_cells
N_panel = N / NP
i = 0
actors = []
run = False
stop = False

clim=(np.min(mesh["faces"]), np.max(mesh["faces"]))
add = True

coastlines = coastline(resolution="110m")

p = pv.BackgroundPlotter()
p.add_mesh(mesh, scalars=None, opacity=0, show_scalar_bar=False)
p.add_text("C12 Panel Cell Order", font_size=13, shadow=True, font="courier")
add_text(p, depth=0.1, opacity=0.7)
p.add_bounding_box()
actor_run = p.add_checkbox_button_widget(button_run, value=False, size=20, border_size=2, color_on="green")
p.add_checkbox_button_widget(button_stop, value=False, size=20, border_size=2, color_on="green", position=(10, 33))

for geometry in coastlines:
    p.add_mesh(geometry, color="white")

rep_run = actor_run.GetRepresentation()

p.show_axes()
p.add_callback(event_draw, interval=10)
p.camera_position = "yz"
