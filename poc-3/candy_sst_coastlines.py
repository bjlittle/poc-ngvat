import pyvista as pv

from utils import coastline

resolution = "50m"
blocks = coastline(resolution=resolution)
print(f"Geometries: {len(blocks)}")

mesh = pv.read("real/pdata_sst_t0.vtk")

p = pv.Plotter()
for block in blocks:
    p.add_mesh(block, color="white")
p.add_mesh(mesh, scalars="faces", cmap="coolwarm", show_edges=True, show_scalar_bar=True)
p.scalar_bar.SetTitle("SST / K")
p.add_text(f"C48 SST ({resolution} coastlines)", font_size=10, shadow=True)
p.show()
