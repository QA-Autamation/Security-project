import sqlite3


security_conn = sqlite3.connect('Data Base/security.db')
security_cursor = security_conn.cursor()

reg_conn = sqlite3.connect('Data Base/registration_base.db')
reg_cursor = reg_conn.cursor()


def check_secerity(name):
    security_cursor.execute('SELECT * FROM blacklist WHERE username = ?', (name,))
    result = security_cursor.fetchone()
    return result 

def sign_up():
    name = input("Введите имя пользователя для регистрации: ")
    password = input("Введите пароль для регистрации: ")
    
    danger = check_secerity(name)
    
    if danger:

        print(f"🛑 ОШИБКА: Пользователь {name} в черном списке!")
        print(f"Причина: {danger[2]}, Уровень опасности: {danger[3]}")
    else:
        reg_cursor.execute('''
        INSERT INTO users (username, password)
        VALUES (?, ?)
        ''', (name, password))
        reg_conn.commit()
        print(f"✅ Пользователь {name} успешно зарегистрирован!")


def get_reservation():
    name = input("Введите имя пользователя для входа: ")
    password = input("Введите пароль для входа: ")
    
    reg_cursor.execute('''
    SELECT * FROM users WHERE username = ? AND password = ?
    ''', (name, password))
    result = reg_cursor.fetchone()
    
    if result:
        print("🔓 Успешный вход в систему!")
    else:
        print("🔒 Ошибка: Неверное имя или пароль.")




sign_up()


print("\n--- Попытка входа ---")
get_reservation()


security_conn.close()
reg_conn.close()
