import netCDF4 as nc
import numpy as np


def earth_cube_nodes(C, r=None, debug=False):
    if r is None:
        r = 1.0
    xs, ys, zs = [], [], []
    s = slice(0, -1)
    Cp1 = C + 1

    #
    # panel 0: yz-plane (+x) - equatorial (europe & africa)
    #
    if debug:
        print("panel: 0")
    shape = (Cp1, Cp1)
    dtype = np.float16

    p0_xs = np.ones(shape, dtype=dtype) * r
    if debug:
        print("xs:\n", p0_xs)

    p0_ys = np.ones(shape, dtype=dtype)
    y = np.linspace(-r, r, Cp1, dtype=dtype)
    p0_ys *= y
    if debug:
        print("ys:\n", p0_ys)

    p0_zs = np.ones(shape, dtype=dtype)
    z = np.linspace(r, -r, Cp1, dtype=dtype).reshape(-1, 1)
    p0_zs *= z
    if debug:
        print("zs:\n", p0_zs)

    xs.append(p0_xs[s, s].ravel())
    ys.append(p0_ys[s, s].ravel())
    zs.append(p0_zs[s, s].ravel())

    if debug:
        print(xs[0].reshape(C, -1))
        print(ys[0].reshape(C, -1))
        print(zs[0].reshape(C, -1))

    #
    # panel 1: xz-plane (+y) - equatorial (asia & west australia)
    #
    if debug:
        print("panel: 1")

    p1_xs = np.ones(shape, dtype=dtype)
    x = np.linspace(r, -r, Cp1, dtype=dtype)
    p1_xs *= x
    if debug:
        print("xs:\n", p1_xs)

    p1_ys = np.ones(shape, dtype=dtype) * r
    if debug:
        print("ys:\n", p1_ys)

    p1_zs = np.ones(shape, dtype=dtype)
    z = np.linspace(r, -r, Cp1, dtype=dtype).reshape(-1, 1)
    p1_zs *= z
    if debug:
        print("zs:\n", p1_zs)

    xs.append(p1_xs[s, s].ravel())
    ys.append(p1_ys[s, s].ravel())
    zs.append(p1_zs[s, s].ravel())

    if debug:
        print(xs[1].reshape(C, -1))
        print(ys[1].reshape(C, -1))
        print(zs[1].reshape(C, -1))

    #
    # panel 2: yz-plane (-x) - equaltorial (east australia)
    #
    if debug:
        print("panel: 2")

    p2_xs = np.ones(shape, dtype=dtype) * -r
    if debug:
        print("xs:\n", p2_xs)

    p2_ys = np.ones(shape, dtype=dtype)
    y = np.linspace(r, -r, Cp1, dtype=dtype)
    p2_ys *= y
    if debug:
        print("ys:\n", p2_ys)

    p2_zs = np.ones(shape, dtype=dtype)
    z = np.linspace(r, -r, Cp1, dtype=dtype).reshape(-1, 1)
    p2_zs *= z
    if debug:
        print("zs:\n", p2_zs)

    xs.append(p2_xs[s, s].ravel())
    ys.append(p2_ys[s, s].ravel())
    zs.append(p2_zs[s, s].ravel())

    if debug:
        print(xs[2].reshape(C, -1))
        print(ys[2].reshape(C, -1))
        print(zs[2].reshape(C, -1))

    #
    # panel 3: xz-plane (-y) - equatorial (north & south america)
    #
    if debug:
        print("panel: 3")

    p3_xs = np.ones(shape, dtype=dtype)
    x = np.linspace(-r, r, Cp1, dtype=dtype)
    p3_xs *= x
    if debug:
        print("xs:\n", p3_xs)

    p3_ys = np.ones(shape, dtype=dtype) * -r
    if debug:
        print("ys:\n", p3_ys)

    p3_zs = np.ones(shape, dtype=dtype)
    z = np.linspace(r, -r, Cp1, dtype=dtype).reshape(-1, 1)
    p3_zs *= z
    if debug:
        print("zs:\n", p3_zs)

    xs.append(p3_xs[s, s].ravel())
    ys.append(p3_ys[s, s].ravel())
    zs.append(p3_zs[s, s].ravel())

    if debug:
        print(xs[3].reshape(C, -1))
        print(ys[3].reshape(C, -1))
        print(zs[3].reshape(C, -1))

    #
    # panel 4: xy-plane (+z) - north (polar)
    #
    if debug:
        print("panel: 4")

    p4_xs = np.ones(shape, dtype=dtype)
    x = np.linspace(-r, r, Cp1, dtype=dtype).reshape(-1, 1)
    p4_xs *= x
    if debug:
        print("xs:\n", p4_xs)

    p4_ys = np.ones(shape, dtype=dtype)
    y = np.linspace(-r, r, C+1, dtype=dtype)
    p4_ys *= y
    if debug:
        print("ys:\n", p4_ys)

    p4_zs = np.ones(shape, dtype=dtype) * r
    if debug:
        print("zs:\n", p4_zs)

    p4_xs = p4_xs[slice(1, -1), slice(1, -1)].T
    p4_ys = p4_ys[slice(1, -1), slice(1, -1)].T
    p4_zs = p4_zs[slice(1, -1), slice(1, -1)].T

    xs.append(p4_xs[:, ::-1].ravel())
    ys.append(p4_ys[:, ::-1].ravel())
    zs.append(p4_zs[:, ::-1].ravel())

    if debug:
        print(xs[4].reshape(C-1, C-1))
        print(ys[4].reshape(C-1, C-1))
        print(zs[4].reshape(C-1, C-1))

    #
    # panel 5: xy-plane (-z) - south (antarctica)
    #
    if debug:
        print("panel: 5")

    p5_xs = np.ones(shape, dtype=dtype)
    x = np.linspace(r, -r, C+1, dtype=dtype).reshape(-1, 1)
    p5_xs = x * p5_xs
    if debug:
        print("xs:\n", p5_xs)

    p5_ys = np.ones(shape, dtype=dtype)
    y = np.linspace(-r, r, C+1, dtype=dtype)
    p5_ys *= y
    if debug:
        print("ys:\n", p5_ys)

    p5_zs = np.ones(shape, dtype=dtype) * -r
    if debug:
        print("zs:\n", p5_zs)

    p5_xs = p5_xs.T[::-1, :]
    p5_ys = p5_ys.T[::-1, :]
    p5_zs = p5_zs.T[::-1, :]

    xs.append(p5_xs[:, :-1].ravel())
    ys.append(p5_ys[:, :-1].ravel())
    zs.append(p5_zs[:, :-1].ravel())

    xs.append(p5_xs[:, -1].ravel())
    ys.append(p5_ys[:, -1].ravel())
    zs.append(p5_zs[:, -1].ravel())

    if debug:
        print(xs[5].reshape(Cp1, C))
        print(ys[5].reshape(Cp1, C))
        print(zs[5].reshape(Cp1, C))
        print(xs[6])
        print(ys[6])
        print(zs[6])

    xs, ys, zs = np.concatenate(xs), np.concatenate(ys), np.concatenate(zs)

    return np.vstack((xs, ys, zs)).T


