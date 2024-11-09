import pyproj


#Pre calibrated points of the building
point1 = (60.16236874308105, 24.905288683037003) 
point2 = (60.1613911264242, 24.902979338824377) 
point1_ifc = (58.057,39.113) 
point2_ifc = (-71.485,-68.524)



def convert_gps_to_utm(latitude, longitude):
    # Create a pyproj Transformer object to convert WGS84 to UTM (Finland Zone 35N)
    transformer = pyproj.Transformer.from_crs("epsg:4326", "epsg:3067", always_xy=True)
    
    # Transform the latitude and longitude to UTM coordinates
    utm_x, utm_y = transformer.transform(longitude, latitude)
    
    return utm_x, utm_y

def convert_utm_to_gps(easting, northing):
    # Use the EPSG code for Finland's UTM Zone 35N
    epsg_code = "3067"  # ETRS89 / ETRS-TM35FIN, commonly used for Finland

    # Create a pyproj Transformer object to convert UTM to WGS84
    transformer = pyproj.Transformer.from_crs(f"epsg:{epsg_code}", "epsg:4326", always_xy=True)
    
    # Transform the UTM coordinates to latitude and longitude
    longitude, latitude = transformer.transform(easting, northing)
    
    return latitude, longitude

dx = point1_ifc[0] - point2_ifc[0]
dy = point1_ifc[1] - point2_ifc[1]

utm_x, utm_y = convert_gps_to_utm(*point1)

point2_x = utm_x - dx
point2_y = utm_y - dy

zero_x = point2_x - point2_ifc[0]
zero_y = point2_y - point2_ifc[1]

def convert_gps_to_ifc(point):
    utm_x, utm_y = convert_gps_to_utm(*point)

    ifc_x = utm_x - zero_x
    ifc_y = utm_y - zero_y

    return ifc_x, ifc_y