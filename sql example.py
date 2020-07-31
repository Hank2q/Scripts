import sqlite3
import os
conn = sqlite3.connect('data.db')

try:
    conn.execute('''
    CREATE TABLE files (filename primary key not null, data text)''')
except Exception:
    pass


# def insert(connection, filename):
#     try:
#         with open(filename, 'rb') as file:
#             data = file.read()
#             connection.execute(
#                 """insert into files values (?, ?);""", (filename, data))
#             connection.commit()
#             os.remove(filename)
#     except FileNotFoundError as e:
#         print(e)


# def select(connection):
#     output = connection.execute('''select * from files''')
#     return output.fetchall()


# def get_file(connection, filename):
#     result = connection.execute(
#         '''SELECT filename, data FROM files where filename=?''', (filename,))
#     return result.fetchone()


# def open_file(connection, filename):
#     name, data = get_file(connection, filename)
#     with open(name, 'wb') as file:
#         file.write(data)
#     os.popen(name)


# def list_files(connection):
#     output = connection.execute('''select filename from files''')
#     return [name[0]for name in output.fetchall()]


# def remove_file(connection, filename):
#     connection.execute('DELETE FROM files where filename=?', (filename,))
#     connection.commit()


# with open('logo2.png', 'rb') as file:
#     insert(conn, id=4, name=file.name, data=file.read())


# result = select(conn)
# for line in result[:1]:
#     i, n, d = line
#     print(f'{i}| {n:10}| {d}')


# print(get_file(conn, 'logo1.png'))


# print(list_files(conn))
