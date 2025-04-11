import sqlite3

# Використовуємо інший шлях, наприклад, в поточній директорії проекту
conn = sqlite3.connect(r"C:\Users\classuser34\PycharmProjects\pythonProject10\trains.db")
cursor = conn.cursor()

# Створення таблиці, якщо вона не існує
cursor.execute("""
CREATE TABLE IF NOT EXISTS trains (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    destination TEXT
)
""")

# Вставка даних
cursor.execute("INSERT INTO trains (name, destination) VALUES ('Express 101', 'Ivano-Frankivsk')")
cursor.execute("INSERT INTO trains (name, destination) VALUES ('Fast 202', 'Japan')")

# Збереження змін
conn.commit()
conn.close()

print("✅ Дані успішно додані!")
