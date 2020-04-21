import matplotlib.pyplot as plt
import numpy as np


radius = 1.0
area_sphere = 4 * np.pi * radius**2
xmin, xmax = 0, 5

plt.xlim(xmin-1, xmax+1)
plt.ylim(12.10, 12.80)
plt.hlines(area_sphere, xmin-1, xmax+1, linestyle="dashed", colors="red", label="S2 Sphere Area")

areas = [12.160646375229627,
         12.520397139859082,
         12.5548565112733,
         12.56349079392264,
         12.565650578352935,
         12.566364572226727]

plt.plot(areas, marker='o', linestyle="dotted", label="Polyhedron Area")
labels = ["", "C4", "C12", "C24", "C48", "C96", "C1048", ""]

ax = plt.gca()
ax.set_xticklabels(labels)

plt.title("Cube-Sphere Polyhedron Surface Area (pyvista)")
plt.ylabel("Total Surface Area")
plt.xlabel("Mesh Resolution")
plt.grid(True)
plt.legend(loc="upper right")

