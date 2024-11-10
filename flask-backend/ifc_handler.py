import ifcopenshell
import ifcopenshell.util
import ifcopenshell.util.element
import ifcopenshell.api
import coordinates
from ifcopenshell import *
import findspace
import json
import pyproj
import ifcopenshell.util.placement
import ifcopenshell.geom
import numpy as np
import trimesh
import update_model

def update_ifc_file(json_object, gps_coordinates):
    # model = ifcopenshell.open('Kaapelitehdas_junction_modified.ifc')
    update_model.add_new_item_with_properties(gps_coordinates, json_object)
    # model.write('Kaapelitehdas_junction_modified.ifc')