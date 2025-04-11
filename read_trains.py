import sqlite3

# Підключення до бази даних
conn = sqlite3.connect(r"C:\Users\classuser34\PycharmProjects\pythonProject10\trains.db")
cursor = conn.cursor()

# Додаємо нові маршрути
cursor.execute("INSERT INTO trains (name, destination) VALUES ('Express 101', 'Kyiv')")
cursor.execute("INSERT INTO trains (name, destination) VALUES ('Fast 202', 'Lviv')")
cursor.execute("INSERT INTO trains (name, destination) VALUES ('Night Train 303', 'Odesa')")
cursor.execute("INSERT INTO trains (name, destination) VALUES ('Regional 404', 'Kharkiv')")
cursor.execute("INSERT INTO trains (name, destination) VALUES ('Luxury 505', 'Dnipropetrovsk')")
cursor.execute("INSERT INTO trains (name, destination) VALUES ('High Speed 606', 'Zaporizhzhia')")
cursor.execute("INSERT INTO trains (name, destination) VALUES ('Intercity 707', 'Vinnytsia')")
cursor.execute("INSERT INTO trains (name, destination) VALUES ('City Express 808', 'Sumy')")
cursor.execute("INSERT INTO trains (name, destination) VALUES ('Night Express 909', 'Mariupol')")
cursor.execute("INSERT INTO trains (name, destination) VALUES ('Super Fast 1010', 'Poltava')")
cursor.execute("INSERT INTO trains (name, destination) VALUES ('Grand Express 1111', 'Kherson')")
cursor.execute("INSERT INTO trains (name, destination) VALUES ('Northern Star 1212', 'Chernihiv')")
cursor.execute("INSERT INTO trains (name, destination) VALUES ('Mountain Route 1313', 'Ivano-Frankivsk')")
cursor.execute("INSERT INTO trains (name, destination) VALUES ('Express 1414', 'Ternopil')")
cursor.execute("INSERT INTO trains (name, destination) VALUES ('Southern Breeze 1515', 'Odessa')")

# Підтверджуємо зміни
conn.commit()

# Отримуємо список таблиць
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

# Виводимо всі таблиці
print("📌 Таблиці у базі даних:")
for table in tables:
    print(table[0])  # Виводимо назви всіх таблиць

# Виводимо всі маршрути з таблиці 'trains'
cursor.execute("SELECT name, destination FROM trains")
rows = cursor.fetchall()
print("\n📑 Маршрути поїздів:")
for row in rows:
    print(f"🚂 {row[0]} - {row[1]}")

# Закриваємо з'єднання з базою даних
conn.close()
