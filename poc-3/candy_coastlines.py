import pyvista as pv

from utils import coastline


resolution = "50m"
blocks = coastline(resolution=resolution)
print(f"Geometries: {len(blocks)}")

p = pv.Plotter()
for block in blocks:
    p.add_mesh(block, color="white")
p.add_text(f"{resolution} Coastlines", font_size=13, shadow=True, font="courier")
p.show()
