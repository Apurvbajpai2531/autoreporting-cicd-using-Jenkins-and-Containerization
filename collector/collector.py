import time
import psutil
import psycopg2
from datetime import datetime

while True:
    try:
        conn = psycopg2.connect(
            dbname="postgres",
            user="postgres",
            password="password",
            host="db"
        )
        break
    except psycopg2.OperationalError:
        print("Waiting for database...")
        time.sleep(3)

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS metrics (
    id SERIAL PRIMARY KEY,
    cpu FLOAT,
    memory FLOAT,
    disk FLOAT,
    created_at TIMESTAMP
)
""")
conn.commit()

while True:
    cpu = psutil.cpu_percent()
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent

    cursor.execute(
        "INSERT INTO metrics (cpu, memory, disk, created_at) VALUES (%s, %s, %s, %s)",
        (cpu, memory, disk, datetime.now())
    )
    conn.commit()

    print(f"Saved metrics | CPU: {cpu}% MEM: {memory}% DISK: {disk}%")
    time.sleep(60)