def load_nodes(fname, node_face, node_x, node_y, radius, start_index=True, data=None, xy=None):
    with nc.Dataset(fname) as ds:
        node_face = ds.variables[node_face][:].data
        node_x = ds.variables[node_x][:].data
        node_y = ds.variables[node_y][:].data
        
        if data is not None:
            data = ds.variables[data][:]
            mask = data.mask
            data = data.data
            data[mask] = np.nan

    # account for start_index = 1
    if start_index:
        node_face = node_face - 1

    # convert lat/lon to cartesian coordinates
    node_x_rad = np.radians(node_x)
    node_y_rad = np.radians(90.0 - node_y)

    x = radius * np.sin(node_y_rad) * np.cos(node_x_rad)
    y = radius * np.sin(node_y_rad) * np.sin(node_x_rad)
    z = radius * np.cos(node_y_rad)

    # construct the vertex count + offsets for each face
    N_nodes = 4
    N_faces = node_face.shape[0]
    faces = np.hstack((np.broadcast_to(np.array([N_nodes], np.int8), (N_faces, 1)),
                      node_face))

    if data is not None:
        result = (x, y, z), faces, data
    else:
        result = (x, y, z), faces

    if xy:
        result = result + (node_x, node_y)

    return result


def load(fname, node_face, node_x, node_y, radius, start_index=True, cube=None):
    ds = nc.Dataset(fname)
    node_face = ds.variables[node_face][:].data
    node_x = ds.variables[node_x][:].data
    node_y = ds.variables[node_y][:].data

    if cube is not None:
        cube_x, cube_y, cube_z = cube[:, 0], cube[:, 1], cube[:, 2]

    # account for start_index = 1
    if start_index:
        node_x = np.concatenate(([0], node_x))
        node_y = np.concatenate(([0], node_y))

        if cube is not None:
            cube_x = np.concatenate(([0], cube_x))
            cube_y = np.concatenate(([0], cube_y))
            cube_z = np.concatenate(([0], cube_z))

    if cube is not None:
        x = radius * cube_x[node_face]
        y = radius * cube_y[node_face]
        z = radius * cube_z[node_face]
    else:
        # convert lat/lon to cartesian coordinates
        node_face_x = node_x[node_face]
        node_face_y = 90.0 - node_y[node_face]

        node_face_x_rad = np.radians(node_face_x)
        node_face_y_rad = np.radians(node_face_y)

        x = radius * np.sin(node_face_y_rad) * np.cos(node_face_x_rad)
        y = radius * np.sin(node_face_y_rad) * np.sin(node_face_x_rad)
        z = radius * np.cos(node_face_y_rad)

    return (ds, (x, y, z))


