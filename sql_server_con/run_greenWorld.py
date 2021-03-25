import pyodbc 

# https://docs.microsoft.com/en-us/sql/connect/python/pyodbc/step-3-proof-of-concept-connecting-to-sql-using-pyodbc?view=sql-server-ver15
import random
import datetime

server = r"localhost\sqlexpress"
database = "Monitoringdb" 
username = "grafanareader" # was granted insert
password = "grafanareader" # 
cnxn = pyodbc.connect("DRIVER={ODBC Driver 17 for SQL Server};SERVER="+server+";DATABASE="+database+";UID="+username+";PWD="+ password)
cursor = cnxn.cursor()


def get_version():
    cursor.execute("SELECT @@version;") 
    row = cursor.fetchone() 
    while row: 
        print(row[0])
        row = cursor.fetchone()


def insert_ cri():
    ran_number = random.randint(20,150)
    current_time_utc = datetime.datetime.utcnow()
    current_time_utc.strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute("""INSERT INTO test.criteria (c_name, c_start, c_end, c_w_id, c_status) VALUES (?,?,?)""", current_time_utc, ran_number, "TAG1") 
    cnxn.commit()

insert_ cri()
print(get_version())

