import sqlite3

conn = sqlite3.connect('Marta_8.db')

sql = conn.cursor()

conn.commit()


def add_table(user_id, username, first_name, vin_num):
    conn = sqlite3.connect('Marta_8.db')

    sql = conn.cursor()

    sql.execute(f'INSERT INTO users (user_id, username, first_name, vin_num) VALUES ("{user_id}", "{username}", "{first_name}","{vin_num}");')

    conn.commit()

def check_user():
    conn = sqlite3.connect('Marta_8.db')

    sql = conn.cursor()

    o = sql.execute('SELECT user_id FROM users;')

    users = [i[0] for i in o]

    conn.commit()

    return users

def check_user_two():
    conn = sqlite3.connect('Marta_8.db')

    sql = conn.cursor()

    o = sql.execute('SELECT * FROM users;')

    conn.commit()

    return o

def get_vin_num(vin_num):
    conn = sqlite3.connect('Marta_8.db')

    sql = conn.cursor()

    o = sql.execute(f'SELECT * FROM users WHERE vin_num={vin_num};')

    conn.commit()

    return o