import sqlite3

conn = sqlite3.connect("clinic.db")
c = conn.cursor()
try:
    c.execute(
        "CREATE TABLE PATIENTS (ID INTEGER PRIMARY KEY AUTOINCREMENT, NAME TEXT, AGE TEXT)"
    )
except:
    # This will delete the table and create again
    c.execute("DROP TABLE PATIENTS")
    c.execute(
        "CREATE TABLE PATIENTS (ID INTEGER PRIMARY KEY AUTOINCREMENT, NAME TEXT, AGE TEXT)"
    )
qName = input("INPUT NAME:")
qAge = input("INPUT AGE:")
c.execute('INSERT INTO PATIENTS (NAME, AGE) VALUES ("' + qName + '", "' + qAge + '")')
print("ADDED TO THE DATABASE.")
print("PATIENTS INFO (ID, NAME, AGE):")
for row in c.execute("SELECT * FROM PATIENTS"):
    print(row)
input()
conn.commit()
conn.close()
