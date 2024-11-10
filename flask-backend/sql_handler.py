import mysql.connector as sqltor
import json
import os
from dotenv import load_dotenv

password = "Jamil2208@"


def replace_none_with_empty(data):
    if isinstance(data, dict):
        return {k: replace_none_with_empty(v) for k, v in data.items()}
    elif data == "None":
        return ""
    return data


def get_entries():
    conn = sqltor.connect(host="localhost", user="root",
                          passwd=password, database="junction")
    cur = conn.cursor()

    query = "SELECT * FROM history ORDER BY upload_time DESC"
    cur.execute(query)
    column_names = [desc[0] for desc in cur.description]
    rows = cur.fetchall()
    result = [dict(zip(column_names, row)) for row in rows]
    
    cur.close()
    conn.close()
    return result  # Return as a list of dictionaries, not JSON

# print(get_entries())


def add_entry(data):
    conn = sqltor.connect(host="localhost", user="root",
                          passwd=password, database="junction")
    cur = conn.cursor()
    query = """
        INSERT INTO history (
            building_address, location_in_building, equipment_type, age, 
            equipment_name, manufacturer, model, serial_number, size_of_machine, material, upload_time
        ) 
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, NOW())
    """

    # Use `get` with `None` as the default value to handle missing keys
    values = (
        data.get("building_address", None),
        data.get("location_in_building", None),
        data.get("equipment_type", None),
        data.get("age", None),
        data.get("equipment_name", None),
        data.get("manufacturer", None),
        data.get("model", None),
        data.get("serial_number", None),
        data.get("size", None),
        data.get("material", None),
    )
    
    try:
        cur.execute(query, values)
        conn.commit()
        last_id = cur.lastrowid
    except sqltor.Error as e:
        print(f"An error occurred: {e}")
        last_id = None
    finally:
        cur.close()
        conn.close()

    return last_id


def modify_entry(entry_id, data):
    conn = sqltor.connect(host="localhost", user="root",
                          passwd=password, database="junction")
    cur = conn.cursor()

    # Prepare the update query
    query = """
        UPDATE history SET 
            building_address = %s, 
            location_in_building = %s, 
            equipment_type = %s, 
            age = %s, 
            equipment_name = %s, 
            manufacturer = %s, 
            model = %s, 
            serial_number = %s, 
            size_of_machine = %s, 
            material = %s
        WHERE id = %s
    """
    # Define values including entry_id at the end
    values = (
        data["building_address"],
        data["location_in_building"],
        data["equipment_type"],
        data["age"],
        data["equipment_name"],
        data["manufacturer"],
        data["model"],
        data["serial_number"],
        data["size"],
        data["material"],
        entry_id
    )

    try:
        cur.execute(query, values)
        conn.commit()
    except sqltor.Error as e:
        print(f"An error occurred: {e}")
    finally:
        cur.close()
        conn.close()

    return cur.rowcount  # Returns the number of rows affected (should be 1 if successful)

def fetch_latest():
    conn = sqltor.connect(host="localhost", user="root",
                          passwd=password, database="junction")
    cur = conn.cursor()

    query = "SELECT * FROM history ORDER BY upload_time DESC LIMIT 1"  # LIMIT 1 to fetch the latest record only
    cur.execute(query)
    column_names = [desc[0] for desc in cur.description]
    row = cur.fetchone()  # fetch only the latest single row

    # If a row was fetched, create a dictionary from it
    result = dict(zip(column_names, row)) if row else None
    
    cur.close()
    conn.close()
    return result