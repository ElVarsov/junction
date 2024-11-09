import ifcopenshell
import ifcopenshell.util.element
from ifcopenshell import *
import ifcopenshell.util.placement
import ifcopenshell.geom
import numpy as np
import trimesh

def where_are_we(model,point):
    # Load the existing IFC file or create a new one
    space = model.by_type('IFCSPACE')
    #print(space[0].get_info())
    settings = ifcopenshell.geom.settings()
    geometry_spaces = []
    for space in space:
        try:
            shape = ifcopenshell.geom.create_shape(settings, space)
            verts = shape.geometry.verts  # Flat list of vertex coordinates
            faces = shape.geometry.faces  # Indices into the verts list

                # Reshape the vertices and faces

            verts_array = np.array(verts, dtype=float).reshape(-1, 3)
            faces_array = np.array(faces, dtype=int).reshape(-1, 3)

            geometry_spaces.append({
                'space': space,
                'vertices': verts_array,
                'faces': faces_array
            })
        except:
            print(f"Could not process space: {space.GlobalId}")

    # Flag to check if the point was found in any space
    point_found = False

    for geom_space in geometry_spaces:
        mesh = trimesh.Trimesh(vertices=geom_space['vertices'], faces=geom_space['faces'])

        # Check if the point is inside the mesh
        is_inside = mesh.contains([point])[0]

        if is_inside:
            space = geom_space['space']
            print(f"Point is inside space: {space.Name} (ID: {space.GlobalId})")
            # Assign your object to this space here
            point_found = True
            break  # Remove this if you want to find all spaces containing the point

    if not point_found:
        return "0"
    
    space_found = geom_space['space']
    
    return space_found.GlobalId


def block_list(model,location_id):
    #space = model.by_guid(location_id)
    all_blocks = model.by_type('IfcBuildingElementProxies')
    block_in_space =[]
    for element in all_blocks:
        if element.Location == location_id:
            block_in_space.append(element.Name)
    return block_in_space

