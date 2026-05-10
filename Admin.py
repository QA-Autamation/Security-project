import sqlite3 
sec_conn = sqlite3.connect('Data Base/security.db')
sec_cursor = sec_conn.cursor()
reg_conn = sqlite3.connect('Data Base/registration_base.db')
reg_cursor = reg_conn.cursor()
print("--Добро пожаловать в административное меню!--")
def admin_menu():
    print("Административное меню:")
    print("1. Добавить пользователя в черный список")
    print("2. Просмотреть черный список")
    print("3. Выйти")
    print("4. Удалить пользователя из черного списка")
    print("5. Ничего не делать")
    print("6. Удалить пользователя из Регистрационной базы")
    choice = input("Выберите действие (1-6): ")
    
    if choice == '1':
        add_bad_man()
    elif choice == '2':
        view_blacklist()    
    elif choice == '3':
        print("Выход из административного меню.")
    elif choice == "4":
        delete_from_blacklist()
    elif choice == "5":
        nothing()
    elif choice == '6':
        delete_from_registration()
    else:
        print("Неверный выбор. Пожалуйста, выберите 1, 2, 3, 4, 5 или 6.")
        admin_menu()

def add_bad_man():
    name = input("Введите имя пользователя для добавления в черный список: ")
    reason = input("Введите причину добавления в черный список: ")
    level = int(input("Введите уровень опасности (1-5): "))
    
    sec_cursor.execute('''
    INSERT INTO blacklist (username, reason, danger_level)
    VALUES (?, ?, ?)
    ''', (name, reason, level))
    
    sec_conn.commit()
    print(f"Пользователь {name} добавлен в черный список с причиной: {reason} и уровнем опасности: {level}")   

def view_blacklist():
    sec_cursor.execute('SELECT * FROM blacklist')
    blacklist = sec_cursor.fetchall()
    
    if blacklist:
        print("Черный список пользователей:")
        for user in blacklist:
            print(f"ID: {user[0]}, Имя: {user[1]}, Причина: {user[2]}, Уровень опасности: {user[3]}")
    else:
        print("Черный список пуст.")
def delete_from_registration():
    name = input("Введите имя пользователя для удаления из регистрационной базы: ")
    reg_cursor.execute('DELETE FROM users WHERE username = ?', (name,))
    reg_conn.commit()
    print(f"Пользователь {name} удален из регистрационной базы.")
def delete_from_blacklist():
    name = input("Введите имя пользователя для удаления из черного списка: ")
    sec_cursor.execute('DELETE FROM blacklist WHERE username = ?', (name,))
    sec_conn.commit()
    print(f"Пользователь {name} удален из черного списка.")
def nothing():
    print("Ничего не делать.")
admin_menu()
print("Еще что-то нибудь? (y/n)")
if input().lower() == 'y':
    admin_menu()
elif input().lower() == 'n':
    print("Выход из программы.")
sec_conn.close()
reg_conn.close()
