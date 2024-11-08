import ifcopenshell
import ifcopenshell.util
import ifcopenshell.util.element
from ifcopenshell import *

model = ifcopenshell.open('Kaapelitehdas_junction.ifc')

"""Get info from image recognition"""
def get_new_item_inforamtion(item):
    item_info = {}
    item_info = {"Name": "name",
     "Location": "Location",
     "Manufacturer": "Manufacturer",
     "object_type": "type",
     "size": "size",
     "age": "age",
     "material": "material",
     "conditions": "conditions",
     "comment": "comments"
      }
    return item_info

def create_property_set(model, object, property_set_name, properties):
    # Generate a unique GlobalId for the property set
    property_set_id = ifcopenshell.guid.new()

    # Create an IfcPropertySet
    property_set = model.create_entity("IfcPropertySet", GlobalId=property_set_id, Name=property_set_name)
    
    # Convert HasProperties to a list if it is not already
    
    properties_ = list()

    property_set.HasProperties = []

    # Create IfcPropertySingleValue for each property
    for prop_name, prop_value in properties.items():
        # Create an IfcPropertySingleValue, specifying the correct IFC data type for the value
        if isinstance(prop_value, str):
            value = model.create_entity("IfcText", prop_value)
        elif isinstance(prop_value, int):
            value = model.create_entity("IfcInteger", prop_value)
        elif isinstance(prop_value, float):
            value = model.create_entity("IfcReal", prop_value)
        else:
            value = model.create_entity("IfcText", str(prop_value))  # Default to text if type is unknown
        
        property = model.create_entity(
            "IfcPropertySingleValue",
            Name=prop_name,
            NominalValue=value
        )
        properties_.append(property)  # Now we can append properties

        property_set.HasProperties = properties_

    # Create an IfcRelDefinesByProperties to attach the property set to the object
    rel_id = ifcopenshell.guid.new()
    rel_defines = model.create_entity(
        "IfcRelDefinesByProperties",
        GlobalId=rel_id,
        RelatedObjects=[object],
        RelatingPropertyDefinition=property_set
    )
    
    return property_set

def add_new_item_with_properties():
    # Create a new object (e.g., IfcFurnishingElement)

    objects = model.by_type("IfcObject")
    print(len(objects))
    new_item = model.create_entity("IfcObject", GlobalId=ifcopenshell.guid.new(), Name="New Item")
    
    
    # Define custom properties
    properties = get_new_item_inforamtion(" ")

    create_property_set(model, new_item, "CustomProperties", properties)
    
    # Output information
    objects = model.by_type("IfcObject")
    print(len(objects))
    print(new_item.get_info())



add_new_item_with_properties()
model.write('Kaapelitehdas_junction_modified.ifc')



model = ifcopenshell.open('Kaapelitehdas_junction_modified.ifc')

def get_properties_from_object(ifc_object):
    # Dictionary to store properties
    properties = {}

    # Iterate over the relationships of the object
    for rel in model.by_type("IfcRelDefinesByProperties"):
        if ifc_object in rel.RelatedObjects:
            property_set = rel.RelatingPropertyDefinition
            if property_set.is_a("IfcPropertySet"):
                # Iterate over the properties in the property set
                for prop in property_set.HasProperties:
                    if prop.is_a("IfcPropertySingleValue"):
                        # Extract the property name and value
                        prop_name = prop.Name
                        prop_value = prop.NominalValue.wrappedValue
                        properties[prop_name] = prop_value

    return properties

# Example usage
def extract_properties_from_new_item():
    # Assuming you have already created an object in your model
    new_item = model.by_type("IfcObject")[0]  # Replace with the correct object if necessary
    properties = get_properties_from_object(new_item)
    print(properties)

extract_properties_from_new_item()

