import matplotlib.pyplot as plt
from matplotlib.ticker import StrMethodFormatter
import numpy as np


radius = 1.0
area_sphere = 4 * np.pi * radius**2
xmin, xmax = 0, 11
ymin, ymax = 12.5655, 12.5665

xoffset = 4
plt.xlim(xmin, xmax+1)
plt.ylim(ymin, ymax)
plt.hlines(area_sphere, xmin-1, xmax+1, linestyle="dashed", colors="red", label="S2 Sphere Area")

areas = [12.160646375229627,
         12.520397139859082,
         12.5548565112733,
         12.56349079392264,
         12.565650578352935,
         12.566190600301852,
         12.566325610528853,
         12.566359363381842,
         12.566364572226727,
         12.56636821770015,
         12.566368229181164]

plt.plot(range(xmin, xmax), areas, marker='o', linestyle="dotted", label="Polyhedron Area")
labels = ["C4", "C12", "C24", "C48", "C96", "C192", "C384", "C768", "C1048", "C1664", "C1668"]

xoffset = 4
plt.xticks(range(xmin, xmax))
plt.gca().set_xticklabels(labels)
plt.yticks(np.linspace(ymin, ymax, 10))
plt.gca().ticklabel_format(axis="y", style="plain", useOffset=False)
plt.gca().yaxis.set_major_formatter(StrMethodFormatter('{x:,.4f}'))

plt.title("Cube-Sphere Polyhedron Surface Area (pyvista)")
plt.ylabel("Total Surface Area")
plt.xlabel("Mesh Resolution")
plt.grid(True)
plt.legend(loc="lower right")

#plt.gca().set_yscale("log")

plt.show()
