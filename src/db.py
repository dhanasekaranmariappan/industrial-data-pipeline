import os
from dotenv import load_dotenv
import mysql.connector

load_dotenv()

def setup_database():
    """Create database and tables if they don't exist."""
    password = os.getenv("SQL_PASSWORD")
    if not password:
        raise ValueError("SQL_PASSWORD environment variable is required")
    
    conn = mysql.connector.connect(
        host=os.getenv("SQL_HOST", "localhost"),
        user=os.getenv("SQL_USERNAME", "root"),
        password=password
    )
    cursor = conn.cursor()
    
    cursor.execute("CREATE DATABASE IF NOT EXISTS industrial_analytics")
    cursor.execute("USE industrial_analytics")
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS machine_data (
        id INT AUTO_INCREMENT PRIMARY KEY,
        air_temperature FLOAT,
        process_temperature FLOAT,
        rotational_speed FLOAT,
        torque FLOAT,
        tool_wear INT,
        power FLOAT,
        temp_diff FLOAT
    )
    """)
    
    conn.commit()
    conn.close()

def connect():
    password = os.getenv("SQL_PASSWORD")
    if not password:
        raise ValueError("SQL_PASSWORD environment variable is required")
    
    return mysql.connector.connect(
        host=os.getenv("SQL_HOST", "localhost"),
        user=os.getenv("SQL_USERNAME", "root"),
        password=password,
        database="industrial_analytics"
    )

def insert_dataframe(df):
    conn = connect()
    cursor = conn.cursor()

    for _, row in df.iterrows():
        cursor.execute("""
        INSERT INTO machine_data
        (air_temperature, process_temperature, rotational_speed, torque, tool_wear, power, temp_diff)
        VALUES (%s,%s,%s,%s,%s,%s,%s)
        """, (
            row['air_temperature_[k]'],
            row['process_temperature_[k]'],
            row['rotational_speed_[rpm]'],
            row['torque_[nm]'],
            row['tool_wear_[min]'],
            row['power'],
            row['temp_diff']
        ))

    conn.commit()
    conn.close()

