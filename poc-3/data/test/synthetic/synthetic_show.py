import matplotlib.pyplot as plt
import numpy as np
import pyvista as pv


ugrid_c4 = pv.read("ugrid_C4_synthetic.vtk")
ugrid_c12 = pv.read("ugrid_C12_synthetic.vtk")
ugrid_c24 = pv.read("ugrid_C24_synthetic.vtk")
ugrid_c48 = pv.read("ugrid_C48_synthetic.vtk")
ugrid_c96 = pv.read("ugrid_C96_synthetic.vtk")
ugrid_c1048 = pv.read("ugrid_C1048_synthetic.vtk")

p = pv.Plotter(shape=(2, 3))

p.subplot(0, 0)
p.add_text("C4")
p.add_mesh(ugrid_c4, scalars=ugrid_c4.get_array("faces"), show_edges=True, cmap=plt.cm.get_cmap("viridis", 4**2))
#p.add_points(ugrid_c4.points, color="red", render_points_as_spheres=True)

p.subplot(0, 1)
p.add_text("C12")
p.add_mesh(ugrid_c12, scalars=ugrid_c12.get_array("faces"), show_edges=True, cmap=plt.cm.get_cmap("viridis", 12**2))
#p.add_points(ugrid_c12.points, color="red", render_points_as_spheres=True)

p.subplot(0, 2)
p.add_text("C24")
p.add_mesh(ugrid_c24, scalars=ugrid_c24.get_array("faces"), show_edges=True, cmap=plt.cm.get_cmap("viridis", 24**2))
#p.add_points(ugrid_c24.points, color="red", render_points_as_spheres=True)

p.subplot(1, 0)
p.add_text("C48")
p.add_mesh(ugrid_c48, scalars=ugrid_c48.get_array("faces"), show_edges=True, cmap=plt.cm.get_cmap("viridis", 48**2))

p.subplot(1, 1)
p.add_text("C96")
p.add_mesh(ugrid_c96, scalars=ugrid_c96.get_array("faces"), show_edges=True, cmap=plt.cm.get_cmap("viridis", 96**2))

p.subplot(1, 2)
p.add_text("C1048")
p.add_mesh(ugrid_c1048, scalars=ugrid_c1048.get_array("faces"), show_edges=True, cmap=plt.cm.get_cmap("viridis", 1048**2))

p.show_axes_all()
p.link_views()
cpos = np.array([(0.0, -1.2, 0.0), (0.0, 0.0, 0.0), (0.0, 0.0, 1.0)])
r = p.show(cpos=cpos)
