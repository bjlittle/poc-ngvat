import numpy as np
import pyvista as pv

from utils import coastline


resolution = "50m"
blocks = coastline(resolution=resolution)
print(f"Geometries: {len(blocks)}")

mesh = pv.read("data/test/real/pdata_sst_t0.vtk")
mesh["rlats"] = mesh.points[:, 2]

lo, hi = -30, 30
radius = 1.0
rlo, rhi = radius * np.cos(np.radians(90-lo)), radius * np.cos(np.radians(90-hi))
value = (rlo, rhi)
tkwargs = dict(value=value, scalars="rlats", preference="point")

tmesh = mesh.threshold(**tkwargs)

p = pv.Plotter()

for block in blocks:
    block["rlats"] = block.points[:, 2]
    tblock = block.threshold(**tkwargs)
    if tblock.n_cells:
        p.add_mesh(tblock, color="white")

p.add_mesh(tmesh, scalars="faces", cmap="coolwarm", show_edges=True, show_scalar_bar=True)

p.scalar_bar.SetTitle("SST / K")
p.add_text(f"C48 SST [{lo}, {hi}] (enclosed, {resolution} coastlines)", font_size=15, shadow=True, font="courier")
p.show()
