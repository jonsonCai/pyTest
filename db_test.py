import cx_Oracle


conn = cx_Oracle.connect("SCOTT/abc123@127.0.0.1/AkiDemo")
cursor = conn.cursor()
cursor.execute("select * from USERS")
result = cursor.fetchall()
print(result)

cursor.close()
conn.close()
