import ifcopenshell
import ifcopenshell.geom
import matplotlib.pyplot as plt
from shapely.geometry import Polygon
import random

path_to_ifc = "Kaapelitehdas_junction.ifc"
# Open the IFC file
model = ifcopenshell.open(path_to_ifc)

# Get all storeys (floors) in the IFC file
storeys = model.by_type("IfcBuildingStorey")

# get first storey
selected_storey = storeys[0]

walls = [element for element in model.by_type("IFCWALLSTANDARDCASE")]

print(walls[0])

settings = ifcopenshell.geom.settings()
settings.set(settings.USE_WORLD_COORDS, True)


def plot_thing(wall, color):
    shape = ifcopenshell.geom.create_shape(settings, wall)
    points = shape.geometry.verts  # Extract vertices from geometry

    # Flatten points into 2D
    flat_points = []
    for i in range(0, len(points), 3):
        flat_points.append((points[i], points[i+1]))

    polygon = Polygon(flat_points)

    # Plot the polygon
    plt.plot(*polygon.exterior.xy, color)


def plot_space(id):
    for wall in walls:
        plot_thing(wall, "black")

    space = model.by_guid(id)
    plot_thing(space, "red")

    plt.axis('off')
    plt.savefig('room.png', dpi=300)
    # plt.show()


# get random space for testing
spaces = [element for element in model.by_type("IFCSPACE")]
plot_space(random.choice(spaces).GlobalId)
