import sqlite3 as sql
# #
# # conn = sql.connect("D:/Works/RASAs/rasa0/Database/rasa.db")
# # cu = conn.cursor()
# #
# # conn.execute("insert into USER(id, acc, password, balance) values (1, 'PQF', '132475', 3000)")
# # conn.commit()
#
# conn = sql.connect("D:/Works/RASAs/rasa0/Database/rasa.db")
#
# def hh(conn):
#     new_acc = "new_account"
#     new_password = "password"
#     s = "insert into USER(acc, password, balance) values (?, ?, 0)"
#     conn.execute(s, (new_acc, new_password, ))
#     conn.commit()
#
# hh(conn)


# def run():
#     conn = sql.connect("D:/Works/RASAs/rasa0/Database/rasa.db")
#     cu = conn.cursor()
#
#
#
#     conn.execute("insert into USER(acc, password, balance) values ('PQF1', '132475', 3000)")
#     conn.execute("insert into USER(acc, password, balance) values ('PQF2', '132475', 34000)")
#     conn.execute("insert into USER(acc, password, balance) values ('PQF3', '132555', 300)")
#     conn.commit()
#
#     acc = "new_account"
#     password = "password"
#
#     f = "select password from USER where acc = ?"
#     cu.execute(f, (acc, ))
#
#     row = cu.fetchone()
#     print(row[0])
#
#     # print(compare_password)
#
#     # if compare_password == password:
#     #     s = "select balance from USER where acc = ?"
#     #     res = conn.execute(s, (acc, ))
#     #
#     #     print(res)
#
#     return []
#
#
# def run2():
#     conn = sql.connect("D:/Works/RASAs/rasa0/Database/rasa.db")
#     cu = conn.cursor()
#
#     acc = "PQF3"
#
#     f = "select password from USER where acc = ?"
#     res = cu.execute(f, (acc, ))
#
#     print(res.fetchone()[0])


# def run3():
#     conn = sql.connect("D:/Works/RASAs/rasa0/Database/rasa.db")
#     cu = conn.cursor()
#
#     acc = "PQF3"
#     password = "132475"
#
#     f = "select password from USER where acc = ?"
#     compare_password = cu.execute(f, (acc, ))
#
#     if password == compare_password.fetchone()[0]:
#         s = "select balance from USER where acc = ?"
#         res = cu.execute(s, (acc, ))
#
#         print(res.fetchone()[0])
#     else:
#         print("fuck you!")
#
# run3()
#
#
# def run4():
#     conn = sql.connect("D:/Works/RASAs/rasa0/Database/rasa.db")
#     cu = conn.cursor()
#
#     print(cu.fetchone())
#
# run4()
