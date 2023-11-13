import mysql.connector as db

HOST = "db4free.net"
PORT = 3306
USER = "sqlworkshop"
PASSWORD = "pambidluis"
DB = "sqlworkshop"

try:
    con = db.connect(host=HOST, port=PORT, user=USER, passwd=PASSWORD, db=DB)
    cur = con.cursor()

    cur.execute("DROP TABLE IF EXISTS IOT")

    cur.execute(
        """CREATE TABLE IOT
                (TEMPERATURE FLOAT,
                HUMIDITY FLOAT)"""
    )

    cur.execute("INSERT INTO IOT (TEMPERATURE, HUMIDITY) VALUES (32.4, 3.14)")

    cur.execute("SELECT * FROM SQLWORKSHOP")

    result = cur.fetchall()

    for row in result:
        print(row)

    con.commit()

except Exception as e:
    print(e)

finally:
    con.close()
