import sqlite3
import os

db_folder = os.path.join(os.path.dirname(__file__), "db_car.db")

def car_name():
    data = []
    conn = sqlite3.connect(db_folder)
    sql = """
        SELECT name, category , price, instock
        FROM car
        ORDER BY name
    """
    cursor = conn.execute(sql)
    rows = cursor.fetchall()

    for row in rows:
        record = {
            'name': row[0],
            'category': row[1],
            'price': row[2],
            'instock':row[3]
            }
        data.append(record)
    
    conn.close()
    return data

def find_carname(car):
    
    data = []
    conn = sqlite3.connect(db_folder)
    sql = """
        SELECT name, category , price, instock
        FROM car
        WHERE name=?
    """
    val = (car,)
    cursor = conn.execute(sql,val)
    rows = cursor.fetchone()

    record = {
        'name': rows[0],
        'category': rows[1],
        'price': rows[2],
        'instock':rows[3]
        }
    data.append(record)
    
    conn.close()
    return data

def car_name_add(name,category,price,instock):
    conn = sqlite3.connect(db_folder)
    sql = """
        INSERT INTO car(name,category,price,instock)
        VALUES(?,?,?,?)
    """
    val = (name,category,price,instock)
    cursor = conn.execute(sql, val)
    conn.commit()
    conn.close()
    return "Car Has Been Created successfully"

def car_delete(car):
    conn = sqlite3.connect(db_folder)
    sql = """
        DELETE FROM car
        WHERE name=?
    """
    val = (car,)
    cursor = conn.execute(sql, val)
    conn.commit()
    conn.close()
    return "Car Has Been Deleted successfully"

def update_car(name,category,price,instock):
    conn = sqlite3.connect(db_folder)
    sql = """
        UPDATE car
        SET category=? , price=?, instock=?
        WHERE name=?
    """
    val = (category,price,instock,name)
    cursor = conn.execute(sql, val)
    conn.commit()
    conn.close()
    return "Car Has Been Update successfully"
