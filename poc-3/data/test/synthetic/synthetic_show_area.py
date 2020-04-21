import matplotlib.pyplot as plt
import numpy as np
import pyvista as pv


pdata_c4 = pv.read("pdata_area_C4.vtk")
pdata_c12 = pv.read("pdata_area_C12.vtk")
pdata_c24 = pv.read("pdata_area_C24.vtk")
pdata_c48 = pv.read("pdata_area_C48.vtk")
pdata_c96 = pv.read("pdata_area_C96.vtk")
pdata_c1048 = pv.read("pdata_area_C1048.vtk")

cmap = "coolwarm"
show_edges = True
show_scalar_bar = False
stitle = "Cell Area"

scalar_kwargs = dict(n_labels=3)#, font_family="courier")#, title_font_size=10, label_font_size=10, vertical=False)

p = pv.Plotter(shape=(2, 3))

p.subplot(0, 0)
p.add_text("C4", font_size=10, shadow=True)
area = pdata_c4["area"]
clim = [area.min(), area.max()]
p.add_mesh(pdata_c4, scalars=area, show_edges=show_edges, cmap=cmap, clim=clim, show_scalar_bar=show_scalar_bar)
p.add_scalar_bar(title="C4 Cell Area", **scalar_kwargs)

p.subplot(0, 1)
p.add_text("C12", font_size=10, shadow=True)
area = pdata_c12["area"]
clim = [area.min(), area.max()]
p.add_mesh(pdata_c12, scalars=area, show_edges=show_edges, cmap=cmap, clim=clim, show_scalar_bar=show_scalar_bar)
p.add_scalar_bar(title="C12 Cell Area", **scalar_kwargs)

p.subplot(0, 2)
p.add_text("C24", font_size=10, shadow=True)
area = pdata_c24["area"]
clim = [area.min(), area.max()]
p.add_mesh(pdata_c24, scalars=area, show_edges=show_edges, cmap=cmap, clim=clim, show_scalar_bar=show_scalar_bar)
p.add_scalar_bar(title="C24 Cell Area", **scalar_kwargs)

p.subplot(1, 0)
p.add_text("C48", font_size=10, shadow=True)
area = pdata_c48["area"]
clim = [area.min(), area.max()]
p.add_mesh(pdata_c48, scalars=area, show_edges=show_edges, cmap=cmap, clim=clim, show_scalar_bar=show_scalar_bar)
p.add_scalar_bar(title="C48 Cell Area", **scalar_kwargs)

p.subplot(1, 1)
p.add_text("C96", font_size=10, shadow=True)
area = pdata_c96["area"]
clim = [area.min(), area.max()]
p.add_mesh(pdata_c96, scalars=area, show_edges=show_edges, cmap=cmap, clim=clim, show_scalar_bar=show_scalar_bar)
p.add_scalar_bar(title="C96 Cell Area", **scalar_kwargs)

p.subplot(1, 2)
p.add_text("C1048", font_size=10, shadow=True)
area = pdata_c1048["area"]
clim = [area.min(), area.max()]
p.add_mesh(pdata_c1048, scalars=area, show_edges=show_edges, cmap=cmap, clim=clim, show_scalar_bar=show_scalar_bar)
p.add_scalar_bar(title="C1048 Cell Area", **scalar_kwargs)

p.show_axes_all()
#p.show_axes()
p.link_views()
p.show()
