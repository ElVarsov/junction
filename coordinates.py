import pyproj

def gps_to_ifc(longitude, latitude, altitude, origin_longitude, origin_latitude, origin_altitude):
    """
    Convert GPS coordinates (longitude, latitude, altitude) to IFC project coordinates.

    Parameters:
    - longitude, latitude, altitude: GPS coordinates in degrees and meters.
    - origin_longitude, origin_latitude, origin_altitude: The origin coordinates in GPS.

    Returns:
    - ifc_x, ifc_y, ifc_z: IFC project coordinates in millimeters.
    """
    # Create a Transformer object
    transformer_to_utm = pyproj.Transformer.from_crs("EPSG:4326", "EPSG:32633")  # Adjust UTM zone as needed

    # Convert the origin and GPS coordinates to UTM
    origin_x, origin_y = transformer_to_utm.transform(origin_latitude, origin_longitude)
    gps_x, gps_y = transformer_to_utm.transform(latitude, longitude)

    # Calculate the IFC project coordinates in millimeters
    ifc_x = (gps_x - origin_x) * 1000  # Convert meters to mm
    ifc_y = (gps_y - origin_y) * 1000  # Convert meters to mm
    ifc_z = (altitude - origin_altitude) * 1000  # Convert meters to mm

    return ifc_x, ifc_y, ifc_z


def ifc_to_gps(ifc_x, ifc_y, ifc_z, known_longitude, known_latitude, known_altitude):
    """
    Calculate the GPS coordinates of the IFC origin (0, 0, 0) given the GPS coordinates of a known point in IFC.

    Parameters:
    - ifc_x, ifc_y, ifc_z: The IFC coordinates in millimeters of the known point.
    - known_longitude, known_latitude, known_altitude: The GPS coordinates of the known point.

    Returns:
    - origin_longitude, origin_latitude, origin_altitude: The GPS coordinates of the origin point in IFC.
    """
    # Create a Transformer object
    transformer_to_utm = pyproj.Transformer.from_crs("EPSG:4326", "EPSG:32633")  # Adjust UTM zone as needed
    transformer_to_geodetic = pyproj.Transformer.from_crs("EPSG:32633", "EPSG:4326")  # Reverse transformation

    # Convert the known GPS coordinates to UTM
    known_x, known_y = transformer_to_utm.transform(known_latitude, known_longitude)

    # Calculate the origin UTM coordinates in meters (since IFC is in mm, divide by 1000)
    origin_x = known_x - (ifc_x / 1000)  # Convert mm to meters
    origin_y = known_y - (ifc_y / 1000)  # Convert mm to meters
    origin_z = known_altitude - (ifc_z / 1000)  # Convert mm to meters

    # Convert the origin UTM coordinates back to GPS
    origin_latitude, origin_longitude = transformer_to_geodetic.transform(origin_x, origin_y)
    origin_altitude = origin_z

    return origin_longitude, origin_latitude, origin_altitude

# Example usage
ifc_x, ifc_y, ifc_z = 5000, 3000, 1000  # Example IFC coordinates in mm
known_longitude, known_latitude, known_altitude = 24.9384, 60.1699, 50.0  # Known GPS coordinates

origin_longitude, origin_latitude, origin_altitude = ifc_to_gps(ifc_x, ifc_y, ifc_z, known_longitude, known_latitude, known_altitude)
print(f"Origin GPS Coordinates: Longitude={origin_longitude}, Latitude={origin_latitude}, Altitude={origin_altitude}")


# Example usage
longitude, latitude, altitude = 24.9384, 60.1699, 50.0  # Example GPS coordinates
origin_longitude, origin_latitude, origin_altitude = 24.9380, 60.1695, 0.0  # Origin point in GPS

ifc_x, ifc_y, ifc_z = gps_to_ifc(longitude, latitude, altitude, origin_longitude, origin_latitude, origin_altitude)
print(f"IFC Project Coordinates: X={ifc_x} mm, Y={ifc_y} mm, Z={ifc_z} mm")