def netcdf_copy(dsin, fnamein, datain):
    assert datain.ndim == 1, "oops! expected only 1D datain"

    # output file
    fnameout, ext = os.path.splitext(fnamein)
    fnameout = os.path.join(f"{fnameout}_synthetic{ext}")

    dsout = nc.Dataset(fnameout, "w", format=dsin.file_format)

    dnameout = None
    meshout = None
    coordinates = []

    # copy dimensions
    for dname, the_dim in dsin.dimensions.items():
        #print(dname, the_dim.size)
        if the_dim.size == datain.shape[0]:
            dnameout = dname
        dsout.createDimension(dname, the_dim.size if not the_dim.isunlimited() else None)

    # copy variables
    for v_name, varin in dsin.variables.items():
        outVar = dsout.createVariable(v_name, varin.datatype, varin.dimensions)
        #print(v_name, varin.datatype, varin.dimensions)

        # copy variable attributes
        attrs = {k: varin.getncattr(k) for k in varin.ncattrs()}
        outVar.setncatts(attrs)
        outVar[:] = varin[:]

        if "cf_role" in attrs and attrs["cf_role"] == "mesh_topology":
            meshout = v_name
        if len(varin.dimensions) == 1 and varin.dimensions[0] == dnameout:
            coordinates.append(v_name)

    # create the new data variable
    assert dnameout is not None, "oops! no output dimension name found"
    assert meshout is not None, "oops! no output mesh topology found"
    outVar = dsout.createVariable("synthetic", datain.dtype, (dnameout,))
    outVar[:] = datain
    coordinatesout = ' '.join(coordinates)
    attrs = dict(long_name="synthetic", units="1", mesh=meshout, coordinates=coordinatesout)
    outVar.setncatts(attrs)

    # copy global attributes
    dsout.setncatts({k: dsin.getncattr(k) for k in dsin.ncattrs()})

    # close the output file
    dsout.close()

