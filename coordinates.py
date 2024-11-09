import pyproj

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

# Example usage
latitude = 60.1699
longitude = 24.9384
utm_x, utm_y = convert_gps_to_utm(*point1)
print(f"UTM Coordinates: X={utm_x}, Y={utm_y}")

dx = point1_ifc[0] - point2_ifc[0]
dy = point1_ifc[1] - point2_ifc[1]

resx = utm_x - dx
resy = utm_y - dy

zero_x = resx - point2_ifc[0]
zero_y = resy - point2_ifc[1]


print(zero_x, zero_y)

print(convert_utm_to_gps(zero_x, zero_y))