def add_man(name,reason,level):
    import sqlite3

    connection = sqlite3.connect("Data Base/security.db")
    cursor = connection.cursor()
    cursor.execute('''
    INSERT INTO blacklist (username, reason, danger_level)
    VALUES (?, ?, ?)
    ''', (name, reason, level))
    connection.commit()
    print(f"пользователь {name} добавлен в черный список с причиной: {reason} и уровнем опасности: {level}")
    connection.close()

name1 = input("Введите имя пользователя для добавления в черный список: ")
reason1 = input("Введите причину добавления в черный список: ")
level1 = int(input("Введите уровень опасности (1-5): "))
add_man(name1, reason1, level1)
