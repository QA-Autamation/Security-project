import sqlite3

connection = sqlite3.connect('security.db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS blacklist (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    reason TEXT,
    danger_level INTEGER DEFAULT 1
)
''')


connection.commit()
print("База данных готова, таблица создана!")
